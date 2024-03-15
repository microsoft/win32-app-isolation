# Command line tools to package and isolate applications

## Package

You can convert your `msi` or `exe` installers to `msix` using `package.py`.

### Requirement

* Python3
* MSIX Packaging Tool
* A [template](https://learn.microsoft.com/en-us/windows/msix/packaging-tool/generate-template-file) file.
  You can also use the [example](./template.xml) we give as a start

### Usage

#### Prepare your template

The best way to generate a template is to use MSIX Packaging Tool to [package](../../docs/packaging/msix-packaging-tool.md#win32---msix)
your application once and save the template.

However, you can also fill in the template manually. The most important sections are `<PackageInformation>` and `<Applications>`

*Note: you have to fill the `PublisherName` field of `<PackageInformation>` accurately (matching your cert) in order to sign the package*

#### Run the script

```
python package.py --template template.xml -o app.msix installer.msi 
```

Under the hood, this is very similar to using
[MSIX Packaging Command Line Tool](https://learn.microsoft.com/en-us/windows/msix/packaging-tool/package-conversion-command-line)

The script helps you fill the `<Installer>` and `<SaveLocation>` according to your input, but feel free to use `MsixPackagingTool.exe`
directly.

*Note: this step requires an elevation because `MsixPackagingTool.exe` needs it*

#### Finish the installation

You need to go though the installation of the application. To make sure this works properly, the app should be uninstalled first
if it's already installed.

## Isolate

You can isolate your `msix` package using `isolate.py`.

### Requirement

* Python3
* [MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases)
* `.pfx` certification to sign your package

### Usage

```
python isolate.py --cert your_cert.pfx -o isolated.msix app.msix
```

The command will try to use the `makeappx.exe` and `signtool.exe` from your MSIX Packaging Tool.
If you want to use your own SDK version, use `--sdk_dir` to pass the directory that has the
binaries.

In order to add capabilities, use `--capability` or `--cap` like

```
python isolate.py --cert your_cert.pfx -o isolated.msix --cap runFullTrust --cap isolatedWin32-promptForAccess app.msix
```
