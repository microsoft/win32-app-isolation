---
external help file: Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.dll-Help.xml
Locale: en-US
Module Name: Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler
ms.date: 05/16/2023
online version:
schema: 2.0.0
title: Start-Profiling
---

# Start-Profiling

## SYNOPSIS
Initiates access attempt profiling for a specified application package.

## SYNTAX

```
Start-Profiling [[-ManifestPath] <string>] [-PackageFullName <string>] [-SignedFilePath <string>] [-Quiet]
[-Force] [-WhatIf] [-Confirm] [<CommonParameters>]

```

## DESCRIPTION

The Start-Profiling cmdlet is used to start access attempt profiling for an application package. The cmdlet both starts an access attempt trace logging session and instruments the application package so it’s able to log to the session.

## EXAMPLES

### Example 1: Start profiling for application package specified by manifest.

```powershell
Start-Profiling -ManifestPath C:\Path\To\MyAppXManifest.xml
```

### Example 2: Start profiling for application package specified by package full name.

```powershell
Start-Profiling -PackageFullName "Contoso.Application_1.0.0.0_neutral__8wekyb3d8bbwe"
```

## PARAMETERS

### -ManifestPath

Specifies the path to the manifest file of the application package to be profiled. The package full name will be inferred from the manifest. Supersedes -PackageFullName.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: m, Manifest

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageFullName 

Superseded by -ManifestPath. Specifies the full name of the application package to be profiled. This can be obtained via [Get-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps). See [ApplicationCapabilityProfiler](application-capability-profiler.md) for details.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: p, PackageName

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SignedFilePath

[Optional] Specifies the path to the authenticode sign file for application packages that are authenticode signed.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Quiet

Indicates that the cmdlet runs in quiet mode, suppressing unnecessary output and prompts.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force

Forces the cmdlet to proceed with profiling without displaying any confirmation prompts. Use this parameter with caution.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf

Shows what would happen if the cmdlet runs. The cmdlet is not executed.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm

Prompts you for confirmation before running the cmdlet.

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

## RELATED LINKS

[ApplicationCapabilityProfiler](application-capability-profiler.md)

[Stop-Profiling](Stop-Profiling.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Merge-ProfilingResults](Merge-ProfilingResults.md)

[Get-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps)