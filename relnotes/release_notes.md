# Public Preview 
## win32-app-isolation 
Release notes for the tools can be found [here](https://github.com/microsoft/win32-app-isolation/releases)

## Windows Insider Canary Channel build 25357 (2023-05-04)
This build contains the underlying infrastructure to install and run isolated applications and support for capabilities which include:
1. Implicit brokering for the open file dialog and other APIs.
2. Printing.
3. System tray icons.
4. Shell notifications.
5. File system privacy settings to reset file access permissions. 
6. Integration with Windows Privacy App Permissions pages.

# Coming soon 
Windows Insider Canary builds after June 2023 will add support for capabilities for isolated applications which include:
1. File consent prompt reduction for legacy directory browsing, translating between shell display names and item identifiers, and isolated application launch through the context menu.
2. Drag and drop into applications.
3. Application multi-instancing with ShellExecute.
