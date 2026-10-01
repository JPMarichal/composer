---
name: catalog-genre-analyzer
description: >
  Analiza el catálogo de canciones del proyecto (canciones/) para calcular
  distribución por género, detectar tendencias y mantener el índice
  (indice-por-genero.md) actualizado. Activar cuando se añadan canciones
  nuevas, se pida análisis de género, estadísticas del catálogo, o cuando
  se quiera recalcular los porcentajes de la regla 21 del AGENTS.md.
---

## Qué hace

- Escanea todos los archivos `.md` en `canciones/`
- Extrae el campo `Género` de los metadatos de cada canción
- Clasifica por género primario y co-géneros
- Calcula distribución porcentual
- Detecta cambios significativos vs el índice existente
- Sugiere actualización de `canciones/indice-por-genero.md` y `AGENTS.md §21`

## Cómo usarlo

Cuando el usuario pida análisis de catálogo, porcentajes, o después de añadir canciones nuevas:

1. Leer `canciones/indice-por-genero.md` para la línea base
2. Escanear todos los `canciones/*.md` y extraer metadatos de género de cada uno
3. Calcular: total por género, porcentajes, detección de nuevos géneros
4. Comparar con el índice existente y reportar diferencias
5. Si hay cambios significativos (>5% de diferencia en algún género, o nuevos géneros), proponer actualización del índice y de AGENTS.md §21

## Formato de extracción de metadatos

Buscar en cada archivo el patrón:

```markdown
- **Género:** <género primario>
```

Y opcionalmente co-géneros en la categorización del índice (si la canción aparece bajo más de un género).

## Clasificación

| Categoría | Géneros incluidos |
|-----------|------------------|
| Pop | Pop, Synth-pop, Alt-pop, Chamber pop, Pop rock, Indie-pop, Pop progresivo, Orchestral pop, Spanish indie pop, Baroque pop, Power pop |
| Balada | Balada |
| Indie/Folk | Indie, Folk, Indie-pop (cuando Folk es co-género) |
| Electrónica | Electrónica, Synth-pop (cuando el primario no es Pop) |
| Rock | Rock, Pop rock (cuando primario), Art rock |
| Otros | Adoración, Soul/R&B, Jazz, Clásica, Spoken word, Cumbia, Vallenato |

## Salida de ejemplo

```
=== Distribución por género ===
Pop:            18 canciones (33%)
Balada:         10 canciones (19%)
Indie/Folk:     11 canciones (20%)
Synth-pop:      4 canciones (7%)
Chamber pop:    3 canciones (6%)
...otros:       8 canciones (15%)
---
Total letra:    54 canciones
Rare Metals:    24 instrumentales
===============================
```

## Notas

- Rare Metals y otras instrumentales se contabilizan aparte
- El índice `indice-por-genero.md` es la fuente de verdad; si no hay metadatos de género en un archivo, usar la clasificación del índice
- Al detectar un desvío >5% respecto a AGENTS.md §21, notificar al usuario
