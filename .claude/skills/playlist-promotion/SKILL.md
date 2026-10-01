---
name: playlist-promotion
description: >
  Crea y gestiona playlists promocionales en Spotify siguiendo proporciones
  validadas por investigación (OnesToWatch, Chartmetric, PlaylistSupply,
  Orphiq, Hypebot, MusicPulse). Incluye reglas de curaduría, posicionamiento
  por tiers, SEO de títulos y ejecución mecánica via API.
---

# Playlist Promotion

## Cuándo activarlo
- "Crea una playlist para promocionar [canción]"
- "Arma una playlist de 80 canciones para [tema/género]"
- "Planifica la estrategia de playlist para [canción]"

## Fuentes de investigación

| Fuente | Hallazgo |
|--------|----------|
| **OnesToWatch (2026)** | 70/30 rule (70% emergentes <100k, 30% establecidos). 30-sec rule (>40% skip pre-30s penaliza). Refrescar 10-15% semanal |
| **Chartmetric (2025-26)** | Save rate >3.5% = 5x más Discover Weekly. Skip rate vs completación es la métrica #1 |
| **PlaylistSupply (2026)** | Discovered On > follower count. Playlist 5k con alto DO > 500k sin DO |
| **Orphiq** | Max 10-20% canciones propias. Propio nunca en posición #1 |
| **Hypebot/OneSubmit** | Playlists <50 tracks = mejor engagement (adaptado a 80 para promoción). Hook 15s crítico |
| **MusicPulse** | Playlists mood/género específicas > mezclas genéricas |
| **artist.tools** | Cover art consistente con género mejora CTR en feed |

## Reglas de Curaduría

### Tiers
| Tier | ML mensuales | Rol |
|------|-------------|-----|
| Propio (A) | <1k | Ancla temática |
| New Emerging (B) | <10k | Descubrimiento (+37% saves) |
| Rising Indie (C) | 10k-100k | Core del mood |
| Established (D) | 100k-1M | Anclas retención |
| Mainstream (E) | >1M | Ganchos anti-skip |

### Proporción para 80 canciones
| Tier | Cantidad | % | Fuente |
|------|----------|---|--------|
| A Propio | 4 | 5% | Orphiq: max 10-20% |
| B New Emerging | 16 | 20% | OnesToWatch 70/30 rule |
| C Rising Indie | 24 | 30% | 70% emerging = 40% new + 30% rising |
| D Established | 21 | 26% | ~30% established como anchors |
| E Mainstream | 15 | 19% | Ganchos familiares |

### Mapa de posiciones (template efectivo)
| Pos | Qué | Por qué |
|-----|-----|---------|
| 1 | E — hook primeros 15s | 30-sec rule de Spotify |
| 2-4 | Mix D+E | Construcción del mood |
| **5** | **Propio #1** | Oyente ya confía — temprano pero no intrusivo |
| 6-10 | Alternar B/C/E | Profundidad sin perder oyente |
| 11-24 | Mayoría B+C | Descubrimiento profundo |
| **25** | **Propio #2** | Punto medio (spacing ~20) |
| 26-44 | Alternar todos | Variedad |
| **45** | **Propio #3** | Oyente comprometido (spacing ~20) |
| 46-64 | Mix B+C+D | Cierre gradual |
| **65** | **Propio #4** | Último ancla (spacing ~20) |
| 66-80 | Mix D+E | Cierre cómodo y fuerte |

### Reglas absolutas
1. **Propio nunca en #1** (Orphiq)
2. **Espaciar propios**: mínimo 15-20 tracks entre cada uno
3. **Máx 4 propios** (Orphiq: 10-20%) — para 80 tracks, 5%
4. **30-sec rule**: hook primeros 15s en TODOS los tracks
5. **Actualización semanal**: 10-15% del contenido
6. **Save rate >3.5%** = meta real para Discover Weekly
7. **BPM**: ~70% entre 60-90 para baladas
8. **Código moral §7 extendido**: Las pistas deben ser moralmente limpias — sin malas palabras, sin café, sin tabaco, sin drogas, sin alcohol, sin sexo, sin promoción de conductas cuestionables, sin contenido controversial, sin violencia, sin relaciones abusivas.

