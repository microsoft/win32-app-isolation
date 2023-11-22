import argparse
import os
import platform
import re
import subprocess
import tempfile
from dataclasses import dataclass


@dataclass
class IsolateConfig:
    output: str
    cert: str
    signtool: str
    makeappx: str
    working_dir: str
    msix: str
    capabilities: list[str]


class Manifest:
    def __init__(self, path: str, config: IsolateConfig):
        self.path = path
        self.config = config
        with open(path, "r") as f:
            self.str = f.read()

    def modify_package(self, s: str):
        m = re.search(r"<Package\s+.*?>", s, re.MULTILINE | re.DOTALL)
        if m:
            package = m.group(0)
            if "IgnorableNamespaces" not in package:
                package = package.replace(">", ' IgnorableNamespaces="">')

            if "xmlns:previewsecurity2=" not in package:
                package = package.replace(">", ' xmlns:previewsecurity2="http://schemas.microsoft.com/appx/manifest/preview/windows10/security/2">')
                package = package.replace('IgnorableNamespaces="', 'IgnorableNamespaces="previewsecurity2 ')
            
            if "xmlns:uap10=" not in package:
                package = package.replace(">", ' xmlns:uap10="http://schemas.microsoft.com/appx/manifest/uap/windows10/10">')
                package = package.replace('IgnorableNamespaces="', 'IgnorableNamespaces="uap10 ')

            if "xmlns:rescap=" not in package:
                package = package.replace(">", ' xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities">')
                package = package.replace('IgnorableNamespaces="', 'IgnorableNamespaces="rescap ')

            s = s.replace(m.group(0), package)
            return s
        else:
            raise ValueError("No package found in manifest")

    def modify_target_device_family(self, s: str):
        m = re.search(r"<TargetDeviceFamily\s+.*?>", s, re.MULTILINE | re.DOTALL)
        if m:
            target_device_family = m.group(0)
            s = s.replace(target_device_family, '<TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.25357.0" MaxVersionTested="10.0.25357.0" />')
        return s

    def modify_application(self, s: str):
        for m in re.finditer(r"<Application\s+.*?>", s, re.MULTILINE | re.DOTALL):
            application = m.group(0)
            application = re.sub('EntryPoint=".*?"', "", application)
            application = re.sub(' .*?TrustLevel=".*?"', "", application)
            application = re.sub(' .*?RuntimeBehavior=".*?"', "", application)
            application = application.replace(">", ' uap10:TrustLevel="appContainer" previewsecurity2:RuntimeBehavior="appSilo">')
            s = s.replace(m.group(0), application)
        return s

    def modify_capabilities(self, s: str):
        m = re.search(r"<Capabilities>.*?</Capabilities>", s, re.MULTILINE | re.DOTALL)
        if m:
            capabilities = m.group(0)
            capabilities = re.sub(r'<rescap:Capability\s+Name="runFullTrust"\s+/>', '', capabilities)
            for capability in self.config.capabilities:
                capabilities = capabilities.replace("</Capabilities>", f'<rescap:Capability Name="{capability}" />\n</Capabilities>')
            s = s.replace(m.group(0), capabilities)
        elif self.config.capabilities:
            capabilities = '<Capabilities>\n</Capabilities>'
            for capability in self.config.capabilities:
                capabilities = capabilities.replace("</Capabilities>", f'<rescap:Capability Name="{capability}" />\n</Capabilities>')
            s = s.replace("</Package>", capabilities + "</Package>")
        return s

    def process(self):
        self.str = self.modify_package(self.str)
        self.str = self.modify_target_device_family(self.str)
        self.str = self.modify_application(self.str)
        self.str = self.modify_capabilities(self.str)

    def save(self, path=None):
        if not path:
            path = self.path
        with open(path, "w") as f:
            f.write(self.str)


def unpack(config: IsolateConfig):
    print("Unpacking...")
    # Create working directory
    os.makedirs(config.working_dir, exist_ok=True)

    # Extract the package
    subprocess.check_call(f"{config.makeappx} unpack /p {config.msix} /d {os.path.join(config.working_dir, 'unpack')}", shell=True)


def pack_and_sign(config: IsolateConfig):
    print("Repacking...")
    # Repack the package
    subprocess.check_call(f"{config.makeappx} pack /nv /d {os.path.join(config.working_dir, 'unpack')} /p {config.output}", shell=True)

    # Sign the package
    subprocess.check_call(f"{config.signtool} sign /fd SHA256 /f {config.cert} {config.output}", shell=True)


def modify_manifest(config: IsolateConfig):
    manifest = Manifest(os.path.join(config.working_dir, "unpack", "AppxManifest.xml"), config)
    manifest.process()
    manifest.save()


def check_requirements(args):
    if platform.system() != "Windows":
        print("This script only works on Windows")
        exit(1)

    if int(platform.version().split(".")[2]) < 25357:
        print("WARNING! This script might not work on your Windows version. You need at least 10.0.25357")

    try:
        subprocess.call([args.signtool, "/?"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(f"{args.signtool} is not found, pass your signtool.exe path with --signtool")
        exit(1)

    try:
        subprocess.call([args.makeappx, "/?"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(f"{args.makeappx} is not found, pass your makeappx.exe path with --makeappx")
        exit(1)

    for capability in args.capability:
        if capability != "runFullTrust" and not capability.startswith("isolatedWin32"):
            print(f"Invalid capability: {capability}. Only runFullTrust and isolatedWin32-* are supported")
            exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", default=None)
    parser.add_argument("--cert", "-c", required=True)
    parser.add_argument("--capability", "--cap", action="append", default=[])
    parser.add_argument("--signtool", default="signtool.exe")
    parser.add_argument("--makeappx", default="makeappx.exe")
    parser.add_argument("msix")

    args = parser.parse_args()

    check_requirements(args)

    with tempfile.TemporaryDirectory() as tmpdir:
        config = IsolateConfig(
            output=os.path.abspath(args.output),
            cert=args.cert,
            signtool=args.signtool,
            makeappx=args.makeappx,
            working_dir=os.path.abspath(tmpdir),
            msix=os.path.abspath(args.msix) if args.msix else None,
            capabilities=args.capability,
        )

        unpack(config)
        modify_manifest(config)
        pack_and_sign(config)


if __name__ == "__main__":
    main()
