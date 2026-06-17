---
name: spotify-editorial-pitch
description: Redacta, mejora y audita pitches editoriales para Spotify for Artists. Activar cuando el usuario pida escribir un pitch editorial, optimizar un pitch de Spotify, preparar una submission editorial, revisar el texto del pitch, crear variantes, o validar si un pitch cumple buenas prácticas. Incluye plantilla maestra, checklist y workflow de validación.
---

# Spotify Editorial Pitch

Skill especializado para redactar y revisar pitches editoriales de Spotify con criterio práctico y tono profesional.

## Objetivo

Convertir información dispersa de un lanzamiento en un pitch editorial breve, concreto y útil para el editor de Spotify.

## Referencias obligatorias

Leer antes de redactar o auditar:

- `docs/003-pitch-editorial-spotify.md`
- `docs/spotify-editorial-pitch-template.md`

Si el usuario quiere un scaffold editable, usar:

```bash
just spotify-pitch-template "Titulo de la canción"
```

## Regla central

El pitch **no** es una bio ni una súplica. Debe responder, con velocidad:

1. Qué suena
2. Qué emoción o historia captura
3. Dónde encaja
4. Qué respaldo real tendrá el lanzamiento

## Workflow

### 1. Reunir insumos mínimos

Antes de redactar, obtener o inferir:

- Título
- Género y subgénero
- Mood
- Instrumentos distintivos
- Idioma
- Contexto cultural/geográfico
- Historia o detonante de la canción
- Momento de escucha o lane editorial plausible
- Plan real de lanzamiento
- Tracción previa si existe
- Traducción práctica de esos insumos al formulario de Spotify for Artists

### 2. Reducir a cuatro bloques

Transformar todo el material a estos cuatro bloques:

- **Sonido**
- **Historia / emoción**
- **Fit editorial**
- **Soporte real**

### 3. Redactar en formato corto

Preferir:

- 1 párrafo
- 3 o 4 frases
- lenguaje concreto
- tono factual y vivo

### 4. Generar variaciones en la primera pasada

El primer documento de trabajo debe incluir siempre:

- **Borrador maestro**
- **Variación 1 — sonido primero**
- **Variación 2 — historia primero**
- **Variación 3 — fit primero**
- **Versión final elegida**

La salida por defecto no es una sola redacción aislada. Es un documento comparativo corto que permite elegir el mejor ángulo antes de enviar.

Salvo excepción clara, la **versión final recomendada** debe derivar de la variación **sonido primero**, porque es la que mejor ayuda al editor a clasificar el track rápido.

### 5. Añadir sugerencias de llenado del formulario

El mismo documento debe incluir una sección de **Sugerencias de llenado en Spotify for Artists** con:

- hasta 3 géneros sugeridos
- hasta 2 estilos
- hasta 2 culturas musicales
- hasta 2 estados de ánimo
- instrumentos del selector
- cover / remix / estudio o en vivo / instrumental

La meta es que el documento sirva tanto para redactar el pitch como para completar la pantalla de datos sin reinterpretar el análisis.

### 6. Auditar contra checklist

No entregar el pitch sin revisar lo siguiente.

## Checklist

### Contenido

- [ ] Explica el sonido con palabras concretas
- [ ] Incluye una historia, imagen o emoción específica
- [ ] Muestra un encaje editorial o momento de escucha realista
- [ ] Menciona soporte real del lanzamiento
- [ ] Incluye 3 variaciones iniciales en el mismo documento
- [ ] Incluye sugerencias concretas para llenar el formulario

### Tono

- [ ] No es una bio del artista
- [ ] No es una carta formal
- [ ] No mendiga placement
- [ ] No usa hype vacío
- [ ] No llama al tema “hit”, “best song”, “genre-defying” o equivalentes

### Coherencia

- [ ] El texto coincide con género, mood e instrumentación del formulario
- [ ] Las sugerencias del formulario son defendibles con el audio y la ficha
- [ ] El fit mencionado no contradice el audio
- [ ] La tracción citada es real
- [ ] El soporte citado está confirmado

## Anti-patrones

- Escribir más sobre el artista que sobre la canción
- Nombrar muchas playlists por follower count
- Inflar números
- Dejar fuera el contexto del lanzamiento
- Usar descriptores vagos como “una vibra increíble”
- Copiar tono de nota de prensa

## Entregables posibles

Según lo que pida el usuario, entregar uno de estos:

1. **Documento completo de pitch** con sugerencias de llenado, borrador, 3 variaciones y versión final recomendada
2. **Auditoría** de un pitch existente
3. **Borrador rellenable** usando la plantilla maestra

## Formato recomendado de salida

### Si redactas desde cero

- `Sugerencias de llenado:`
- `Variaciones iniciales:`
- `Pitch final recomendado:`
- `Por qué funciona:` una explicación corta

### Si auditas uno existente

- `Veredicto:` fuerte / aceptable / débil
- `Problemas:` lista corta
- `Versión corregida:`

## Nota práctica

Si falta información importante, pedir solo lo mínimo que desbloquee el pitch:

- historia o imagen del tema
- fit editorial / momento de escucha
- soporte real del lanzamiento

Sin esos tres elementos, el pitch tiende a quedar genérico.