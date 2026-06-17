param(
    [Parameter(Mandatory = $true)]
    [string]$Title,

    [string]$OutputPath = ""
)

$slug = $Title.ToLowerInvariant()
$slug = $slug -replace "[^a-z0-9áéíóúñü\s-]", ""
$slug = $slug -replace "\s+", "-"
$slug = $slug -replace "-+", "-"

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $OutputPath = Join-Path "canciones\pitches" ("pitch-editorial-" + $slug + ".md")
}

$directory = Split-Path -Parent $OutputPath
if (-not [string]::IsNullOrWhiteSpace($directory) -and -not (Test-Path $directory)) {
    New-Item -ItemType Directory -Path $directory -Force | Out-Null
}

$content = @"
# Pitch Editorial Spotify — $Title

## Naturaleza del pitch

Este texto está pensado para **revisión editorial interna en Spotify for Artists**.
No es visible para el público como descripción de lanzamiento, bio o copy promocional.
Debe escribirse para ayudar al editor a clasificar el track con rapidez, no para venderlo al oyente final.

## Datos base

- **Título:** $Title
- **Género principal:**
- **Subgénero:**
- **Mood principal:**
- **Mood secundario:**
- **BPM / energía:**
- **Instrumentos distintivos:**
- **Idioma:**
- **Contexto cultural o geográfico:**

## Historia y emoción

- **Detonante de la canción:**
- **Escena de escucha:**
- **Emoción concreta:**
- **Tesis en una frase:**

## Encaje editorial

- **Momento de escucha:**
- **Audiencia probable:**
- **Lane editorial plausible:**
- **1-2 referencias de fit realista:**

## Soporte real del lanzamiento

- **Video / visualizer / live session:**
- **Clips / creators / redes:**
- **Pre-save:**
- **Prensa / premieres:**
- **Shows / activación local:**
- **Tracción previa relevante:**

## Sugerencias de llenado en Spotify for Artists

### Géneros

- **Hasta 3 géneros sugeridos:**
- **Motivo breve de la selección:**

### Estilos de la canción

- **Hasta 2 estilos sugeridos:**
- **Motivo breve de la selección:**

### Culturas musicales

- **Hasta 2 culturas sugeridas:**
- **Motivo breve de la selección:**

### Estados de ánimo

- **Hasta 2 estados de ánimo sugeridos:**
- **Motivo breve de la selección:**

### Instrumentos

- **Instrumentos sugeridos del selector:**
- **Instrumentos importantes que no aparecen en el selector:**

### Flags del formulario

- **¿Es un cover?:** No
- **¿Es un remix?:** No
- **¿Cómo se grabó?:** Estudio
- **¿Es una canción instrumental?:** No
- **Notas para decidir rápido:**

## Borrador maestro

> $Title es un/a [SUBGENERO] con [ELEMENTOS SONOROS CLAVE]. Nace de [HISTORIA / IMAGEN / DETONANTE] y trabaja [EMOCION / TENSION / MOMENTO]. Encaja en [MOMENTO DE ESCUCHA / LANE EDITORIAL / AUDIENCIA]. El lanzamiento contará con [SOPORTE REAL].

## Variaciones iniciales

### Variación 1 — Sonido primero

> 

### Variación 2 — Historia primero

> 

### Variación 3 — Fit primero

> 

## Versión final recomendada

> 

## Checklist

### Contenido

- [ ] Dice qué suena de forma concreta
- [ ] Incluye historia o imagen útil
- [ ] Explica el fit editorial o momento de escucha
- [ ] Menciona soporte real del release
- [ ] El documento incluye 3 variaciones útiles
- [ ] El documento incluye sugerencias concretas para llenar el formulario
- [ ] Todo cabe en un párrafo corto

### Tono

- [ ] No suena a bio
- [ ] No suena a carta formal
- [ ] No mendiga placement
- [ ] No usa hype vacío
- [ ] No exagera cifras ni logros

### Coherencia

- [ ] Coincide con los metadatos del formulario
- [ ] Las sugerencias de géneros, estilos, moods e instrumentos son defendibles
- [ ] El lane sugerido es realista
- [ ] El soporte citado existe o está confirmado
- [ ] El perfil de artista está actualizado
"@

Set-Content -LiteralPath $OutputPath -Value $content -Encoding UTF8
Write-Host "Plantilla creada: $OutputPath"