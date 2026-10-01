param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Arguments
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$justPath = 'C:\git\_gitDocs\.agent\bin\just.exe'

if (!(Test-Path -LiteralPath $justPath)) {
    throw "No se encontró just.exe en $justPath"
}

& $justPath @Arguments
$exitCode = $LASTEXITCODE
if ($null -ne $exitCode) {
    exit $exitCode
}