**Filtro de título automático**: si el título contiene malas palabras, referencias a café, alcohol, drogas, tabaco, sexo o violencia, la pista se descarta sin revisar letra. El título es señal de alerta suficiente.

**Artistas excluidos permanentemente** (sin excepción): Bad Bunny, Enrique Iglesias, J Balvin, y cualquier artista cuyo catálogo principal gire en torno a sexualización o apología de drogas/alcohol.

### SEO de títulos — basado en investigación (no asumir género=primario)

**Regla corregida 2026-06**: la asunción "género va siempre primero" es **incorrecta** según la investigación de Spotify Research. Las queries se distribuyen en **4 dimensiones** y el primary keyword es el de mayor search volume, no el género por defecto.

**4 dimensiones de búsqueda en Spotify:**

| Dimensión | Ejemplos | Cuándo domina |
|---|---|---|
| **Actividad** | workout, study, focus, sleep, driving, commute, running, cooking | Búsquedas funcionales |
| **Mood** | chill, sad, nostalgic, melancholic, energetic, happy, romantic | Búsquedas emocionales |
| **Género/subgénero** | lofi, indie folk, phonk, bedroom pop, balada, pop | Búsquedas de sonido |
| **Era/Contexto** | 2000s, 90s hip hop, throwback, late night, christmas | Búsquedas temporales |

Spotify Research (2021) distingue:
- **Focused queries** (ej. "Bad Bunny un ratito") → unsuitable para long-tail
- **Non-focused / exploratory** (ej. "lofi beats for studying at night") → **aquí viven los long-tail**; suelen empezar por mood o actividad

### Patrón "Research-Once-Use-Many" — 2-3 min por playlist, no 15-20

**Inversión one-time (1-2 horas)**: poblar `kw-pool/` con 30-50 keywords por (género × mercado) + Google Trends data + Spotify Search proxy. Mercados meta: ES, MX, AR. Géneros del catálogo: balada, pop, indie/folk, indie pop, folk latino.

**Per-playlist (2-3 min)**:
1. Listar 5-8 candidatos de `kw-pool/` para el (género × mercado) de esta playlist
2. **30s check en Spotify Autocomplete** manual — escribir el candidato principal y ver si aparece en sugerencias
3. Si hay duda entre 2-3, correr `just kw-spotify "termino" "ES"` para señales de demanda
4. Pick primary (mayor volume / más resultados / más popular en autocomplete)
5. Componer título con estructura `[Primary] : [Secondary mood/activity], [Tema]`
6. Documentar decisión en changelog

**Monthly refresh (15 min)**: re-correr trendspyg en top 20 keywords, detectar rising/falling, update `kw-pool/`.

### Herramientas gratuitas validadas (sin coste)

| Herramienta | Función | Idioma ES | Comando |
|---|---|---|---|
| **Spotify Search API** (nuestra `playlister` app) | `GET /v1/search?type=playlist&q=<term>` — los títulos de las top 10-50 playlists = proxy directo de queries reales | ✅ | `just kw-spotify "termino" "ES"` |
| **trendspyg** (`flack0x/trendspyg`) | Google Trends: interest over time, related queries, trending — RSS-based, sin API key, sin 429, 0.2s | ✅ 125 países | `just kw-trends "termino" "ES"` |
| **trendsmcp MCP** (free tier 100/día) | Alternativa MCP-integrada con Claude/Cursor | ✅ Markets ES/MX/AR | MCP tool |
| ~~pytrends~~ | ❌ Archivado 2023, 429 constantes, requiere proxies | — | NO USAR |
| ~~artist.tools Keyword Explorer~~ | Freemium muy limitado; útil solo con plan de pago | ✅ | No sin Industry Access |

### 6 variantes de título

| Variante | Fórmula | Ejemplo | Cuándo usarla |
|----------|---------|---------|---------------|
| A — Actividad + Género + Mood | `[Actividad] : [Género], [Mood]` | "Estudio: Balada Folk Latino, Nostalgia" | Cuando "estudio/focus" tiene más search que el género |
| B — Mood + Género + Tema | `[Mood] : [Género], [Tema]` | "Nostalgia: Balada Folk Latino, Raíces y Hogar" | Cuando el mood ES el #1 (común en baladas) |
| C — Género + Mood + Tema | `[Género] : [Mood], [Tema]` | "Balada Folk Latino: Nostalgia, Raíces y Hogar" | Default — el género ES el high-volume term |
| D — Género + Actividad | `[Género] : [Actividad]` | "Balada Folk: Para Tu Próximo Logro" | Playlists funcionales |
| E — Género + Era | `[Género] : [Era/Etiqueta]` | "Pop Español: Los 2000 Te Llaman" | Nostálgicas |
| F — Referente | `[Mood/Género] : Si Te Gusta [Artista]` | "Indie Pop: Si Te Gusta Little Jesus" | Promoción al lado de referentes |

- **Probar siempre**: si alguien lee SOLO el título, ¿sabe qué género esperar Y usaría esas palabras para buscar?
- **Validar contra primary keyword del research** (paso 4 del workflow per-playlist).
- **Longitud**: < 60 caracteres idealmente. Spotify corta en mobile.
- **Descripción**: primer párrafo listar artistas conocidos — son términos de búsqueda reales.

### Referencias

- Spotify Research (long-tail): https://research.atspotify.com/2021/03/query-understanding-for-surfacing-long-tail-music-content
- Spotify Research (agentic search 2025): https://research.atspotify.com/2025/9/you-say-search-i-say-recs-a-scalable-agentic-approach-to-query-understanding
- trendspyg: https://github.com/flack0x/trendspyg
- trendsmcp (free MCP): https://github.com/trendsmcp/google-trends-mcp
- SerpApi Google Trends (250/mes free): https://serpapi.com/blog/scraping-google-trends-with-python-pytrends-alternative/

### Rigor temático — selección track por track

El subtítulo (mood, tema, actividad) debe reflejarse en CADA track. No basta con que el género sintonice.

**Workflow de verificación por track:**

1. **Filtro grueso (API)**: explicit flag + título ausente de keywords prohibidas (§2.5 alcohol/droga/sexo)
2. **Filtro medio (título + artista)**: si el track es de un artista conocido sin historial de infracciones §7, pasa a revisión rápida
3. **Filtro fino (letra)**: para tracks sospechosos o fronterizos, leer letra completa y verificar alineación con el tema declarado de la playlist
4. **Prueba de coherencia**: ¿este track refuerza el subtítulo de la playlist o solo comparte género?

Si la playlist se titula "Triunfo y Transformación", cada track debe tener una conexión verificable con triunfo, superación o cambio positivo — no basta con que suene "épico".

## Workflow completo

### Fase 1 — Planificación
1. Definir canción a promover → ID Spotify, BPM, tonalidad, tema
2. Elegir género/mood → filtro de selección
3. Determinar proporciones de tiers y espaciado de propias

### Fase 2 — Descubrimiento de tracks (optimizado)

**⚠️ El cuello de botella es buscar + verificar uno por uno. Para acelerar:**

1. **Generar pool inicial con búsquedas por artista**, no por track:
   ```
   just playlist-search "género+artista conocido" track
   just playlist-search "género+mood" track
   ```
   Recoger ~150 URIs candidatas en 2-3 queries grandes.

2. **Filtrar grueso en lote** (todo vía API, una sola llamada con URIs):
   - `GET /tracks` batch (hasta 50 URIs) → explicit flag
   - Descartar explicit=true automáticamente
   - Marcar títulos con keywords de alerta: "sexual", "noche", "alcohol", "veneno", "piel", "cama"

3. **Clasificar tiers en lote** (`GET /artists` batch):
   - Mapear monthly listeners de cada artista
   - Asignar tier automáticamente por fórmula

4. **Verificación profunda** (solo lo que pasa filtro grueso):
   - Leer letras SOLO de tracks fronterizos (título sospechoso pero no explicit flag, o artista no conocido)
   - Para artistas ya verificados en playlists anteriores, reusar juicio (no releer)
   - Confirmar alineación con el tema declarado de la playlist

5. **No escuchar 30s de cada track manualmente** — confiar en metadata (BPM, energía, danceability vía API) para tracks no-Suno. Para Suno, escuchar solo tracks fronterizos.

### Fase 3 — Construcción
1. Crear la playlist vacía:
   ```
   just playlist-create "Título SEO" "Descripción con artistas"
   ```
   ⚠️ Usar SIEMPRE `POST /v1/me/playlists`. NO usar `/users/{id}/playlists`
   (devuelve 403).

