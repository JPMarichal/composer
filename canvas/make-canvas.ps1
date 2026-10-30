param(
    [Parameter(Mandatory)][string]$Clip,
    [string]$OutDir = "$PSScriptRoot\out",
    [int]$Height = 1920,
    [int]$Fps = 24
)
# Convierte un clip generado en un Canvas de Spotify: 9:16, H.264, sin audio, loop de rebote.
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $OutDir | Out-Null
$w = [int]($Height * 9 / 16)

foreach ($frames in 191) {
    $out = Join-Path $OutDir ("canvas_{0}f.mp4" -f $frames)
    # rebote: adelante + reversa, recortado al número exacto de frames
    $vf = "[0:v]scale=${w}:${Height}:force_original_aspect_ratio=increase,crop=${w}:${Height},fps=$Fps,split[a][b];" +
          "[b]reverse[r];[a][r]concat=n=2:v=1:a=0,trim=end_frame=$frames,setpts=PTS-STARTPTS,format=yuv420p[v]"
    ffmpeg -y -v error -i $Clip -filter_complex $vf -map '[v]' -an -c:v libx264 -profile:v high `
        -crf 20 -maxrate 4M -bufsize 8M -movflags +faststart $out
    $info = ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name,nb_frames,r_frame_rate:format=duration,size `
        -of default=nw=1 $out
    $audio = ffprobe -v error -select_streams a -show_entries stream=codec_name -of csv=p=0 $out
    Write-Host "== $out"; $info; Write-Host ("audio streams: " + $(if ($audio) { $audio } else { 'ninguno' }))
}
