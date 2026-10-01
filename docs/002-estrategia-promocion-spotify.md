# Estrategia de Promoción en Spotify

## Regulación y TOS

### Lo que NO está permitido (viola TOS de Spotify)
- **Manipulación artificial de streams** — bots, playlists falsas, intercambio de streams
- **Pagar por colocación en playlists** — servicios de "payola" que prometen posiciones editoriales
- **Comprar seguidores o streams** — cualquier servicio de métricas fraudulentas
- **Usar datos de Spotify for Artists fuera de la plataforma** — los analytics no se pueden redistribuir
- **Automatizar interacciones** — seguir/dejar de seguir en masa, dar like automatizado

### Lo que SÍ está permitido
- **Crear playlists propias** con tu música mezclada con artistas similares (TOS-compliant)
- **Promocionar en redes sociales** tus playlists propias (Instagram, TikTok, Twitter, Facebook)
- **Anuncios pagados** (Meta Ads, Google Ads) dirigiendo a tu perfil/playlists
- **Discovery Mode** — programa oficial de Spotify donde reduces royalty rate a cambio de recomendación algorítmica
- **Editorial pitch** — enviar canciones no lanzadas a los editores de Spotify via Spotify for Artists
- **Colaboración con playlisters legítimos** — contactar curadores reales, no servicios automáticos

## Estrategia de Curación

### Playlists propias para promoción
- **Regla 90/10**: ~90% de artistas establecidos + ~10% de música propia
- **Coherencia temática**: cada playlist debe tener un género/estado de ánimo/contexto claro
- **Actualización semanal**: playlists estáticas pierden tracción algorítmica
- **Título descriptivo**: nombres que la gente busca realmente (no títulos poéticos crípticos)
- **Descripción útil**: explicar qué contiene y para qué momento escucharla
- **Portada atractiva**: imagen coherente con el tema

### Qué playlists valen la pena
| Tipo | Valor | Ejemplo |
|------|-------|---------|
| Catálogo propio | Alto | "Canciones de JPMarichal Playlist" |
| Curatorial temática | Medio-Alto | "Major Tom Biographical History" |
| Shazam sincronizada | Bajo | "Mis pistas en Shazam" (autogenerada, sin curaduría) |
| Generada por herramienta | Cero/Negativo | Chosic (~100 tracks idénticos) |
| Homenaje a un artista | Bajo | "Miguel Bosé", "The Beatles" (0 seguidores) |

### Señales de alerta (playlists que NO aportan)
- 0 seguidores después de meses
- Track count exacto y redondo (100, 101, 102 — sugiere generación automática)
- Descripciones vacías o idénticas entre playlists
- Sin coherencia temática real
- Creadas en lote el mismo día

## Restricciones del API Pública

### Lo que SÍ puedes medir
- Seguidores por playlist
- Total de tracks
- Contenido (qué canciones, de quién)
- Visibilidad (pública/privada)

### Lo que NO puedes medir (solo Spotify for Artists)
- Save rate / skip rate por track
- Source of Streams (cómo llegó el oyente)
- "Discovered On" (qué playlist generó el stream)
- Crecimiento histórico de seguidores
- Demografía de oyentes
- Tiempo de escucha por sesión

### Implicación estratégica
Sin los datos de engagement, no puedes auditar playlist por "efectividad real" desde el API. Las decisiones de qué playlists mantener se basan en:
1. **Seguidores** (>0 es mejor que 0)
2. **Propósito curatorial** (¿tiene una razón de existir?)
3. **Contenido propio** (¿incluye tu música?)

## Arquitectura de Promoción

### Canales
1. **Playlists propias** (control total, sin costo)
2. **Redes sociales** (orgánico + ads → perfil de Spotify)
3. **Editorial Pitch** (Spotify for Artists, 7 días antes del lanzamiento)
4. **Discovery Mode** (programa oficial, reduce royalty rate)
5. **Collaborative playlists** (seguidores pueden añadir → más engagement)

### Ciclo semanal recomendado
- Lunes: refrescar playlist principal (rotar ~20% del contenido)
- Martes: compartir en stories/redes
- Miércoles: revisar métricas de Spotify for Artists
- Jueves: buscar colaboraciones con otros artistas independientes
- Viernes: promover el fin de semana (playlists para conducción/fiesta/relax)

### Anti-patrones
- **Crear 50 playlists idénticas con Chosic** → 0 seguidores, perfil parece spam
- **Meter toda tu música en 20 playlists diferentes** → canibalización
- **No actualizar nunca** → el algoritmo entierra playlists estáticas
- **Títulos en otros idiomas sin audiencia en ese idioma** → nadie las busca
