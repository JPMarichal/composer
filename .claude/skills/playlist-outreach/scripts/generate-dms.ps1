param(
    [string]$CsvPath = "C:\own\composer\contacts\playlist-artists.csv",
    [string]$OutputDir = "C:\own\composer\contacts\outreach"
)

$csv = Import-Csv $CsvPath -Encoding UTF8

$artists = $csv | Group-Object Artist | ForEach-Object {
    $first = $_.Group[0]
    $ig = if ($first.IG) { $first.IG } else { "" }
    $igClean = $ig -replace '@', ''
$playlists = @($_.Group | Group-Object Playlist_ID | ForEach-Object {
    $g = $_.Group[0]
    @{Name = $g.Playlist_Name; URL = $g.Playlist_URL; Track = $g.Track}
})
[PSCustomObject]@{
    Artist      = $first.Artist
    IG          = $ig
    IGHandle    = $igClean
    Tier        = $first.Tier
    Playlists   = $playlists
    PlaylistCnt = $playlists.Count
    Status      = $first.Status
}
}

$pending = $artists | Where-Object { $_.Status -eq "pending" }

$dms = @()
foreach ($a in $pending) {
    $handle = if ($a.IGHandle) { "@$($a.IGHandle)" } else { $a.Artist }
    if ($a.PlaylistCnt -eq 1) {
        $p = $a.Playlists[0]
        $dmText = @"
Hola $handle, soy curador de "$($p.Name)" en Spotify.
Acabo de incluir "$($p.Track)" porque encaja perfecto con el mood de la playlist.
Si te gusta el proyecto, agradecería un share en stories. ¡Un abrazo!

🎵 $($p.URL)
"@
    }
    else {
        $items = $a.Playlists | ForEach-Object { "- `"$($_.Track)`" en `"$($_.Name)`"" }
        $urls = $a.Playlists | ForEach-Object { "🎵 $($_.URL)" }
        $dmText = @"
Hola $handle, soy curador de dos playlists en Spotify que incluyen tu música.
$($items -join "`n")
Si te gusta el proyecto, agradecería un share en stories. ¡Un abrazo!

$($urls -join "`n")
"@
    }
    $dms += $dmText
}

$outputLines = @()
for ($i = 0; $i -lt $dms.Count; $i++) {
    $outputLines += $dms[$i]
    if ($i -lt $dms.Count - 1) {
        $outputLines += ""
        $outputLines += "---"
        $outputLines += ""
    }
}

$utf8Bom = [byte[]]@(0xEF, 0xBB, 0xBF)
$enc = [System.Text.UTF8Encoding]::new($false)
$outputFile = Join-Path $OutputDir "dms-pl1-pl2.md"
$fs = [System.IO.File]::Create($outputFile)
$fs.Write($utf8Bom, 0, 3)
($outputLines -join "`r`n") | ForEach-Object { $b = $enc.GetBytes($_ + "`r`n"); $fs.Write($b, 0, $b.Length) }
$fs.Close()

Write-Output "OUTREACH_FILE=$outputFile"
Write-Output "DMS_GENERATED=$($dms.Count)"
