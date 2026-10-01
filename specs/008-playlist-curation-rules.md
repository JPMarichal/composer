# Playlist Curation Rules

## Fuente

Investigación validada con:

| Fuente | Hallazgo clave |
|--------|---------------|
| **OnesToWatch (2026)** | Playlists temáticas de 80 tracks = mejor descubrimiento. **30-sec rule**: >40% skip rate antes de 30s mata el algoritmo. **70/30**: 70% emergentes/indie, 30% establecidos. Refrescar 10-15% del contenido semanalmente. |
| **Chartmetric (2025-26)** | **Save rate >3.5%** = 5x más probabilidad de trigger Discover Weekly. Tasa de skip vs completación es la métrica #1. **Discovered On %** determina si tu playlist rankea. |
| **PlaylistSupply (2026)** | **Discovered On** es más importante que follower count. Una playlist de 5k seguidores con alto Discovered On genera más exposición real que una de 500k sin él. |
| **Orphiq** | **10-20% máximo** de canciones propias por playlist. Own tracks nunca en posición #1. |
| **Hypebot / OneSubmit** | Análisis de **100K+ submissions**: playlists con <50 tracks tienen engagement más alto. **Hook en primeros 15s** crítico. |
| **MusicPulse** | Playlists **mood/genre** específicas (no "mezclas") tienen mejor CTR y retención. |
| **artist.tools** | **Cover art consistente** con el género mejora la tasa de click en el feed. |

## Reglas generales

- **Playlist de 80 canciones** para promoción
- **4 canciones propias** (5%) — máximo Orphiq: 10-20%
- **Nunca canción propia en #1** — oyente percibe autopromoción y salta
- **Espaciar canciones propias**: mínimo 15-20 tracks entre cada una
- **Evitar instrumentales** en playlists vocales — el cambio de textura rompe el mood
- **30-sec rule**: hook en primeros 15-30s en cada track (Spotify: skip rate >40% antes 30s penaliza el algoritmo)
- **BPM progression**: ~70% entre 60-90 BPM
- **SEO del título — basado en investigación (no asumir género=primario)**: El término con **mayor search volume** va primero — puede ser actividad, mood, era o género, NO siempre el género. 4 dimensiones: actividad (workout, study, focus), mood (chill, sad, nostalgic, energetic), género/subgénero (lofi, indie folk, phonk), era/contexto (2000s, late night). Estructura: `[Primary high-volume] : [Secondary mood/activity], [Tema]`. Ejemplos válidos SOLO si la research confirma el primary:
  - ✅ "Balada Folk Latino: Nostalgia, Raíces y Hogar" — válido si `balada folk` gana en search vs `baladas para mamá` o `música nostálgica latina`
  - ✅ "Indie Pop Épico: Triunfo y Transformación" — válido si `indie pop` es el primary
  - ✅ "Estudio: Balada Folk Latino, Nostalgia" — alternativa si `estudio`/`focus` tiene más search
  - ❌ "Raíces y Vuelo" (poético, no se entiende el género)
- **Patrón "Research-Once-Use-Many"** — objetivo: 2-3 min por playlist, no 15-20:
  - **One-time (1-2h)**: poblar `kw-pool/<genero>-<mercado>.json` con 30-50 keywords + Google Trends data + Spotify Search proxy. Mercados meta iniciales: ES, MX, AR. Géneros: balada, pop, indie/folk, indie pop, folk latino
  - **Per-playlist (2-3 min)**: (1) pick 5-8 candidatos de `kw-pool/`, (2) 30s Spotify Autocomplete check, (3) opcional `just kw-spotify` o `just kw-trends` para tie-break, (4) componer título, (5) documentar en changelog
  - **Monthly refresh (15 min)**: re-correr trendspyg en top 20 keywords
- **Herramientas gratuitas** (sin coste):
  - **Spotify Search API** (nuestra `playlister` app) — `GET /v1/search?type=playlist&q=<term>`. Títulos de top playlists = proxy directo de queries reales
  - **trendspyg** (`flack0x/trendspyg`) — Google Trends sin API key, 125 países, RSS-based, sin 429
  - **trendsmcp MCP** (free tier 100/día) — alternativa MCP con Claude/Cursor
  - ~~pytrends~~ — archivado, 429, no usar
  - ~~artist.tools~~ — sin plan de pago, free tier inútil
- **Procedimiento**: (a) consultar `kw-pool/` para el (género × mercado), (b) componer título con la estructura, (c) verificar la prueba: "si alguien lee SOLO el título, ¿sabe qué género esperar Y usaría esas palabras para buscar?"
### Descripción SEO — Fórmula y uso

