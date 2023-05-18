# Public Preview 
## Windows Insider Canary Channel OS build 25357 (2023-05-04)
## Application Capability Profiler v0.1.0 (2023-05-16) 
## MSIX Packaging Tool v1.2023.517.0 (2023-05-17)

# Windows Insider Canary Channel OS build 25357 (2023-05-04)  
This build contains the underlying infrastructure to install and run isolated applications and support for capabilities which include:
1. Implicit brokering for the open file dialog and other APIs.
2. Printing.
3. System tray icons.
4. Shell notifications.
5. File system privacy settings to reset file access permissions. 
6. Integration with Windows Privacy App Permissions pages.

# Application Capability Profiler v0.1.0 (2023-05-16)
1. ApplicationCapabilityProfiler PowerShell 7 module to enable access attempt profiling via the following cmdlets:
    * Start-Profiling: instruments target application packages for trace logging and starts access attempt trace logging via wpr.
    * Stop-Profiling: takes away trace logging instrumentation from target application packages, stops trace logging and collects trace file.
    * Get-ProfilingResults: parses trace file to find access denied events for target application packages and outputs access capabilities to be declared in the application package manifest. Additional error and diagnostic information are also output.
    * Merge-ProfilingResults: utility to merge the output of multiple runs of Get-ProfilingResults.
2. ACP supports automatic inclusion of capabilities in target application package manifest.
3. The file ACP-StackTrace.wpaProfile is provided to configure Windows Performance Analyzer (WPA) to display relevant stack information in the analysis view of the collected traces.

# MSIX Packaging Tool v1.2023.517.0 (2023-05-17)
Initial support to package MSIX applications to run isolated with broad support for extensions, such as to support COM servers, file type associations, modern and classic context menus.

# Coming soon 
Windows Insider Canary builds after June 2023 will add support for capabilities for isolated applications which include:
1. File consent prompt reduction for legacy directory browsing, translating between shell display names and item identifiers, and isolated application launch through the context menu.
2. Drag and drop into applications.
3. Application multi-instancing with ShellExecute.
