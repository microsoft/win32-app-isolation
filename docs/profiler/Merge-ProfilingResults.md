---
external help file: Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.dll-Help.xml
Locale: en-US
Module Name: Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler
ms.date: 05/16/2023
online version:
schema: 2.0.0
title: Merge-ProfilingResults
---

# Merge-ProfilingResults

## SYNOPSIS
Merges multiple Get-ProfilingResults output files into a single output file.

## SYNTAX

### XML Set

```
Merge-ProfilingResults [-XmlInput] <string[]> [-OutputPath <string>] [-PackageNames <string[]>] [-Quiet]
[-ShowFirstParty] [-ShowNoNameObjectFailures] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CSV Set

```
Merge-ProfilingResults [-CsvInput] <string[]> [-OutputPath <string>] [-PackageNames <string[]>] [-Quiet]
[-ShowFirstParty] [-ShowNoNameObjectFailures] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## DESCRIPTION

The Merge-ProfilingResults cmdlet is used to merge multiple Get-ProfilingResults output files into a single output file.

## EXAMPLES

### Example 1: Merge multiple AppXManifest results into one.

```powershell
Merge-ProfilingResults -XmlInput "C:\Path\To\AppXManifest1.xml", "C:\Path\To\AppXManifest2.xml" -OutputPath "C:\Path\To\MergedAppXManifest.xml"
```

### Example 2: Merge multiple AccessAttemptRecords.csv results into one.

```powershell
Merge-ProfilingResults -CsvInput "C:\Path\To\AccessAttemptRecords1.csv", "C:\Path\To\AccessAttemptRecords2.csv" -OutputPath "C:\Path\To\MergedAccessAttemptRecords.csv" 
```

## PARAMETERS

### -XmlInput

Specifies an array of paths to XML application package manifests to be merged.


```yaml
Type: System.String[]
Parameter Sets: XML
Aliases: c, Capabilities

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CsvInput

Specifies an array of paths to CSV access attempt records to be merged.


```yaml
Type: System.String[]
Parameter Sets: CSV
Aliases: r, Records

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```t wildcard characters: False
```

### -OutputPath

Specifies the path to the output file where the merged output will be saved.


```yaml
Type: System.String
Parameter Sets: (All)
Aliases: o, Output

Required: False
Position: Named
Default value: <working directory>\merged\AppXManifest-Capabilities.xml (XML) or <working directory>\merged\AccessAttemptRecords.csv (CSV)
Accept pipeline input: False
Accept wildcard characters: False
```

### -PackageNames

Specifies an array of package names to filter the merging. Only information related to the specified packages will be merged into the output file.

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases: p, Packages

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ShowFirstParty

Indicates whether to include first-party capabilities in the output. These may only be declared by Microsoft-signed packages.

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

### -ShowNoNameObjectFailures

Indicates whether to output summary information for access attempts to unidentified objects.

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

[ApplicationCapabilityProfiler](application-capability-profiler.md)

[Get-ProfilingResults](Get-ProfilingResults.md)

[Start-Profiling](Start-Profiling.md)

[Stop-Profiling](Stop-Profiling.md)