**Hallazgo clave** (playlistfeed, artist.tools, playlistpush 2025-26): Spotify indexa TANTO el título COMO la descripción. La descripción alimenta long-tail keywords que el título no puede cubrir. Ambos factores determinan Relevancia — el primero de los 3 pilares del algoritmo.

**Fórmula de descripción (40-60 palabras):**

```
[1-2 frases: genre + mood + actividad] + [Artistas comparables] + [Propuesta de valor] + [Frecuencia]
```

| Componente | Qué poner | Ejemplo |
|------------|-----------|---------|
| **Género + Mood** | Descriptores del género + emoción principal | "Chamber pop español con cuerdas, piano y voz íntima" |
| **Actividad** | Cuándo/para qué se escucha | "Para soñar despierto, leer o contemplar la lluvia" |
| **Artistas comparables** | Nombres reales que la gente busca | "Natalia Lafourcade, Silvana Estrada, Carla Morrison" |
| **Propuesta de valor** | Por qué esta playlist y no otra | "Una pausa elegante en un mundo ruidoso" |
| **Frecuencia** | Señal de freshness para el algoritmo | "Actualizada cada semana" |

**Ejemplo aplicado — Chamber Pop:**
> "Chamber pop y baroque pop en español: cuerdas, piano y voz íntima para soñar despierto. Inspirada en Natalia Lafourcade, Silvana Estrada, Carla Morrison y Jorge Drexler. Una pausa elegante en un mundo ruidoso. Actualizada semanalmente."

**Ejemplo aplicado — Balada Folk:**
> "Balada folk y canción de autor latinoamericana: guitarra acústica, harmonía y letras que abrazan. Mercedes Sosa, Violeta Parra, Silvio Rodríguez, Kevin Kaarl. Para los que extrañan, recuerdan o buscan hogar. Actualizada cada semana."

**Reglas de descripción:**
1. **Artistas van en la descripción, NO en el título** — el título es para keywords de género/mood; los artistas son long-tail
2. **Máximo 100 caracteres por frase** — Spotify truncar en móvil
3. **Incluir 3-5 artistas** — suficiente para SEO, no tanto para parecer spam
4. **Nunca keyword-stuffing** — el algoritmo detecta texto antinatural (Spotify Community, 2020)
5. **Cover art consistente** — la descripción atrae, la imagen decide el click (artist.tools)

## Proporción por tiers

| Tier | ML | Cantidad | % | Rol |
|------|-----|----------|---|-----|
| JPMarichal | <1k | 4 | 5% | Anclas temáticas |
| New Emerging | <10k | 16 | 20% | Descubrimiento |
| Rising Indie | 10k-100k | 24 | 30% | Core del mood |
| Established | 100k-1M | 21 | 26% | Anclas retención |
| Mainstream | >1M | 16 | 20% | Ganchos anti-skip |

En la práctica (v1 "Balada Folk Latino"), la realización fue: A=4, B=9, C=19, D=26, E=22.
Faltaron B y C vs objetivo. Para v2+ priorizar más emerging y rising sobre established/mainstream.

## Mapa de posiciones

| Posición | Tier | Principio |
|----------|------|-----------|
| 1 | Mainstream | Hook fuerte primeros 15s |
| 2-4 | Mix D+E | Construcción del mood |
| **5** | **Propio #1** | Oyente ya confía — temprano pero no intrusivo |
| 6-10 | Alternar B/C/E | Profundidad sin perder oyente |
| 11-24 | Mayoría B+C | Zona de descubrimiento |
| **25** | **Propio #2** | Punto medio (spacing ~20 desde #5) |
| 26-44 | Alternar todos | Variedad |
| **45** | **Propio #3** | Oyente comprometido (spacing ~20) |
| 46-64 | Mix B+C+D | Cierre gradual |
| **65** | **Propio #4** | Último ancla antes del cierre |
| 66-80 | Mix D+E | Cierre cómodo y fuerte |

## Código moral — Filtro de artistas

Basado en §7 del spec 002-anti-ai-isms.md. Los artistas en la playlist deben:

| Situación | Permitido | Prohibido |
|-----------|-----------|-----------|
| Alcohol/drogas/tabaco | Contexto negativo | Como celebración o refugio |
| Sexo | Cero menciones | Ni implícito ni idealizado |
| Violencia | Contexto crítico | Como catarsis o empoderamiento |
| Familia | Lazos imperfectos pero reales | Familia como jaula |
| Esperanza | Concreta, basada en acciones | Vacía o mágica |
| **Lenguaje** | Cero malas palabras | Ni en título ni letra |
| **Café** | Cero menciones | Ni siquiera como metáfora |

