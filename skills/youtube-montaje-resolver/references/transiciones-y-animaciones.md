# DaVinci Resolve: inventario de transiciones y animaciones

Documento de referencia para el montaje de los videos del canal. Se elaboró el 2026-11-13 a partir del **manual oficial de Blackmagic (DaVinci Resolve 18, capítulos 46 a 53)**, descargado de un espejo en PDF y leído como texto, más guías de terceros para lo que el manual no precisa (gratis frente a Studio, Resolve 20 y 21).

**Límites de esta fuente.** El manual es de la versión 18 y en el equipo está instalada la 21 (gratuita): puede haber transiciones nuevas o cambios de nombre que no constan aquí. Las transiciones integradas no se pueden listar desde los archivos instalados (están dentro del programa), así que el inventario definitivo de tu versión se confirma en *Edit > Effects Library > Toolbox > Video Transitions*. Lo marcado como **[verificar]** no está confirmado.

Fuentes principales:
- Manual de referencia de DaVinci Resolve 18, capítulos 46 a 53 (Efectos y transiciones): https://ltbits.github.io/davinci-resolve-manuals/DR18/DR18-RM06-EditingEffectsAndTransitions.pdf
- Guía actualizada a Resolve 21.0.1 (transiciones, ajustes y Smooth Cut): https://tryuncle.com/learn/davinci-resolve/transitions
- Guía con las categorías y los efectos de Resolve FX: https://davinciresolveclub.com/davinci-resolve-transitions/
- Comparación gratuita frente a Studio: https://www.toolfarm.com/tutorial/in-depth-davinci-resolve-studio-vs-the-free-version/

---

## 1. Cómo se usan las transiciones

**Dónde están:** Edit > Effects Library > Toolbox > Video Transitions (en la página Cut, pestaña Transitions). Hay una carpeta *Favorites* y una *User* con tus presets.

**Cómo se aplican**
- Arrastrar la transición a un punto de corte (queda centrada, o al inicio o al final del corte).
- Doble clic en la transición: la aplica al corte indicado por el playhead.
- Seleccionar uno o varios cortes (tecla V para elegir el corte más cercano al playhead) y pulsar **Ctrl+T** (Cmd+T en Mac): añade la transición estándar de video y audio. **Alt+T**: solo video. **Shift+T**: solo audio. La tecla **U** cambia entre inicio, centro y fin del corte antes de aplicarla.
- Clic derecho sobre un corte: elegir una duración (un cuarto de segundo, medio, uno o dos).
- Clic derecho sobre una transición del Effects Library: *Add to Selected Edit Points* (a muchos cortes a la vez).
- Pegar la misma transición en muchos cortes: copiar la transición, mantener Ctrl y seleccionar los cortes, pegar.
- Para crear la superposición arrastrando: Alt+Shift y arrastrar un clip sobre otro.

**Requisito:** los dos clips necesitan **material extra (handles)** más allá del punto de corte. Con imágenes fijas no hay problema (se pueden alargar); si falta, Resolver ofrece *Trim Clips*, *Skip Clips* o cancelar.

**Duración estándar:** 1 s por defecto (Preferences > User > Editing > Standard transition duration). La transición estándar se cambia con clic derecho > *Set as Standard Transition*.

**Previsualizar:** con *Hover Scrub Preview* activado, al pasar el puntero por una miniatura se ve el efecto con los dos clips junto al playhead.

### Propiedades comunes en el Inspector (doble clic sobre la transición)
| Parámetro | Qué hace |
|---|---|
| Transition Type | Cambia a cualquier otra transición instalada. |
| Duration | En segundos o cuadros. |
| Alignment | *Start on Edit*, *Center on Edit* (por defecto) o *End on Edit*. |
| Style | (solo disoluciones) Video, Film, Additive, Subtractive, Highlights, Shadows. |
| Start Ratio / End Ratio | Porcentaje de avance al primer y último cuadro (0 a 100 %). |
| Reverse | Invierte el sentido (no disponible en disoluciones). |
| Ease | None, In, Out, In & Out, Custom: inercia no lineal. |
| Transition Curve | Curva de keyframes que reajusta el tiempo de la transición. |

**Estilos de la disolución cruzada:** *Video* (lineal), *Film* (logarítmica, como copiadora óptica), *Additive* (aclara a la mitad), *Subtractive* (oscurece a la mitad), *Highlights* (modo Lighten: realza lo claro), *Shadows* (modo Darken: realza lo oscuro).

