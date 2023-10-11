# Win32 App Isolation Introduction

### Target Applications

* Win32
* Centennial

### Minimum requirements:

* Windows insider version >= 25357
* [Customized MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) This version is required to build a Win32 App Isolation application
* If is needed to know which capabilities are required, one can use [ACP](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [WPR](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder)

### Creating a Silo App:

1. Create an MSIX package from Win32 installer *if the app is not already MSIX* ([step 1](docs/packaging/msix-packaging-tool.md#win32---msix))
2. Turn the MSIX Package to Win32 App Isolation ([step 2](docs/packaging/msix-packaging-tool.md#msix---isolated-win32))
3. Identify the Required Capabilities Using [ACP](docs/profiler/application-capability-profiler.md)
4. Repackage the app with the capabilities just found
