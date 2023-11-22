import argparse
import os
import subprocess
import tempfile
import xml.etree.ElementTree as XMLET
from dataclasses import dataclass


@dataclass
class PackageConfig:
    template: str
    output: str
    working_dir: str
    installer: str


def make_msix(config: PackageConfig):
    ns = {
        "V1": "http://schemas.microsoft.com/appx/msixpackagingtool/template/2018",
        "V2": "http://schemas.microsoft.com/appx/msixpackagingtool/template/1904",
        "V3": "http://schemas.microsoft.com/appx/msixpackagingtool/template/1907",
        "V4": "http://schemas.microsoft.com/appx/msixpackagingtool/template/1910",
        "V5": "http://schemas.microsoft.com/appx/msixpackagingtool/template/2001",
    }
    tree = XMLET.parse(config.template)
    root = tree.getroot()

    # Set the save location for template
    save_location = root.find("V1:SaveLocation", ns)
    if not save_location:
        save_location = XMLET.Element(f"{{{ns['V1']}}}SaveLocation")
        save_location.set("PackagePath", config.output)
        root.append(save_location)

    # Set the installer to use
    installer = root.find("V1:Installer", ns)
    if not installer:
        if not config.installer:
            print("No installer is passed, please pass your installer or add it to the template")
            exit(1)
        installer = XMLET.Element(f"{{{ns['V1']}}}Installer")
        installer.set(f"Path", config.installer)
        if config.installer.endswith(".exe"):
            installer.set(f"Arguments", "/qn /norestart INSTALLSTARTMENUSHORTCUTS=1 DISABLEADVTSHORTCUTS=1")
        root.append(installer)

    template_path = os.path.join(config.working_dir, "template.xml")
    tree.write(template_path)

    # Create the package
    subprocess.call(f"MsixPackagingTool.exe create-package --template {template_path}", shell=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", "-t", required=True)
    parser.add_argument("--output", "-o", default="app.msix")
    parser.add_argument("installer", nargs="?")

    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmpdir:
        config = PackageConfig(
            template=args.template,
            output=os.path.abspath(args.output),
            working_dir=os.path.abspath(tmpdir),
            installer=os.path.abspath(args.installer) if args.installer else None,
        )

        make_msix(config)


if __name__ == "__main__":
    main()