**Editar la curva:** botón en la esquina inferior derecha de la transición, luego el Curve Editor. Con interpolación Bezier se logran inicios lentos y finales rápidos, o al revés. El punto blanco arriba a la izquierda apaga la curva sin quitar la transición.

**Presets propios:** clic derecho en una transición ajustada > *Create Transition Preset* (se guarda en *User*, y es lo único que se puede borrar).

**Convertir a Fusion:** clic derecho > *Convert to Fusion Cross Dissolve*, luego *Open in Fusion Page* para rehacerla con nodos.

---

## 2. Inventario de transiciones de video (manual oficial)

Todas las de bordes (iris, wipes, shape, motion) comparten: **Color** y **Border** (grosor del borde en píxeles, 0 sin borde), **Feather** (suaviza el borde), **Reverse**. Las de *Motion* añaden **Motion Blur**.

### 2.1 Dissolve (6)
| Transición | Parámetros propios |
|---|---|
| **Cross Dissolve** | Style (6 estilos), Start/End Ratio, Reverse. Es la estándar. |
| **Additive Dissolve** | Style, Start/End Ratio, Reverse. |
| **Non-Additive Dissolve** | Start/End Ratio, Reverse. |
| **Dip to Color Dissolve** | Color del punto medio, Start/End Ratio, Reverse. |
| **Blur Dissolve** | Horizontal y Vertical Strength (desenfoque en X e Y), Start/End Ratio, Reverse. |
| **Smooth Cut** | Mode: *Better* (por defecto, conserva el movimiento) o *Faster*. Solo sirve para disimular saltos en entrevistas o planos de cabeza. Mejor en 2 a 6 cuadros. Según una guía, el modo *Better* usa Speed Warp, función de **Studio** **[verificar]**. |

### 2.2 Iris (9)
Parámetros comunes: Color, Border, Offset to Center, Feather, Reverse; casi todos añaden Aspect Ratio y Rotation.
| Transición | Presets |
|---|---|
| Arrow Iris | Arrow Up, Down, Left, Right |
| Cross Iris | (sin presets) |
| Diamond Iris | (sin presets) |
| Eye Iris | (sin presets; sin Offset ni Rotation) |
| Hexagon Iris | Hexagon, Hexagon Vertical |
| Oval Iris | Oval Ratio (ancho o alto) |
| Pentagon Iris | Pentagon Up, Pentagon Down |
| Square Iris | Square Flat, Square Point |
| Triangle Iris | Triangle Up, Bottom, Left, Right |

### 2.3 Motion (4)
| Transición | Presets y notas |
|---|---|
| **Barn Door** | Barn Door Vertical, Barn Door Horizontal |
| **Push** | Push Left, Right, Up, Down |
| **Slide** | Slide Left-Right, Right-Left, Bottom-Up, Top-Down, Top-Left, Bottom-Right; parámetro *Direction* (entra el clip nuevo o sale el viejo) |
| **Split** | Parte la imagen y la abre |

### 2.4 Shape (5)
| Transición | Presets |
|---|---|
| Box | Upper Left, Upper Right, Lower Left, Lower Right, Left Center, Top Center, Right Center, Bottom Center |
| Heart | Aspect Ratio, Offset, Rotation |
| Star | 4-Point, 5-Point, 6-Point |
| Triangle Left | (sin presets) |
| Triangle Right | (sin presets) |

### 2.5 Wipe (8)
| Transición | Presets y notas |
|---|---|
| Band Wipe | Horizontal, Vertical, Horizontal Bilinear, Vertical Bilinear |
| Center Wipe | Angle |
| Clock Wipe | Angle, Clockwise |
| Edge Wipe | Angle |
| Radial Wipe | (sin presets) |
| Spiral Wipe | (sin presets) |
| Venetian Blind Wipe | Repeat (número de persianas), Angle |
| X Wipe | (sin presets) |

(Algunas guías de terceros omiten Center Wipe; el manual oficial sí lo incluye.)

### 2.6 Fusion Transitions (23 en el manual de la versión 18; 29 contando las 4 direcciones de Pan y de Slide)
Transiciones hechas con Fusion, con parámetros propios en el Inspector. Clic derecho > *Open in Fusion Page* para ver los nodos. Se pueden crear las tuyas guardando un macro en la carpeta de plantillas de Fusion.

| Transición | Qué hace | Parámetros |
|---|---|---|
| Brightness Flash | Sube el brillo hasta un destello al pasar | Brightness, Saturation |
| Camera Shake | Sacudida con separación de canales de color | Shake Speed, Shake Strength, Contrast, Brightness, Saturation |
| Circles | Círculos concéntricos | Circle Color, Red, Green, Blue, Alpha, Circle Thickness |
| Crash Zoom | Dos acercamientos rápidos | (sin parámetros) |
| Cross Dissolve | Disolvencia base para crear la tuya | (sin parámetros) |
| Drop Warp | Gota de agua que deforma | Warp Scale |
| Fall and Bounce | El clip entrante cae y rebota | Fall Angle |
| Film Strip | Zoom sobre una tira de película | Color, Red, Green, Blue, Alpha |
| Flip 3D | Giro entre las dos caras de un plano | (sin parámetros) |
| Foreground Wipe | Columna ampliada que barre | Invert Wipe, Shadow Softness, Border Width |
| Glitch | Rotura digital (solo en pocos cuadros) | (sin parámetros) |
| Noise Dissolve | Disolución con ruido de Fusion | Mix, Type, Softness, Animation, Border |
| Paint On | Pinceladas de pintura (mejor largas) | Shadow Blend |
| Pan (Down, Left, Right, Up) | Imágenes en espejo en movimiento | según la dirección |
| Rotate | Giro de 180° con disolvencia | (sin parámetros) |
| Rotate 90 | Giro de 90° con disolvencia | (sin parámetros) |
| Round and Down | Giro alrededor de un pivote mientras disuelve | (sin parámetros) |
| Slice Push | Varias columnas que empujan | Slices, Angle, Shadow, Shadow Softness, Shadow Offset |
| Slide (Down, Left, Right, Up) | Deslizamiento en espejo | Curve: Linear, Easing, Custom |
| Tunnel of Light | El primer clip se absorbe en un punto y el segundo sale de él | Contrast, Glow Gain, Glow Size, Glow Red, Green, Blue |
| Warp | Torbellino como agua por un desagüe | (sin parámetros) |
| Zoom In | Acerca y mezcla | Zoom Scale (negativo aleja), Zoom Center, Curve |
| Zoom In and Out | Acerca el primero y aleja el segundo | Zoom Scale, Zoom Center |

### 2.7 Otros tipos
- **Resolve FX Transitions** (más pesadas de procesar): *Burn Away* (película que se quema). Controles: Motion (Directional, Hotspots con 1 a 8 puntos, Path con 2 a 5 puntos), Angle, Adjust Start/End, Raggedness, Scale, Melt, Char, Burn, Burn Hue/Sat/Brightness, Glow Brightness/Spread, Ash. Si requiere Studio, **[verificar]**.
- **DCTL Transition:** transiciones programadas con DaVinci Color Transform Language (para desarrolladores).
- **OpenFX Transitions:** aparecen en el panel OpenFX si se instalan plugins de terceros.
- **User Transitions:** tus presets guardados.
- **Audio Transitions:** *Cross Fade 0 dB* (lineal), *Cross Fade -3 dB* (baja el nivel en el cruce), *Cross Fade +3 dB* (lo sube).

**Gratis frente a Studio:** según las fuentes, las transiciones de las categorías anteriores (Dissolve, Iris, Motion, Shape, Wipe, Fusion Transitions) están en la versión gratuita. Lo que depende de Studio en torno a transiciones es **Smooth Cut en modo Speed Warp** y los efectos ResolveFX avanzados **[verificar con el instalado]**.

---

## 3. Mapa para nuestras canciones (columna «Transición» de `PLAN.md`)

| En el plan | En Resolver | Cómo |
|---|---|---|
| Disolvencia | **Cross Dissolve** (estilo Video, o Film para más suavidad) | Ctrl+T; 0,5 a 1 s |
| Zoom cruzado | **Fusion Transitions > Zoom In and Out** (o *Zoom In*) | Zoom Scale bajo para que sea sutil |
| Desenfoque | **Blur Dissolve** | Horizontal/Vertical Strength moderado |
| Cortina suave | **Edge Wipe** con *Feather* activado, o **Band Wipe** | 0,6 a 1 s |
| Empuje hacia arriba | **Push Up** (Motion) | Motion Blur activado |
| Corte con destello (3 a 4 cuadros) | **Fusion Transitions > Brightness Flash** (3 a 4 cuadros) | Brightness alto, Saturation baja |
| Disolvencia final o a negro | **Dip to Color Dissolve** (negro) | Duración larga, 2 a 3 s |

