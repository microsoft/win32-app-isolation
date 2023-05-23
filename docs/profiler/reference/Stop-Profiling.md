Module Name: [Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler](Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

# Stop-Profiling

## SYNOPSIS
Stops access attempt profiling for a specified application package.

## SYNTAX

```
Stop-Profiling [[-TracePath] <string>] [-PackageFullName <string>] [-ManifestPath <string>] [-Quiet] [-WhatIf]
[-Confirm] [<CommonParameters>]


```

## DESCRIPTION

The Stop-Profiling cmdlet is used to stop access attempt profiling for a specified application package. The cmdlet stops an active trace logging session started via [Start-Profiling](Start-Profiling.md), collects the resulting Event Trace Log (ETL) file and takes away access attempt trace logging instrumentation from all currently instrumented packages. **Note** that Stop-Profiling requires administrator privileges and that Developer Mode be enabled.

## EXAMPLES

### Example 1: Stop profiling and save results to the default trace path.

```powershell
Stop-Profiling
```

### Example 2: Stop profiling and save results to a specific trace path.

```powershell
Stop-Profiling -TracePath "C:\Path\To\Trace.etl"
```

## PARAMETERS

### -TracePath

Specifies the path to which save the collected Event Trace Log.

```yaml
Type: System.String
Parameter Sets: (All)
Aliases: t, Trace

Required: False
Position: Named
Default value: <working directory>\trace.etl
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManifestPath

Specifies the path to the manifest file of the application package from which to take away access attempt logging instrumentation. Supersedes -PackageFullName. Avoid using unless individual packages must have instrumentation taken away.

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

Superseded by -ManifestPath. Specifies the full name of the application package from which to take away access attempt logging instrumentation.
Avoid using unless individual packages must have instrumentation taken away.
This can be obtained via [Get-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps).
See [ApplicationCapabilityProfiler](../application-capability-profiler.md) for details.

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

[Application capability profiler](../application-capability-profiler.md)

[Start-Profiling](Start-Profiling.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Merge-ProfilingResults](Merge-ProfilingResults.md)

[Get-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps)