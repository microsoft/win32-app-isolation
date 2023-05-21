# Windows Release Notes
This file contains the summary of changes in Windows OS releases, available through the Insider Canary Channel, for Win32 app isolation.
Release notes for the tools can be found in the [releases](../../../releases) section of the repo.

## Windows build 25357 (2023-05-04)
This Windows release contains the underlying infrastructure to install and run isolated applications, and support for capabilities for
these applications which include:
1. Implicit brokering for the open file dialog and other APIs.
2. Printing.
3. System tray icons.
4. Shell notifications.
5. File system privacy settings to reset file access permissions. 
6. Integration with Windows Privacy App Permissions pages.

## Coming soon 
Windows releases on the Insider Canary Channel after June 2023 will add support for capabilities for isolated applications which include:
1. File consent prompt reduction for
* Legacy directory browsing
* Translating between shell display names and item identifiers
* Isolated application launch through the context menu.
2. Drag and drop into applications.
3. Application multi-instancing with ShellExecute.