Aviso: el FCPXML que genera el skill **no incluye transiciones** (solo cortes duros). Para meterlas por XML habría que añadir `<transition>` con efectos que Resolver reconozca; solo es seguro para *Cross Dissolve* **[no probado]**. Lo práctico es aplicarlas en Resolver con Ctrl+T o copiando una transición a muchos cortes.

---

## 4. Animación

### 4.1 Keyframes en el Inspector (Edit y Cut)
- Casi todos los parámetros del Inspector se animan con el **rombo gris** a la derecha del control; se vuelve naranja con el playhead sobre un keyframe. Con un keyframe ya puesto, cualquier cambio en otro cuadro crea uno nuevo. Mínimo dos para animar.
- Botones: anterior, crear o borrar, siguiente. Atajos de teclado: corchetes para saltar entre keyframes.
- **Interpolación** (clic derecho en el rombo naranja): *Linear*, *Ease In*, *Ease Out*, *Ease In and Out*.
- **Keyframe Editor:** *Clip > Show Keyframe Editor* (Mayús+Cmd+C). Muestra una pista por grupo (Transform agrupa Pan, Tilt, Zoom, Rotación y Anchor) que se puede desplegar parámetro por parámetro.
- **Curve Editor:** *Clip > Show Curve Editor* (Mayús+C). Cuatro botones de interpolación Bezier arriba. Opción-clic añade un punto.
- Borrar: reset junto al parámetro (uno), o junto al título del grupo (todos).
- Un grupo se enciende o apaga con el interruptor a la izquierda de su título.
- **Pegar atributos** (Alt+V): copia los keyframes con *Maintain Timing* o *Stretch to Fit*. Con varios clips seleccionados, el Inspector edita todos a la vez (modificación relativa o valor igual).
- **Adjustment Clip:** capa de ajuste en Toolbox > Effects; aplica a todo lo que tiene debajo Resolve FX, Open FX, Composite, Transform, Cropping y Dynamic Zoom.

### 4.2 Parámetros animables del clip (Video Inspector)
**Composite:** Composite Mode (ver 4.3), Opacity.
**Transform:** Zoom X y Y (enlazables), Position X y Y, Rotation Angle, Anchor Point X y Y, Pitch, Yaw, Flip horizontal y vertical.
**Cropping:** Crop Left, Right, Top, Bottom, Softness.
**Dynamic Zoom:** panorámica y zoom de inicio a fin, con recuadro verde (inicio) y rojo (fin) en el visor. Parámetros: *Dynamic Zoom Ease* (**Linear, Ease In, Ease Out, Ease In and Out**) y *Swap* (invierte inicio y fin). Es la forma más rápida de hacer el efecto Ken Burns de nuestras imágenes. Se activa con el botón Transform/Crop/Dynamic Zoom al pie del visor.
**Stabilization:** Perspective, Similarity, Translation; Camera Lock, Zoom, Cropping Ratio, Smooth, Strength.
**Lens Correction (solo Studio):** Analyze, Distortion.
**Retime and Scaling:** Retime Process (Nearest, Frame Blend, Optical Flow), Motion Estimation, Scaling (Crop, Fit, Fill, Stretch), Resize Filter (Sharper, Smoother, Bicubic, Bilinear).
**Smart Reframe (solo Studio):** reencuadre automático a otras proporciones (por ejemplo de 16:9 a 9:16).

### 4.3 Modos de composición (Composite Mode)
Normal, Add, Color, Color Burn, Darken, Darker Color, Difference, Divide, Exclusion, Hard Mix, Hardlight, Hue, Lighten, Linear Burn, Linear Dodge, Linear Light, Luminosity, Multiply, Overlay, Pin Light, Screen, Softlight, Subtract, Vivid Light. Todos interactúan con Opacity. Utilidad para el canal: *Screen* o *Add* para destellos y partículas sobre una imagen.

### 4.4 Velocidad (Speed Effects)
- *Change Clip Speed* (porcentaje, cuadros por segundo o duración), *Reverse*, *Freeze Frame* (Mayús+R).
- **Retime Controls** (Cmd+R): rampas de velocidad variables dentro del clip.
- **Retime Curves:** dos curvas de velocidad.
- Velocidad y fps se pueden animar con keyframes.
- Audio: sin corrección de tono en Windows y Linux; el audio de rampas variables queda mudo.