2. Añadir tracks de una sola vez (80 URIs):
   ```
   just playlist-add <id> uri1 uri2...
   ```
   Usar `POST /v1/playlists/{id}/items`.

3. Verificar: `just playlist-tracks <id>`

### ⚠️ Limitaciones y hallazgos

**Endpoints:**
- **Leer tracks:** usar `GET /v1/playlists/{id}/items` (NO `/tracks` — da 403)
- **Añadir tracks:** usar `POST /v1/playlists/{id}/items` (NO /tracks — da 403)
- **Eliminar (unfollow) playlist:** `DELETE /v1/playlists/{id}/followers` (no la borra, solo la quita de tu perfil)
- **DELETE items:** `DELETE /v1/playlists/{id}/items` con `{"tracks":[{"uri":"..."}]}` devuelve 400 "No uris provided" — no funciona
- **Crear playlist:** `POST /v1/me/playlists` (NO `/users/{id}/playlists` — da 403)

**Para "actualizar", la única opción viable es:**
1. Crear playlist NUEVA: `just playlist-create "..." "..."`
2. Añadir todos los tracks: `just playlist-add <newId> uri1 uri2...`
3. Eliminar (unfollow) la vieja: `just playlist-delete <oldId>`

**La URL cambia cada vez.** PL1 v1→v2, PL2 v1→v2→v3.

**Respuesta de la API:** `tracks.total` retorna blank incluso con `fields=total`. Usar `/items?fields=total` para leer conteo.

### Fase 4 — Lanzamiento
1. Confirmar título SEO, descripción, cover art
2. Registrar la nueva playlist en `contacts/playlist-registry.csv` (ID, Name, URL, fecha, canción promovida)
3. Actualizar `contacts/playlist-artists.csv` con los artistas nuevos añadidos (añadir filas con Playlist_ID, Playlist_Name, Playlist_URL, IG, Contact_Tier)
4. Monitorear save rate (>3.5%), skip rate (<40%), completación
5. Refrescar 10-15% semanalmente

### Fase 5 — Outreach a artistas

**Contactar solo artistas B (<10k ML) y C (10k-100k ML).** D tier y superiores reciben demasiados mensajes y no responderán.

Archivos de referencia:
- `contacts/playlist-artists.csv` — todos los artistas, su playlist, IG, estado de contacto
- `contacts/playlist-registry.csv` — relación playlist ID ↔ nombre + URL

**Protocolo:**
1. Filtrar CSV por `Contact_Tier = "contact"` y `Status = "pending"`
2. Contactar vía IG DM con template del mensaje
3. Escalonar: 5-10 artistas por día (no saturar)
4. Actualizar `Status` a "contacted" tras enviar
5. Si responde → "responded"; si no responde en 7 días → "no_reply"
6. **No contactar al mismo artista más de una vez**, aunque aparezca en playlists nuevas — el CSV ya registra su historial

**Template DM (IG):**
```
Hola [artista], soy curador de "[Playlist_Name]" en Spotify.
Acabo de incluir "[Track]" porque encaja perfecto con el mood.
Si te gusta el proyecto, agradecería un share en stories. ¡Un abrazo!

🎵 [Playlist_URL]
```

## Optimización de velocidad

El proceso de 80 tracks puede tardar horas si se hace track por track. Estrategias para reducirlo a ~30 min:

### 1. Pool de candidatos pre-seleccionados
- Mantener un catálogo curado de artistas por tier (ver `contacts/artistas-playlist-balada-folk-latino.md`)
- Para playlists nuevas, empezar desde ese catálogo en vez de buscar desde cero
- Añadir ~10-15 artistas nuevos por playlist para expandir el pool

### 2. Operaciones batch vía API (no secuenciales)
- `GET /tracks?ids=...` (hasta 50 URIs) — explicit flag en 1 llamada
- `GET /artists?ids=...` (hasta 50 URIs) — monthly listeners en 1 llamada
- `GET /audio-features?ids=...` (hasta 100 URIs) — BPM/energy en 1 llamada (no funciona para Suno)
- Esto reduce de ~80 llamadas API a ~3-4

