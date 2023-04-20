# Table of Contents
1. [Convert an existing win32 installer into an .msix app](#win32_AppSilo)
2. [Convert an existing .msix app to run in an AppSilo](#MSIX_AppSilo)

## Win32 -> MSIX <a name="win32_AppSilo"></a>

1. Select "Application Pacakge" on the far left and choose where the package will be created. This flow will follow the "Create package on this computer" option.

    ![image](https://user-images.githubusercontent.com/128075585/231865964-b1892885-52c2-4a8f-af4d-a95c6a655d3a.png)

2. Wait for the "MSIX Packaging Tool Driver" field to finish checking

    ![image](https://user-images.githubusercontent.com/128075585/231866875-281b5727-df14-4a9e-b53d-ebebf95c4d13.png)

3. Use the browse button to navigate to and select your win32 installer. Leave signing preference blank as we will need to edit the manifest and sign it again.

    ![image](https://user-images.githubusercontent.com/128075585/233446591-deecc616-ec69-48ed-bbee-48aa80ecbd07.png)


4. Enter your package information

    ![image](https://user-images.githubusercontent.com/128075585/231867726-bc50988a-251a-4067-b35c-bcc8fe55310f.png)

5. Go through the win32 installer as normal
6. If there are additional entry points besides the main one, launch or browse to them. If your app has options for File Type Association in settings/config/preferences, toggle them at this step so MSIX will pick up on them

7. Repeat the same process if there are services in your package
8. Clicking Create will save the package as a full trust package. Click the "Package Editor" button to go to the "Package Editor" flow from the main menu
    
   ![image](https://user-images.githubusercontent.com/128075585/231869540-fa8c5078-8f7f-4d8c-94e5-ce6006bf74e3.png)


## MSIX -> AppSilo <a name="MSIX_AppSilo"></a>
1. Select "Application Pacakge" on the far right. Browse to your .msix file and click the "Open package" button. You skip this step if you've come from the package creation flow.

   ![image](https://user-images.githubusercontent.com/128075585/231865964-b1892885-52c2-4a8f-af4d-a95c6a655d3a.png)

2. Scroll down to the "Manifest file" section and click "Open file"

   ![image](https://user-images.githubusercontent.com/128075585/231869898-3c306ff9-eeb8-4998-8354-8043f51401bc.png)

  Add `xmlns:previewsecurity2="http://schemas.microsoft.com/appx/manifest/preview/windows10/security/2"` to the <Package> element
 
  Add `previewsecurity2` to `IgnorableNamespaces` at the end of the `<Package>` element
  
  In <Dependencies> change TargetDeviceFamily to `<TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.22622.0" MaxVersionTested="10.0.22622.0" />`
  
  In <Application> replace any existing entrypoint/trustlevel/runtimebehavior with `uap10:TrustLevel="appContainer" previewsecurity2:RuntimeBehavior="appSilo"`

  ![image](https://user-images.githubusercontent.com/128075585/231876449-09171326-a48f-4e8d-b455-f0b1c59151ac.png)

3. If your app needs to do any of the following, you will need to add the capabilities, In this case I've added the isolatedWin32-print capability since NotePad++ is a text editor
* isolatedWin32-dotNetBreadcrumbStore - 
* isolatedWin32-print - Printing documents 
* isolatedWin32-profilesRootMinimal -  
* isolatedWin32-sysTrayIcon - Display notifications from the Systray
* isolatedWin32-userProfileMinimal -
* isolatedWin32-shellExtensionContextMenu - Display COM-based context menu entries
* isolatedWin32-volumeRootMinimal -
* isolatedWin32-promptForAccess - Prompt Users for file access
* isolatedWin32-accessToPublisherDirectory - Access to directories that end with the publisher ID

4. Select Create/Save