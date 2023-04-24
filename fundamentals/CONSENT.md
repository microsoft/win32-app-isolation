## Resetting Consent for Isolated Win32 Apps

## How file access consent is granted

Consent is granted for Isolated Win32 Apps in three ways.
1. Prompting: If the application has the isolatedWin32-promptForAccess capability, the first time the app attempts to access a file or directory, a prompt will be generated for the user to accept or decline. The choice will be saved until the consent is revoked
2. Implicit-Consent: If the application has file type associations registered, then opening the file through the context menu, or setting the isolated app as the default application and opening a file, will grant access without prompting. This also extends to dragging a file onto the app will also grant access.
3. Publisher Directory: If the application has the isolatedWin32-accessToPublisherDirectory capability, then the app will have full access to directories with names ending with the publisher ID of the app located in \Device\BootDevice\ProgramData.
4. File Dialog: Files that are selected or created through Window's file dialog created from an isolated app, will also have their access granted to the isolated app.

## How consent is revoked
Consent can currently be revoked in two ways.
1. Settings: Through the settings, navigate to "Reset file permissions on isolated Win32 applications". On this page you can fully reset the consent granted to specific isolated apps. This will reset both prompted and implicit consent, but won't affect the publisher directory. 
2. Uninstall: During uninstall, all consent will be revoked.