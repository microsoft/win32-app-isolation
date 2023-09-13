# Welcome to Win32 App Isolation Introduction

### Target Applications

* Win32
* Centennial apps.

### Minimum requirements:

* Windows insider version >= 25357
* [MPT v1.2023.517.0] (https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1)
* If is needed to know which capabilities are required, one will use ACP (check the MPT link) and [WPR] (https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder)

### Creating a Silo App:

[Detailed instructions] (https://github.com/microsoft/win32-app-isolation/blob/v0.1.1/docs/packaging/msix-packaging-tool.md)
1.	Create an MSIX package from Win32 installer (if the app is not already MSIX)
2.	Turning the MSIX Package to Win32 App Isolation
3.	Identifying the Required Capabilities Using [ACP] (https://github.com/microsoft/win32-app-isolation/blob/v0.1.1/docs/profiler/application-capability-profiler.md)
