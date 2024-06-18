# Win32 App Isolation Introduction

### Target Applications

* Win32
* Desktop Bridge (Centennial)

### Minimum Requirements:

* Windows insider version >= 25357 (Canary channel only)
* Dev tool to package
    * [Visual Studio](https://visualstudio.microsoft.com/) version 17.10.2 or greater
    * or [Customized MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1)
* (optional) [ACP](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [WPR](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder), if need to identify the capabilities to use

### Creating a Win32 App Isolation App:

* If you are using Visual Studio to build your project
    * Follow the [instructions](packaging/packaging-with-visual-studio.md) for Visual Studio
* Or if you have the Win32 installer / MSIX package
    * [Create](packaging/msix-packaging-tool.md#win32---msix) the MSIX package from the Win32 installer
    * [Turn](packaging/msix-packaging-tool.md#msix---isolated-win32) the MSIX Package to isolated Win32 app
* If you need to Identify the required capabilities
    * Use [Application Capability Profiler](profiler/application-capability-profiler.md)
    * Repackage the app with the capabilities
