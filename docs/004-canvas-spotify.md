# Canvas para Spotify

## Objetivo

Documentar criterios tecnicos y creativos para crear Canvas efectivos en Spotify, con enfasis en loops verticales generados o refinados con herramientas como CapCut/Seedance.

## Conclusión ejecutiva

Un Canvas efectivo no es un mini videoclip ni un anuncio. Es una unidad visual breve, silenciosa y repetible que amplifica el clima emocional de una cancion mientras esta suena.

La regla dominante es:

**una sola idea visual, movimiento sutil, loop limpio y coherencia con el universo del lanzamiento.**

## Especificaciones tecnicas consolidadas

Las fuentes revisadas repiten con alta consistencia este nucleo tecnico:

- **Duracion:** 3 a 8 segundos
- **Formato:** vertical 9:16
- **Resolucion:** minimo 720 px de alto
- **Resolucion recomendada de trabajo:** 1080 x 1920
- **Formato de archivo mas comun:** MP4
- **Comportamiento esperado:** loop visual continuo, sin corte brusco

> [!IMPORTANT]
> Aunque algunas fuentes de ayuda mencionan JPG en ciertos flujos de Canvas, para trabajo creativo con generacion de video conviene tratar Canvas como un loop MP4 vertical.

## Qué hace efectivo a un Canvas

### 1. Una sola idea visual clara

El Canvas funciona mejor cuando se puede resumir en una frase concreta:

- una mano soltando una cinta en el viento
- un cajon apenas abierto lleno de cartas
- dos personas casi mirandose sin llegar a tocarse
- una farola apagada con una ventana encendida al fondo

Si la idea necesita explicacion larga, normalmente ya es demasiado para 3-8 segundos.

### 2. Movimiento pequeno y legible

Las recomendaciones que mas se repiten favorecen:

- respiracion
- viento
- humo
- agua
- tela
- luces que palpitan
- microgestos
- paneos o dolly muy suaves

Y desaconsejan:

- muchos cortes
- camara nerviosa
- exceso de sujetos
- accion compleja
- coreografia narrativa en tan poco tiempo

### 3. Loop natural

Un buen Canvas no debe sentirse como un clip que "termina". Debe poder repetirse sin llamar la atencion sobre el empalme.

Las mejores estrategias de loop suelen ser:

- oscilaciones suaves
- luces ciclicas
- humo o niebla
- objetos suspendidos
- caminar que casi vuelve al mismo punto
- movimientos de camara muy cortos

> [!TIP]
> Si el plano no puede volver visualmente a un estado parecido al inicial, probablemente no es una buena idea de Canvas.

### 4. Foco visual unico

La atencion debe caer rapido sobre un solo sujeto, gesto u objeto emocional. Esto importa aun mas porque la interfaz de Spotify puede reducir legibilidad en los bordes.

Por eso conviene:

- mantener el foco principal centrado o dentro de la zona media
- evitar informacion critica pegada a los extremos
- no llenar el cuadro de elementos equivalentes compitiendo entre si

### 5. Coherencia con la cancion, no solo con la portada

El Canvas no debe ser solo una extension decorativa del arte de tapa. Debe representar la temperatura emocional del track:

- nostalgia
- desvelo
- deseo
- remordimiento
- reconciliacion
- liberacion

La pregunta correcta no es `¿que se ve bonito?`, sino `¿que imagen se quedaria viviendo con esta cancion?`.

## Qué evitar

Las fuentes consultadas y los snippets indexados coinciden especialmente en evitar:

- texto en pantalla
- subtitulos
- logos
- UI o elementos promocionales
- gestos de anuncio
- talking head innecesario
- bocas cantando, hablando o rapeando si no es una decision muy controlada
- caos visual
- simbolismo incomprensible
- loops con corte evidente

> [!WARNING]
> Un Canvas no debe sentirse como promo. Si parece una story de anuncio, pierde valor artistico y reduce inmersion.

## Recomendaciones especificas para generacion con IA

Cuando el Canvas se genera con IA, el mayor riesgo no es la falta de belleza sino la falta de control. Por eso conviene estructurar los prompts con cinco capas:

1. **Sujeto principal**
2. **Entorno concreto**
3. **Accion simple**
4. **Atmosfera emocional**
5. **Restricciones negativas**

Ejemplo estructural:

```text
A solitary figure under a dim streetlight, empty avenue before sunrise, slight coat movement in the wind, intimate regretful mood, vertical 9:16, seamless loop, no text, no logo, no lip-sync, no fast cuts.
```

## Recomendaciones operativas para CapCut / Seedance

- Usar `Text to Video`
- Fijar `9:16`
- Empezar con `6 s` o `8 s`
- Pedir varias variantes del mismo prompt
- Mantener movimiento bajo o medio-bajo
- Corregir una sola variable por iteracion

### Sufijo util para prompts

```text
vertical 9:16, 8-second seamless loop, cinematic, subtle motion, clear focal subject, no text, no subtitles, no logo, no watermark, no lip-sync, no talking to camera, no hard cuts, no chaotic motion
```

## Heuristicas practicas

### Si la generacion sale demasiado literal

- Quitar detalles narrativos secundarios
- Volver a un solo gesto o simbolo

### Si la generacion sale demasiado caotica

- Añadir `single subject`, `minimal movement`, `clean composition`

### Si el loop corta mal

- Pedir que el ultimo frame se parezca al primero
- Sustituir desplazamiento por oscilacion, luz, humo o respiracion

### Si las caras o labios salen raros

- Eliminar la accion facial
- Cambiar a siluetas, reflejos, manos u objetos

## Criterio de evaluacion posterior

Si se publican varios Canvas, conviene revisar si hay impacto en:

- saves
- shares
- playlist adds
- retencion subjetiva del loop
- coherencia de catalogo

No todo Canvas bonito sera util. El mejor suele ser el que permanece invisible como tecnica y muy presente como atmosfera.

## Referencias internas

- Ver tambien `docs/002-estrategia-promocion-spotify.md`
- Ver tambien `docs/003-pitch-editorial-spotify.md`

## Fuentes revisadas

### Locales

1. `docs/003-pitch-editorial-spotify.md`

### Web y snippets indexados

1. `support.spotify.com/us/artists/article/canvas-guidelines/`
2. `support.symdistro.com/hc/en-us/articles/360040227571-Spotify-Canvas`
3. `amuse.io/en/categories/how-to/promote-music/how-to-create-an-engaging-spotify-canvas/`
4. `identitymusic.com/blog/how-to-use-video-to-boost-engagement-on-spotify`
5. `a3tunes.com/blog/spotify-canvas-make-your-tracks-stand-out`

> [!NOTE]
> Parte del material oficial de Spotify no resolvio de forma limpia en el extractor web disponible en esta sesion, pero los snippets indexados y las fuentes de distribucion musical consultadas repitieron las mismas especificaciones y recomendaciones nucleares.