param([string]$IndexPath = "C:\own\composer\suno-index.json", [string]$EnvPath = "C:\own\composer\.env")
$ErrorActionPreference = "Stop"

$idx = Get-Content $IndexPath | ConvertFrom-Json
$defaultClips = $idx.clips | Where-Object { -not $_.project_id -or $_.project_id -eq "" -or $_.project_id -eq "default" }
Write-Host "Checking $($defaultClips.Count) clips in default for empty lyrics..."

$raw = Get-Content $EnvPath | Where-Object {$_ -match 'SUNO_COOKIE'} | ForEach-Object {$_ -replace 'SUNO_COOKIE=', '' -replace '"', ''} | Select-Object -First 1
$h = @{"Cookie" = $raw;"Authorization" = ($raw -split ';' | Where-Object {$_ -match '__client'} | ForEach-Object {($_ -split '=', 2)[1].Trim()});"Content-Type"="application/json"}
$r = Invoke-WebRequest -Uri "https://auth.suno.com/v1/client?__clerk_api_version=2021-02-05&_clerk_js_version=5.56.0" -Method Get -Headers $h -SkipCertificateCheck -ErrorAction Stop
$d = $r.Content | ConvertFrom-Json
$sid = if ($d.response.last_active_session_id) { $d.response.last_active_session_id } else { ($d.response.sessions | Where-Object status -eq 'active' | Select-Object -First 1).id }
$r2 = Invoke-WebRequest -Uri "https://auth.suno.com/v1/client/sessions/$sid/tokens?__clerk_api_version=2021-02-05&_clerk_js_version=5.56.0" -Method Post -Headers $h -SkipCertificateCheck -ErrorAction Stop
$freshJwt = ($r2.Content | ConvertFrom-Json).jwt

$A = @{"Cookie"=$raw;"Authorization"="Bearer $freshJwt"}

$instrumentals = [System.Collections.Concurrent.ConcurrentBag[string]]::new()
$processed = 0
$total = $defaultClips.Count
$sw = [System.Diagnostics.Stopwatch]::StartNew()

$defaultClips.id | ForEach-Object -Parallel {
    $id = $_
    $headers = $using:A
    $bag = $using:instrumentals
    try {
        $r = Invoke-WebRequest -Uri "https://studio-api.prod.suno.com/api/clip/$id" -Method Get -Headers $headers -SkipCertificateCheck -ErrorAction Stop -TimeoutSec 10
        $clip = $r.Content | ConvertFrom-Json
        $prompt = if ($clip.metadata.prompt) { $clip.metadata.prompt.Trim() } else { "" }
        if ([string]::IsNullOrEmpty($prompt)) {
            $bag.Add($clip.id)
        }
        Write-Host "."
        $null = [System.Threading.Interlocked]::Increment([ref]$using:processed)
    } catch {
        Write-Host "x"
    }
} -ThrottleLimit 20

$sw.Stop()
Write-Host "`nDone in $($sw.Elapsed.TotalSeconds.ToString('F1'))s"
Write-Host "Checked $processed/$total clips"
$result = $instrumentals.ToArray()
Write-Host "Found $($result.Count) instrumentals (empty lyrics)"
$result | ForEach-Object { Write-Host $_ }
$result | ConvertTo-Json -Compress | Set-Content -Path "instrumental-ids.txt"
Write-Host "Saved to instrumental-ids.txt"