**Filtro de título automático:** si el título contiene malas palabras, café, alcohol,
drogas, tabaco, sexo o violencia, la pista se descarta sin revisar letra. El título
es señal de alerta suficiente.

**Artistas eliminados durante auditoría:**
- Bad Bunny (reggaeton explícito, sexual)
- Enrique Iglesias ("EL BAÑO" es sexual explícito)
- Pau Laggies ("Me Caga Tu Novia" — mala palabra en título) → reemplazado en PL1 y PL2
- Jimena Amarillo ("Cafeliko" — café como tema central) → reemplazada con "Mandarinas en la cocina" (mismo artista, track distinto)

## Flujo de trabajo completo

### Fase 1 — Planificación
1. Elegir canción a promocionar y su tema central (ej: "Mamá, si vuelvo a verte" → madres/raíces/nostalgia/inmigración)
2. Definir género anchor y BPM target (ej: Balada Folk, 60-90 BPM)
3. Determinar proporciones de tiers y espaciado de propias

### Fase 2 — Descubrimiento de tracks
1. **Buscar por keyword en Spotify:**
   ```
   just playlist-search "balada folk" track
   just playlist-search "canción de autor" track
   just playlist-search "música nostálgica" track
   ```
2. **Verificar cada candidato:**
   - Escuchar primeros 30s (hook rate)
   - Identificar tier por monthly listeners (abrir perfil del artista)
   - Confirmar no viola código moral
3. **Clasificar por tier y registrar URI** en archivo seed

### Fase 2.5 — Validación de género (OBLIGATORIA antes de publicar)
> **Lección aprendida:** La playlist "Chamber Pop Romántico" contenía folk-pop e indie pop, no chamber pop. El oyente que busca chamber pop y escucha folk-pop siente que se le mintió. Esto mata la retención.

1. **Verificar los 5 primeros tracks** de la playlist candidates contra el género prometido en el título:
   - Abrir cada track en Spotify → ver "Fans also like" del artista → ¿el artista suena a chamber pop / folk / indie / lofi / etc.?
   - Si 2+ de los 5 primeros NO pertenecen al género del título → **cambiar el título** para reflejar el contenido real
2. **Aplicar la "prueba del bar":** Si un hablante nativo del género escucha los primeros 60s, ¿diría "esto es [género del título]"? Si la respuesta es no → nombre engañoso.
3. **Verificar descripción:** Los artistas mencionados en la descripción deben SÍ aparecer en la playlist (no solo en la descripción). La descripción es una promesa.
4. **Registrar resultado** en el changelog de la playlist: "Género validado: [X]. Tracks verificados: [lista]. Resultado: PASS/FAIL".

### Fase 3 — Construcción
1. **Crear la playlist vacía:**
   ```
   just playlist-create "Título SEO: Subtítulo Descriptivo" "Descripción con artistas clave..."
   ```
2. **Añadir tracks de una sola vez** (80 URIs en un único `PUT /v1/playlists/{id}/tracks`):
   ```
   just playlist-upload <id> "Title" "Desc" true|false uri1 uri2...
   ```
3. **Verificar:** `just playlist-tracks <id>`

### Fase 4 — Descripción SEO
1. **Componer descripción** con la fórmula de 5 componentes (ver §Descripción SEO)
2. **Validar:** ¿Los artistas mencionados son buscables en Spotify? (no artistas underground)
3. **Validar:** ¿La descripción supera la "prueba del escáner"? (si alguien lee solo descripción, ¿sabe qué encontrará?)
4. **Insertar en playlist** al crear con `just playlist-create` o actualizar con `PUT /playlists/{id}`

### Fase 5 — Lanzamiento
1. Confirmar título, descripción, cover art
2. Monitorear save rate (>3.5%), skip rate (<40% primeros 30s), completación
3. Refrescar 10-15% del playlist semanalmente (OnesToWatch)
4. **Cada 2 semanas:** revisar si la descripción sigue alineada con trending artists del género

## Hallazgos de procedimiento

### API de Spotify

1. **Refresh token (crítico):** El token de acceso expira cada ~1h. El refresh token
   está en `.env` como `SPOTIFY_REFRESH_TOKEN`. El script `scripts/spotify-playlist.ps1`
   refresca automáticamente. Para operaciones ad-hoc desde CLI, copiar el bloque de
   refresh de 5 líneas del script.

