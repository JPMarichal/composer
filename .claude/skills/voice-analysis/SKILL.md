---
name: voice-analysis
description: >
  Análisis exhaustivo de la voz de cantantes/artístas para generación en Suno o estudio
  de características vocales. Genera songcases en voces/ usando el template 013.
---

# Voice Analysis Skill

## Cuándo activarlo

Cuando el usuario pida:
- "Analiza la voz de X"
- "Quiero estudiar el timbre de X"
- "Haz un análisis vocal de X"
- "Genera voice emulation para X"
- Cualquier request de análisis de **voz humana** (no canción)

NOTA: Este skill es PARA ANÁLISIS DE VOZ DE PERSONAS REALES. Para canciones existentes, usar songcase-analysis.

## Template base

`specs/013-voice-analysis-template.md` define la estructura obligatoria.

## Workflow

### Paso 1: Identificar información básica
```
1. Nombre del artista
2. Género principal donde se desempeña la voz
3. Tipo de voz (según clasificación: S, MS, A, C, T, BT, B)
4. Rango vocal estimado (E2-G6, etc.)
```

### Paso 2: Recopilar características vocales
```
1. Timbre y calidad (usar adjetivos técnicos: brillante, oscuro, nasal, etc.)
2. Rango y tessitura
3. Técnicas características (falsete, belting, vibrato)
4. Patrones de fraseo
5. Emociones dominantes (escala 1-5)
```

### Paso 3: Investigar géneros y contexto
```
1. Géneros donde brilla naturalmente
2. Instrumentación típica que acompaña su voz
3. Progresiones armónicas efectivas
4. Parámetros técnicos sugeridos (tempo, tonalidad)
```

### Paso 4: Generar prompt de emulación
Usar la fórmula de 6 componentes (specs/003):
1. Género + Era
2. Tempo/BPM
3. Instrumentación y riffs
4. Tratamiento vocal (personaje)
5. Ambiente y tonalidad
6. Mezcla

Máximo 1000 caracteres.

### Paso 5: Escribir canción propuesta
```
1. Usar template 013-sección 5.2
2. Letra en español con meta-tags [Verse], [Chorus], etc.
3. Aplicar checklist anti-AI de specs/002
4. Verificar sintaxis Suno (specs/004)
```

### Paso 6: Guardar en directorio correcto
```
1. Crear directorio: voces/ (si no existe)
2. Nombre del archivo según justfile voice-analysis:
   <PREFIX>_<RANGE>_<ARTIST>.md
   
   PREFIX = {F|F#|M|M#|A|A#|C|C#|T|T#|B|B#} + {S= Soprano, MS=Mezzo-soprano, A=Alto/Contralto, T=Tenor, BT=Barítono, B=Bajo}
   RANGE = rango vocal (ej: C3-C5)
   ARTIST = nombre artístico en MAYÚSCULAS sin vocales ni espacios (ej: JLP|MaríaB, JULIETAV)

   Ejemplos:
   - F_E3-C6_JLP → F (Fem), E3-C6, JLP (Juan Pablo Marichal)
   - MS_C3-C5_JULIETAV → Mezzo-soprano, rango medio, Julieta Venegas
```

### Paso 7: Indexar (opcional)
```bash
just ingest
```

Esto incluye `voces/` en el RAG.

## Formato del archivo

Usar template `specs/013-voice-analysis-template.md` con estas secciones obligatorias:

1. **Metadatos** — nombre, fecha, versión
2. **Características vocales básicas** — rango, timbre, técnicas
3. **Patrones del habla y canto** — articulación, entonación
4. **Asociación con géneros** — estilos, estructuras, producción
5. **Cualidades emocionales** — tabla de emociones 1-5
6. **Directrices técnicas para generación** — prompt, letra, variaciones, parámetros
7. **Aplicación en flujo de composición** — checklist AGENTS.md
8. **Ejemplos de referencia** — canciones representativas
9. **Historial de revisiones**
10. **Notas adicionales**

## Reglas

1. No adivinar rango vocal exacto — usar estimados basados en discografía o marcar como estimado
2. Letra debe ser original (no copiar letras existentes)
3. Prompt máximo 1000 caracteres (secciones 5.1 y 5.3)
4. Nombre archivo según justfile voice-analysis (líneas 201-212)
5. No usar canciones/ para voces — solo para canciones originales del autor
6. Aplicar anti-AI safeguards a toda letra propuesta

## Directorios

| Tipo | Directorio |
|------|-----------|
| Voz (personas reales) | `voces/` |
| Canción (autoría original) | `canciones/` |
| Canción existente (análisis) | `inspiration/` |

## Comandos útiles

```bash
# Generar análisis
just voice-analysis "MS C3-C5 JLP"

# Indexar voces
just ingest

# Consultar análisis existentes
just query "voces julieta"
```

## Archivos de referencia

- Template: `specs/013-voice-analysis-template.md`
- Sintaxis Suno: `specs/004-suno-syntax.md`
- Anti-AI: `specs/002-anti-ai-isms.md`
- Justfile: `justfile` (líneas 201-212)