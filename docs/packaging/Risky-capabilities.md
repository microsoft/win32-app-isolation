# Risky Capabilities

This page specifically focuses on capabilities that are incompatible with win 32 app isolation. The following capabilities can lower the security offered by win32 app isolation and application developers should refrain from using them when onboarding to win32 app isolation. 

* "uiAccess"
* "allowElevation"
* "inputInjectionBrokered"
* "oemDeployment"
* "packagedServices"
* "localSystemServices"
* "enterpriseAuthentication"

The following capabilities are not compatible with Win32 app isoltaion. They may cause the application not to work

* "packageManagement"
* "cortanaPermissions"
* "backgroundVoIP"
* "broadFileSystemAccess"
* "deviceEncryptionManagement"
* "deviceLockManagement"
* "deviceManagementAdministrator"
* "deviceManagementDeclaredConfiguration"
* "deviceManagementDeviceLockPolicies"
* "deviceManagementDmAccount"
* "deviceManagementEmailAccount"
* "deviceManagementFoundation"
* "deviceManagementRegistration"
* "deviceManagementWapSecurityPolicies"
* "devicePortalProvider"
* "deviceUnlock"