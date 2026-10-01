param(
    [Parameter(Position = 0)]
    [ValidateSet('activate', 'deactivate', 'status')]
    [string]$Action = 'status',

    [string]$ProjectConfig = (Join-Path $PSScriptRoot '..\opencode.json'),
    [string]$UserConfig = (Join-Path $env:APPDATA 'Code\User\mcpServers.json'),
    [string]$StateFile = (Join-Path $PSScriptRoot '..\.opencode\project-mcp-state.json')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Read-JsonFile {
    param([string]$Path)

    if (!(Test-Path -LiteralPath $Path)) {
        throw "No existe el archivo JSON: $Path"
    }

    $raw = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ([string]::IsNullOrWhiteSpace($raw)) {
        throw "El archivo JSON está vacío: $Path"
    }

    return $raw | ConvertFrom-Json -Depth 100
}

function Write-JsonFile {
    param(
        [string]$Path,
        [Parameter(ValueFromPipeline = $true)]
        $Data
    )

    $directory = Split-Path -Parent $Path
    if ($directory -and !(Test-Path -LiteralPath $directory)) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }

    $json = $Data | ConvertTo-Json -Depth 100
    [System.IO.File]::WriteAllText($Path, $json + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))
}

function Convert-ToMcpServerEntry {
    param(
        [string]$ProjectName,
        [string]$ServerName,
        $Definition
    )

    if ($null -eq $Definition.command) {
        throw "El servidor '$ServerName' no define 'command'."
    }

    $entry = [ordered]@{}
    $commandValue = $Definition.command
    $args = @()

    if ($commandValue -is [System.Array]) {
        if ($commandValue.Count -eq 0) {
            throw "El servidor '$ServerName' tiene 'command' vacío."
        }

        $entry.command = [string]$commandValue[0]
        if ($commandValue.Count -gt 1) {
            $args = @($commandValue[1..($commandValue.Count - 1)] | ForEach-Object { [string]$_ })
        }
    }
    else {
        $entry.command = [string]$commandValue
        if ($Definition.PSObject.Properties.Name -contains 'args') {
            $args = @($Definition.args | ForEach-Object { [string]$_ })
        }
    }

    if ($args.Count -gt 0) {
        $entry.args = $args
    }

    if ($Definition.PSObject.Properties.Name -contains 'environment' -and $null -ne $Definition.environment) {
        $envMap = [ordered]@{}
        foreach ($property in $Definition.environment.PSObject.Properties) {
            $envMap[$property.Name] = [string]$property.Value
        }
        $entry.env = $envMap
    }

    if ($Definition.PSObject.Properties.Name -contains 'enabled' -and -not [bool]$Definition.enabled) {
        $entry.disabled = $true
    }

    if ($Definition.PSObject.Properties.Name -contains 'type' -and $Definition.type -and $Definition.type -ne 'local') {
        $entry.type = [string]$Definition.type
    }

    return @{
        Name = "$ProjectName--$ServerName"
        Entry = $entry
    }
}

function Get-ProjectMcpEntries {
    param([string]$ConfigPath)

    $projectConfig = Read-JsonFile -Path $ConfigPath
    if ($null -eq $projectConfig.mcp) {
        throw "El archivo no contiene el bloque 'mcp': $ConfigPath"
    }

    $projectName = Split-Path -LeafBase (Resolve-Path -LiteralPath (Split-Path -Parent $ConfigPath))
    $entries = @()

    foreach ($property in $projectConfig.mcp.PSObject.Properties) {
        $entries += Convert-ToMcpServerEntry -ProjectName $projectName -ServerName $property.Name -Definition $property.Value
    }

    return $entries
}

function Get-UserConfig {
    param([string]$ConfigPath)

    if (Test-Path -LiteralPath $ConfigPath) {
        $config = Read-JsonFile -Path $ConfigPath
        if ($null -eq $config.mcpServers) {
            $config | Add-Member -MemberType NoteProperty -Name mcpServers -Value ([pscustomobject]@{})
        }
        return $config
    }

    return [pscustomobject]@{
        mcpServers = [pscustomobject]@{}
    }
}

function Save-State {
    param(
        [string]$Path,
        [string]$ProjectConfigPath,
        [string]$UserConfigPath,
        [string[]]$ServerNames
    )

    [ordered]@{
        projectConfig = (Resolve-Path -LiteralPath $ProjectConfigPath).Path
        userConfig = $UserConfigPath
        serverNames = $ServerNames
        updatedAt = (Get-Date).ToString('o')
    } | Write-JsonFile -Path $Path
}

function Remove-ManagedServers {
    param(
        $Config,
        [string[]]$ServerNames
    )

    foreach ($name in $ServerNames) {
        if ($Config.mcpServers.PSObject.Properties.Name -contains $name) {
            $Config.mcpServers.PSObject.Properties.Remove($name)
        }
    }
}

$projectEntries = Get-ProjectMcpEntries -ConfigPath $ProjectConfig
$userConfigObject = Get-UserConfig -ConfigPath $UserConfig
$managedNames = @($projectEntries | ForEach-Object { $_.Name })

switch ($Action) {
    'activate' {
        Remove-ManagedServers -Config $userConfigObject -ServerNames $managedNames

        foreach ($projectEntry in $projectEntries) {
            $userConfigObject.mcpServers | Add-Member -MemberType NoteProperty -Name $projectEntry.Name -Value ([pscustomobject]$projectEntry.Entry)
        }

        $userConfigObject | Write-JsonFile -Path $UserConfig
        Save-State -Path $StateFile -ProjectConfigPath $ProjectConfig -UserConfigPath $UserConfig -ServerNames $managedNames

        Write-Host "Activados $($managedNames.Count) MCP del proyecto en $UserConfig"
        $managedNames | ForEach-Object { Write-Host "  + $_" }
    }

    'deactivate' {
        $stateNames = $managedNames
        if (Test-Path -LiteralPath $StateFile) {
            $state = Read-JsonFile -Path $StateFile
            if ($state.PSObject.Properties.Name -contains 'serverNames' -and $state.serverNames) {
                $stateNames = @($state.serverNames | ForEach-Object { [string]$_ })
            }
        }

        Remove-ManagedServers -Config $userConfigObject -ServerNames $stateNames
        $userConfigObject | Write-JsonFile -Path $UserConfig

        if (Test-Path -LiteralPath $StateFile) {
            Remove-Item -LiteralPath $StateFile -Force
        }

        Write-Host "Desactivados $($stateNames.Count) MCP del proyecto en $UserConfig"
        $stateNames | ForEach-Object { Write-Host "  - $_" }
    }

    'status' {
        $present = @($managedNames | Where-Object { $userConfigObject.mcpServers.PSObject.Properties.Name -contains $_ })
        $missing = @($managedNames | Where-Object { $userConfigObject.mcpServers.PSObject.Properties.Name -notcontains $_ })

        Write-Host "Proyecto: $(Split-Path -LeafBase (Resolve-Path -LiteralPath (Split-Path -Parent $ProjectConfig)))"
        Write-Host "Config proyecto: $ProjectConfig"
        Write-Host "Config activa:   $UserConfig"
        Write-Host "Esperados:       $($managedNames.Count)"
        Write-Host "Activos:         $($present.Count)"

        if ($present.Count -gt 0) {
            Write-Host 'Presentes:'
            $present | ForEach-Object { Write-Host "  = $_" }
        }

        if ($missing.Count -gt 0) {
            Write-Host 'Faltantes:'
            $missing | ForEach-Object { Write-Host "  ! $_" }
        }
    }
}