2. **Crear playlist:** Usar `POST /v1/me/playlists` (NO `/users/{id}/playlists` que
   devuelve 403). Crea una playlist vacía. Luego `POST /v1/playlists/{id}/items`
   añade tracks. NO hay endpoint para "crear playlist con tracks".

3. **Límite de búsqueda:** API de Spotify max `limit=20` en search. Usar sin
   parámetro `limit` para default 20. No se puede paginar eficientemente.

4. **Estructura de respuesta playlist:** `GET /v1/playlists/{id}` devuelve items
   en `.items.items[].item` (no `.tracks.items[].track` como el endpoint de items).
   Si un track tiene URI inválida, aparece como `$null` o `.item = $null`.

5. **URIs inválidas son silenciosas:** La API acepta URIs inválidas en add-tracks
   sin devolver error — simplemente ignora esa URI. Siempre verificar con `GET`
   después de añadir. En v1, "Amor Eterno - Rocío Dúrcal" no se añadió silenciosamente
   (URI: `spotify:track:3MlrCa3bY4HSM3U3Lz8Cx3`). La playlist reportó 80 items pero
   solo 79 tenían nombre.

6. **Popularidad vacía:** Canciones de distribuidores independientes (OffStep,
   DistroKid, etc.) pueden tener popularidad = 0 o `null`. El endpoint
   `audio-features` devuelve 403 para tracks distribuidos por Suno AI (retorno
   de inversión: no se puede obtener BPM, key, energy de las propias canciones).

7. **Actualizar título/descripción:** `PUT /v1/playlists/{id}` con JSON body
   `{ "name": "...", "description": "..." }`. No retorna body en éxito (solo
   status 200).

8. **Eliminar tracks (no funciona):** `DELETE /v1/playlists/{id}/items` con
   `{"uris":[]}` devuelve 400, y con `{"tracks":[...]}` devuelve 403. Para
   cambiar tracks, crear playlist nueva y eliminar la vieja (`DELETE /playlists/{id}/followers`).

### Suno AI tracks

- **403 en audio-features** para tracks distribuidos por Suno (OffStep). No se puede
  obtener BPM, key, energy, danceability de canciones propias.
- **Popularidad vacía** para el mismo perfil. JPMarichal (artist ID:
  `39fvIeIzCHa9nEgTMPtcAe`) tiene todas las tracks con popularidad 0 — consistente
  con perfil <1k monthly listeners.

### SEO y naming

- **NO usar títulos poéticos/abstractos** ("Raíces y Vuelo") — nadie los busca.
- **Patrón Research-Once-Use-Many** — 2-3 min por playlist, no 15-20. Mantener `kw-pool/` cacheado.
- **Workflow per-playlist**:
  1. Pick 5-8 candidatos de `kw-pool/<genero>-<mercado>.json`
  2. 30s Spotify Autocomplete check
  3. Opcional: `just kw-spotify "termino" "ES"` o `just kw-trends "termino" "ES"` para tie-break
  4. Componer título `[Primary] : [Secondary], [Tema]`
  5. Documentar en changelog
- **Sí usar formato** `[Primary] : [Secondary], [Tema]` — ej: "Balada Folk Latino:
  Nostalgia, Raíces y Hogar" (válido SOLO si research confirmó que `balada folk` es
  el primary; sino ajustar — ej: "Estudio: Balada Folk, Nostalgia")
- **Descripción:** primero 1-2 frases con artistas conocidos del playlist —
  son términos de búsqueda reales en Spotify. Ej: "Balada folk y canción de autor
  latinoamericana. Mercedes Sosa, Natalia Lafourcade, Silvio Rodríguez..."
- **Cover art:** consistente con el género del playlist (MusicPulse). Idealmente
  una imagen cálida y orgánica para folk/balada.

### Keyword pool (`kw-pool/`)

Estructura de archivos:
```
kw-pool/
├── README.md                       # criterios de inclusión, fecha de último refresh
├── balada-ES.json                  # mercado España
├── balada-MX.json
├── balada-AR.json
├── pop-ES.json
├── indie-folk-MX.json
└── ... (un JSON por género × mercado)
```

Cada JSON contiene:
```json
{
  "mercado": "ES",
  "genero": "balada",
  "last_refresh": "2026-06-06",
  "keywords": [
    {
      "term": "balada folk",
      "dimension": "género",
      "trends_interest_30d": 65,
      "trends_related_queries": ["balada folk español", "balada folk latino"],
      "spotify_playlist_count": 1240,
      "spotify_top_titles": ["Balada Folk Latino: ...", "Baladas en Español: ..."],
      "is_primary_candidate": true
    }
  ]
}
```

## Credenciales y datos persistentes