### 3. Shortcuts de verificación moral
- **explicit flag = true** → descartar automáticamente (sin leer letra)
- **Artista ya verificado** en playlist anterior → verificación rápida (solo confirmar que el track específico no introduce novedades §7, sin releer toda la discografía)
- **Emergente nuevo (B <10k, nunca evaluado)** → obligatorio leer al menos **2 canciones representativas** (la candidata + un hit del artista) para establecer juicio de su estilo lírico
- **Keywords en título** + cualquier artista → leer letra completa del track
- **Resto** → pasa filtro grueso

**⚠️ No sacrificar descubrimiento por velocidad.** Los 16 tracks B por playlist son el corazón de la estrategia. Invertir tiempo en evaluarlos bien; la optimización está en los tracks C/D/E que podemos procesar en lote.

### 4. Catálogo vivo de artistas verificados
- Mantener un registro (en `contacts/`) de artistas ya evaluados con su veredicto §7
- Para artistas B nuevos, añadirlos al registro tras la evaluación para que futuras playlists los tengan pre-aprobados
- Esto acelera PL3, PL4, etc. sin escatimar rigor en las primeras evaluaciones

### 4. Plantilla de playlist reutilizable
- Copiar estructura de tiers y espaciado de PL1/PL2
- Cambiar solo URIs, tier y título — no rediseñar la estructura cada vez

### 5. Batch de adds
- Añadir tracks de 50 en 50 (límite Spotify: 100 por request)
- Verificar conteo final con `GET .../items?fields=total`

## Hallazgos de procedimiento

### API de Spotify
- **Refresh token cada ~1h** — usar script (refresh automático desde `.env`)
- **PUT playlist** crea vacía; **POST items** añade — no hay "crear con tracks"
- **Items en `items[].track`** (vía GET .../items)
- **URIs inválidas = silencioso** — verificar siempre con GET después
- **Popularidad vacía** para distribuidores indie / Suno AI (OffStep)
- **PUT /v1/playlists/{id}** actualiza título/desc (status 200, sin body)
- **403 en audio-features** para tracks Suno — no se obtiene BPM/key/energy

### Suno AI
- JPMarichal (ID: `39fvIeIzCHa9nEgTMPtcAe`) — todas las tracks popularidad 0
- `audio-features` retorna 403 — no se puede analizar BPM propio

## Playlist v1 — "Balada Folk Latino: Nostalgia, Raíces y Hogar"

| Propiedad | Valor |
|-----------|-------|
| **Canción promovida** | Mamá, si vuelvo a verte (#10, `0Db0xDc6rhBRHd12Sq5lZ5`) |
| **URL** | https://open.spotify.com/playlist/3RemCcFC1HkpdutHaATLbp |
| **Tracks** | 80 verificados |
| **Tiers realizados** | A=4, B=9, C=19, D=26, E=22 |
| **Archivo fuente** | `canciones/playlist-raices-y-vuelo.txt` |
| **Propias** | #5 Mamá, si vuelvo a verte / #25 Que Das la Vida para Dar Vida / #45 El Remanso de Su Voz / #65 Mármol Que Respira |

## Comandos Just
```bash
just playlist-create "Título" "Descripción" true|false
just playlist-add <playlistId> <uri1> <uri2>...
just playlist-clear <playlistId>
just playlist-delete <playlistId>
just playlist-search "término" track|artist|playlist
just playlist-tracks <playlistId>
just playlist-upload <id> "Title" "Desc" true|false uri1 uri2...
```

## Script
`scripts/spotify-playlist.ps1` — Lee credenciales de `.env`.

## API Limitations
- **Popularity = null** para nuestra app (playlister, creada post-Feb 2026 en dev mode). No se puede obtener ni popularity ni stream counts vía API.
- **Medir efectividad**: usar **Spotify for Artists** → Music tab → seleccionar canción → ver streams, save rate, skip rate, source of streams, monthly listeners.
- **Save rate benchmark**: >3-4% es saludable. >5% excelente. <2% indica desajuste de audiencia.
- **Refresh token**: extraer con `$line -split '=', 2 | Select-Object -Last 1`. NO usar `-replace '.*= '`.

## Datos fijos
- App: **playlister** (Spotify Developer Dashboard)
- Client ID: `a71a05d01e87436e863eb717b975a421`
- Redirect URI: `http://127.0.0.1:8080/callback/`