### 4.5 Títulos y animación de texto
**Títulos básicos** (todos con texto enriquecido salvo Text+): *L Lower 3rd*, *M Lower 3rd*, *R Lower 3rd* (dos líneas, cada una con Position, Zoom y Rotación independientes), *Scroll* (créditos que suben; la duración del clip fija la velocidad), *Text*.
**Parámetros del texto enriquecido:** fuente, tipo, color, tamaño, tracking, interlineado, estilos (subrayado, tachado, superíndice, subíndice), mayúsculas (mixto, todo mayúsculas, todo minúsculas, versalitas, título), alineación, anclaje, Position, Zoom, Rotation. Además **Drop Shadow** (color, offset, blur, opacidad), **Stroke** (color, tamaño) y **Background** (rectángulo con color, contorno, ancho, alto, radio de esquina, centro, opacidad).
**Text+:** el generador de texto de Fusion en la página Edit; sin texto enriquecido (un solo estilo para todo), pero con paneles Text, Layout, Transform y Shading, **Write On / Write Off** animables, trazado sobre punto, cuadro, círculo o ruta, y transformaciones y animación por carácter, palabra o línea. Se puede abrir en Fusion y es etalonable como cualquier clip.
**Fusion Titles:** biblioteca de plantillas de texto ya animadas (por ejemplo lower thirds animados) con controles personalizados en el Inspector; son macros de Fusion. No hay una lista oficial completa en el manual: ver la lista real en *Effects Library > Titles*.
**Posición y animación:** todo título tiene los mismos grupos Composite, Transform y Cropping para animarlo con keyframes (entrada, salida, vuelo).
**Vista previa:** con *Hover Scrub Preview*, pasar el puntero por una miniatura reproduce la animación.
**Guardar un título:** arrastrarlo al Media Pool conserva sus keyframes.

### 4.6 Generadores
10 Step, 100mV Steps, BT.2111 Color Bar (HLG Narrow, PQ Full, PQ Narrow), EBU Color Bar, **Four Color Gradient** (degradado de cuatro colores animable), Grey Scale, SMPTE Color Bar, **Solid Color**, **Window**, YCbCr Ramp, y en *Fusion Generators* el ejemplo **Noise Gradient**. Solo Solid Color tiene parámetros propios; los demás aceptan Composite, Transform, Cropping y Dynamic Zoom.

### 4.7 Imágenes fijas
Una imagen fija entra al Media Pool con 10 s de duración y puede alargarse hasta 17 h 40 min. Formatos: TIF, PNG, JPG, DPX, EXR, DNG, TGA, HEIF, NEF, CR2, PSD. Tiene los mismos Composite, Transform, Cropping, Retime y Scaling que cualquier clip.

### 4.8 Resolve FX y Fusion
- **Resolve FX:** efectos con aceleración de GPU que se aplican a clips o capas de ajuste (desenfoques, color, luz, estilo, etc.). Parte de ellos son exclusivos de Studio; las guías mencionan ruido, desenfoques ópticos, grano de película, máscara mágica y reducción de ruido por IA. La lista exacta de la versión gratuita **[verificar con el instalado en Edit > Effects > Resolve FX]**.
- **Fusion page:** composición por nodos con keyframes, splines y modificadores; permite crear transiciones, generadores y títulos propios guardados como macros. Dentro de la versión gratuita casi todo está disponible; solo faltan algunas herramientas como Camera Tracker y VR Toolset (según una guía).

---

## 5. Recomendaciones para el canal

1. **Movimiento de las imágenes:** usar *Dynamic Zoom* con *Ease In and Out* en lugar de keyframes manuales de Transform; es lo más rápido para 60 imágenes y combina bien con el plan (zoom máximo ≈ 105 %).
2. **Transiciones:** definir una transición estándar con *Set as Standard Transition* (Cross Dissolve de 0,5 s) y aplicarla a todos los cortes con Ctrl+T, y reservar *Zoom In and Out*, *Push Up*, *Blur Dissolve* y *Brightness Flash* para los puntos del plan que las piden. Guardar cada ajuste como **Transition Preset**.
3. **Títulos:** probar *Text+* para letras con entrada suave (Write On o fundido por Opacity con keyframes); es más flexible que *Text*.
4. **Consistencia:** con varias imágenes seleccionadas, el Inspector aplica el mismo cambio a todas (Dynamic Zoom, Opacity, etc.).
5. **Pendiente de probar:** aplicar transiciones desde el XML, y confirmar en la versión 21 gratuita qué efectos Resolve FX están disponibles.