| Variable | Valor | Dónde |
|----------|-------|-------|
| SPOTIFY_CLIENT_ID | `a71a05d01e87436e863eb717b975a421` | `.env` |
| SPOTIFY_CLIENT_SECRET | `8d4f5bcf145045fcade0ba0790b19bfe` | `.env` |
| SPOTIFY_REFRESH_TOKEN | (en .env) | `.env` |
| SPOTIFY_USER_ID | `12141566464` | `.env` |
| App | playlister | Spotify Developer Dashboard |
| Redirect URI | `http://127.0.0.1:8080/callback/` | registrada en dashboard |
| JPMarichal artist ID | `39fvIeIzCHa9nEgTMPtcAe` | fijo |
| Mamá, si vuelvo a verte | `spotify:track:0Db0xDc6rhBRHd12Sq5lZ5` | fijo (#5) |
| Que Das la Vida para Dar Vida | `spotify:track:6XhccyJwqQwbzLO29ooyKw` | fijo (#25) |
| El Remanso de Su Voz | `spotify:track:49oZsVhJ9bNQB3LmpMMX7K` | fijo (#45) |
| Mármol Que Respira | `spotify:track:6OeAtwcT7NcWWzAl4P1zrr` | fijo (#65) |

## Inventario de canciones — Catálogo propio con metadata

> **Objetivo:** Matching instantáneo canción↔playlist sin research cada vez. Los curadores profesionales mantienen un catálogo con metadata por cada track. Esto permite saber en 5s qué canción va en qué playlist.

### Formato del inventario

Cada canción del catálogo propio debe tener:

| Campo | Ejemplo | Uso |
|-------|---------|-----|
| **Título** | La Magia del Violín | Identificación |
| **Spotify URI** | `spotify:track:5j2BEitZnNLAAyjOp3I6cS` | Para playlists |
| **Género primario** | Chamber pop | Matching por género |
| **Género secundario** | Folk pop, Indie | Matching por mood |
| **Mood** | Intimo, Nostalgico, Esperanzador | Matching por情绪 |
| **BPM** | 72 | Progresión rítmica |
| **Tonalidad** | G major | Compatibilidad armónica |
| ** comparable artists** | Silvana Estrada, Carla Morrison | SEO descripción |
| **Keywords SEO** | chamber pop español, cuerdas voz íntima | Título/descripción |
| **Distribuido** | Sí/No | Filtrado |
| **Playlist themes** | Folk íntimo, Chamber pop, Nostalgia | Matching rápido |

### Cómo usar el inventario

1. **Al crear playlist:** Buscar en el inventario por género/mood → seleccionar candidatos → verificar con Fase 2.5
2. **Al escribir descripción:** Tomar "comparable artists" del inventario → incluir en descripción (máx 3-5)
3. **Al buscar keywords:** Usar "keywords SEO" del inventario como punto de partida para kw-pool

### Mantenimiento

- **Al distribuir canción nueva:** Agregar al inventario con todos los campos
- **Cada 3 meses:** Revisar comparable artists (¿siguen siendo relevantes?)
- **Fuente de verdad:** `docs/indice-por-genero.md` + inventario = catálogo completo

## Scorecard — Métricas de éxito

| Métrica | Target | Fuente |
|---------|--------|--------|
| Save rate | >3.5% | Chartmetric — 5x más probable trigger Discover Weekly |
| Skip rate primeros 30s | <40% | OnesToWatch — penalización algorítmica |
| Compleción promedio | >60% | Chartmetric — sesiones de >30 min |
| Discovered On | >15% | PlaylistSupply — ranking en resultados de búsqueda |
| Crecimiento semanal seguidores | >5% | Referencia industria playlist curada |
| Ratio emergentes/establecidos | ~70/30 | OnesToWatch — mejor descubrimiento |

## Playlist "Balada Folk Latino: Nostalgia, Raíces y Hogar" — 80 canciones

**URL final:** https://open.spotify.com/playlist/3RemCcFC1HkpdutHaATLbp
**Canción promovida:** Mamá, si vuelvo a verte (JPMarichal) — posición #5
**Playlist anterior (eliminada):** 3xU4ojrteEuf2SbbjNTzaN
**Tema:** Balada folk, madres/raíces/infancia/inmigración/nostalgia
**BPM target:** 60-90
**Instrumentación:** Piano, cuerdas, guitarra acústica

### Composición final

A=Propio(4) B=Emerging(~9) C=Rising(~19) D=Established(~26) E=Mainstream(~22)

| # | Canción | Artista | URI |
|---|---------|---------|-----|
| 1 | Hasta la Raíz | Natalia Lafourcade | spotify:track:3lGMtkONrZdJ8kTCg6KIFf |
| 2 | Gracias A La Vida | Mercedes Sosa | spotify:track:0UKSse3fcKetDzXnXzE1Pv |
| 3 | Tu Falta De Querer | Mon Laferte | spotify:track:4skuEIloXWuxxgekKupkEH |
| 4 | Volver a los 17 | Violeta Parra | spotify:track:5bf9o4Nok6R91nwKhG1moz |
| 5 | **Mamá, Si Vuelvo a Verte** | **JPMarichal** | spotify:track:0Db0xDc6rhBRHd12Sq5lZ5 |
| 6 | Clandestino | Manu Chao | spotify:track:51R2M1JgyFfRS3e6v5wCt3 |
| 7 | Vas A Quedarte | Aitana | spotify:track:0fwIHsKXNEcb57u2um7z9I |
| 8 | Canción De Las Simples Cosas | Mercedes Sosa | spotify:track:540A2oZpEHjdMpCSBhF0xx |
| 9 | Fina Estampa | Chabuca Granda | spotify:track:2zwlCikJuu9eBNoIWsNssW |
| 10 | No Soy De Aqui, Ni Soy De Alla | Facundo Cabral | spotify:track:70xSLxbCLBQSxBtP46AuZq |
| 11 | El Breve Espacio | Pablo Milanés | spotify:track:0zUfQGC8ZeZiHMIsT1HSxa |
| 12 | Todo Cambia | Mercedes Sosa | spotify:track:0njOsb3y8TnwIJC7GnlWwD |
| 13 | Gracias a la Vida | Violeta Parra | spotify:track:0GO8mb18nuWS3rh5Aihscy |
| 14 | San Lucas | Kevin Kaarl | spotify:track:3aZxnqYFM8UI2jLgUD3B2a |
| 15 | La Carta | Los Tigres Del Norte | spotify:track:61Ym6uMASRkhoKFxMb2Nof |
| 16 | Algo Contigo | Cecilia Gallardo | spotify:track:6WiKa6osuUaYf5os6ZD45e |
| 17 | Alfonsina Y El Mar | Mercedes Sosa | spotify:track:6Q3ozAXkxLpKQy6sc8L0TY |
| 18 | Dueles | Jesse & Joy | spotify:track:1iRvhKiXRElIH2Uf4gd95P |
| 19 | Corazón partío | Alejandro Sanz | spotify:track:0wQCKR9OFjYu5Kzrk7WivJ |
| 20 | El Día Que Me Quieras | Carlos Gardel | spotify:track:6sGfYOW9RUwGDm9xlrzutp |
| 21 | Amapolas | Leo Rizzi | spotify:track:0z5yLgBmAtaylDYrgwzlpH |
| 22 | Solamente tú | Pablo Alborán | spotify:track:7vd2YXwqxAG2BGuEUoMzGl |
| 23 | El Mismo Sol | Alvaro Soler | spotify:track:58WOkUl3O9LvLZjdhiQvIX |
| 24 | No Me Doy Por Vencido | Luis Fonsi | spotify:track:4lerOTNr2tFWJCAmmhymhi |
| 25 | **Que Das la Vida para Dar Vida** | **JPMarichal** | spotify:track:6XhccyJwqQwbzLO29ooyKw |
| 26 | Robarte un Beso | Carlos Vives | spotify:track:0JcNysfWVWaMS7R6vzGB2k |
| 27 | Te Quiero | Mau y Ricky | spotify:track:7GzRxRiDEBBa42S6Nx3IHJ |
| 28 | Ojalá | Beret | spotify:track:75KrTLbcLWgCcldZGxZR12 |
| 29 | Tacones Rojos | Sebastian Yatra | spotify:track:0Be7sopyKMv8Y8npsUkax2 |
| 30 | Madrecita | José José | spotify:track:4RQpKdmRVAjNXjqZo2OWoW |
| 31 | La Frontera | Juan Gabriel | spotify:track:50zWrJYU2srHaKA14dvyKu |
| 32 | Abrázame Muy Fuerte | Juan Gabriel | spotify:track:2nejvFyJeTDtMRP2nUMt0J |
| 33 | Florecita Rockera | Aterciopelados | spotify:track:7dg3Q2HXM5tlaV5B5KXhTr |
| 34 | Guantanamera | Guitarricadelafuente | spotify:track:6rlI9zMChJzIv5u0iSBO4l |
| 35 | Te Guardo | Silvana Estrada | spotify:track:0MbiIQrfTj9U3MXzv3AsoK |
| 36 | En Otra Vida | Yami Safdie | spotify:track:0EhmTBq33eARyOz3SIi4P2 |
| 37 | Vas a encontrarte | Muerdo | spotify:track:5koBWoS2PnjWSOsiHVlXQv |
| 38 | Ojos Noche | Elsa y Elmar | spotify:track:69xKQh7dxKqCe91WbGUhWv |
| 39 | Flores | Daniela Spalla | spotify:track:3IdwVRNZzzkoz0QJg72Lyq |
| 40 | Ojalá | Silvio Rodríguez | spotify:track:5NhaohsLVlQa3RpOCD2V4X |
| 41 | Unicornio | Silvio Rodríguez | spotify:track:5g7RWYeiBzkzUZn2TSr4gF |
| 42 | Yolanda | Pablo Milanés | spotify:track:2A0ZLZ2Bixhcnf9Jkdh5Xp |
| 43 | La Puerta Violeta | Rozalén | spotify:track:42ZASSKlh3UtYCgwZb8lBS |
| 44 | Limón y Sal | Julieta Venegas | spotify:track:7dITAq1YP5e0kTcaDq4YWI |
| 45 | **El Remanso de Su Voz** | **JPMarichal** | spotify:track:49oZsVhJ9bNQB3LmpMMX7K |
| 46 | Andar Conmigo | Julieta Venegas | spotify:track:05iMQqncVBIm4AE26EvaTL |
| 47 | Te Vi | Julieta Venegas | spotify:track:3JBFUsZatpE435Y8ejP7RZ |
| 48 | Me Miras Pero No Me Ves | María José Llergo | spotify:track:0Q8CGolKgAJPl2EV3k2p3k |
| 49 | Amor de Anticuario | Sofia Ellar | spotify:track:3v76x7Laqw77NNygd5QvcX |
| 50 | El Baile | Pedro Pastor | spotify:track:2In3kGLwM10ViRLBVJnVhI |
| 51 | Eres Tú - Mamá | Carlos Rivera | spotify:track:3Paluopb7bgoB5gHj4Z1k7 |
| 52 | Aunque tú no lo sepas | Enrique Urquijo | spotify:track:2VybHZvsshGs8GpOaB0wS1 |
| 53 | Chica de ayer | Nacha Pop | spotify:track:4chpfrjIqrOPshlDU4ZrKe |
| 54 | Maria Cristina | Vieja Trova Santiaguera | spotify:track:6R9jgcolWRwvk6WLqzp27A |
| 55 | El amor después del amor | Fito Páez | spotify:track:1PQzZbitOJ6XPFg7FFzsKQ |
| 56 | Comiendote a Besos | Rozalén | spotify:track:02FKjeU8CrA2ckppBa5RJg |
| 57 | mejores amigos | Paula Koops | spotify:track:3UO6Hj6xtowWdanb3hs5QR |
| 58 | Nunca Es Suficiente | Los Ángeles Azules | spotify:track:0HlMshB5JmZjPNbOuOgFHN |
| 59 | Es Por Ti | Juanes | spotify:track:3b1IQflSLrgzYQPGFzI9cl |
| 60 | Así Como Hoy | Amanda Miguel | spotify:track:6EYP9tf0c261shAYPTltw2 |
| 61 | Valentina | Carla Morrison | spotify:track:5YI1qT0IqnBt4hfEXgHfdE |
| 62 | lo que un día fue | Paloma Morphy | spotify:track:3b9BBjthb7r9Jn5yyWMlrm |
| 63 | Polvo de mariposas | Vanesa Martín | spotify:track:2Qh8SdiYF0JEjTLPvlFE8C |
| 64 | guerrera | Valeria Castro | spotify:track:4zXhEgk3gx2HkLVREPBYdq |
| 65 | **Mármol Que Respira** | **JPMarichal** | spotify:track:6OeAtwcT7NcWWzAl4P1zrr |
| 66 | Qué Bello Es Vivir | El Kanka | spotify:track:19DGqUZiSINPaWi1zsGsM9 |
| 67 | Te Regalo - Versión Desnudo | Carla Morrison | spotify:track:6m2zdtNuSoZSjN4FtNR1sJ |
| 68 | Rara Bien | Rupatrupa | spotify:track:0vccKCMndMlg1ZVfGllV63 |
| 69 | Vámonos De Viaje | Bandalos Chinos | spotify:track:1tyI6Sq6oBLsMmIgvBfQrI |
| 70 | Respiro (Cap. 8) | Siddhartha | spotify:track:5O612Iau2nHDR3yv8jAFXs |
| 71 | Para Que No Me Olvides | Tony Acosta | spotify:track:5zToFZsOW3uV98BrfvB2Z9 |
| 72 | Mandarinas en la cocina | Jimena Amarillo | spotify:track:4GAt1gXPMOk11qAuOHIC5N |
| 73 | 9Amor | Gala Briê | spotify:track:6UMFZWqCG8K5G31MmodMtw |
| 74 | Handful of Water | Sofía Valdés | spotify:track:4ieunk0Q7WADWYoZMSolwG |
| 75 | El Anhelo - Bulerías | Israel Fernández | spotify:track:7aHKl52jUd9Yyj4q1eegCk |
| 76 | El Tiempo Está Después | Jorge Drexler | spotify:track:35bUtk1405wm3ZR03FaXF1 |
| 77 | Maldita Dulzura | Vetusta Morla | spotify:track:1RnDdNwGdqTMSTiZmSLYdU |
| 78 | Copacabana | IZAL | spotify:track:5FrtmkTTf45HUlP9mwSAYZ |
| 79 | Allí donde solíamos gritar | Love of Lesbian | spotify:track:29tVNOmg85qDLh2wVnJxpv |
| 80 | Aquí te espero | Laia Lepiani | spotify:track:1WvWaKRZA7NfJVY95GR8aD |

## Plan de uso efectivo — Descripción SEO

### Objetivo
Que cada playlist nuestra sea encontrada por **dos caminos**: búsqueda directa (título) y browsing de artistas similares (descripción). La descripción convierte clicks en seguidores.

### Workflow por playlist (5 min extra, no 15)

| Paso | Acción | Tiempo |
|------|--------|--------|
| 1 | Elegir 3-5 artistas comparables del kw-pool (los que tienen mayor search volume) | 30s |
| 2 | Escribir 1-2 frases con genre + mood + actividad | 1min |
| 3 | Añadir artistas + propuesta de valor + "Actualizada semanalmente" | 1min |
| 4 | Validar: ¿Artistas son buscables? ¿描述 supera prueba del escáner? | 1min |
| 5 | Insertar en `PUT /playlists/{id}` o crear con `playlist-create` | 30s |

### Auditoría de playlists existentes

Cada playlist activa debe tener su descripción revisada:

| Playlist | Estado actual | Acción necesaria |
|----------|---------------|------------------|
| Balada Folk Latino (3RemCcFC1HkpdutHaATLbp) | Revisar | Aplicar fórmula si no la tiene |
| Chamber Pop (7tFHlHONqE3Hhy2XfK59xC) | Nueva | Escribir descripción con fórmula |
| Indie Pop Épico (3A35KIqDxtIPnmU9FrAkAH) | Revisar | Verificar artistas en descripción |

### Métricas de impacto

| Métrica | Antes (sin descripción optimizada) | Target (con fórmula) |
|---------|-------------------------------------|----------------------|
| Discovered On % | <10% | >15% |
| CTR desde búsqueda | Bajo | +20% relativo |
| Save rate | >3.5% | >5% (la descripción refuerza expectativa) |

### Errores comunes a evitar

| Error | Por qué falla | Solución |
|-------|---------------|----------|
| Descripción vacía | Spotify no tiene contexto para clasificar | Siempre escribir |
| Artist-stuffing (>8 parecidos) | Parece spam, penalización | 3-5 artistas máximo |
| Artistas no buscables | Nadie los busca = SEO muerto | Solo artistas con >100k ML |
| Descripción genérica ("música bonita") | No diferencia de otras playlists | Ser específico: género + mood + actividad |
| No actualizar | Freshness signal se pierde | Revisar cada 2 semanas |

## Comandos útiles

```bash
just playlist-create "Título" "Descripción" true|false   — Crear playlist (siempre nueva)
just playlist-upload <oldId> "Title" "Desc" true|false uri1 uri2... — Crea NUEVA + elimina vieja
just playlist-search "término" track                      — Buscar tracks
just playlist-tracks <id>                                 — Listar tracks
just playlist-delete <id>                                 — Eliminar playlist (unfollow)
```

**⚠️ Limitación crítica de la API:** No se puede modificar/limpiar tracks de una
playlist existente. `DELETE /items` devuelve 400/403. El comando `upload` crea
una playlist **nueva** cada vez (la URL cambia). `DELETE /items` con `{"uris":[]}`
no funciona — tampoco `DELETE /tracks` con `{"tracks":[...]}`. La única forma
de "actualizar" tracks es: crear nueva → añadir tracks → unfollow vieja.

Ver `scripts/spotify-playlist.ps1` para más operaciones.
