# Win32 App Isolation Introduction

### Target Applications

* Win32
* Desktop Bridge (Centennial)

### Minimum Requirements:

* Windows insider version >= 25357 (Canary channel only)
* [Customized MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) This version is required to build a Win32 app isolation application
* If is needed to know which capabilities are required, one can use [ACP](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [WPR](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder)

### Creating a Win32 App Isolation App:

There are two mechanisms for creating and converting an MSIX package to be ready to use app silo. One option is to use the MSIX packaging tool. The other option is to use Visual Studio.

1. Create and convert an MSIX package to be ready to use AppSilo. 
   * Using MSIX packaing tool
     1. Create an MSIX package from Win32 installer *if the app is not already MSIX* ([step 1](packaging/msix-packaging-tool.md#win32---msix))
     2. Turn the MSIX Package to isolated Win32 app ([step 2](packaging/msix-packaging-tool.md#msix---isolated-win32))

   * Using Visual Studio ([step 1](packaging/packaging-with-visual-studio.md))
2. Identify the required capabilities using [ACP](profiler/application-capability-profiler.md)
3. Repackage the app with the capabilities just found
