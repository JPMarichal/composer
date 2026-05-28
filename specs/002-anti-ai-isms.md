# Especificación: Safeguards Anti-AI en Composición Lírica

Basado en Wikipedia:Signs of AI writing (WikiProject AI Cleanup), repositorios humanizer/blader y avoid-ai-writing/conorbronsdon.

## Problema

La canción "Velocidad Cero" sonó a IA. Identificar y corregir los patrones que delatan origen sintético.

## Patrón sintético vs. humano

| Marca de IA                                                 | Por qué delata                                               | Alternativa humana                            |
| ----------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| Parallel negation ("no sé... no puedo... no tengo...")      | Simetría perfecta que la IA replica por defecto              | Alternar afirmación y negación                |
| Rule of threes (sustantivo, sustantivo, sustantivo)         | La IA tiende a ternarios automáticos                         | Binarios + ruptura                            |
| Em dash consecutivo (—)                                     | Casi inexistente en lírica real; la IA lo usa como coletilla | Punto, coma, nada                             |
| Inflated symbolism ("no es X, es Y")                        | Estructura favorita de la IA para dar "profundidad"          | Decir directamente                            |
| Rima consonante perfecta sostenida                          | La IA rima perfecto por defecto                              | Rima asonante o libre                         |
| Metáfora sobre-explicada                                    | La IA explica su propia metáfora en el mismo verso           | Dejar respirar la imagen                      |
| Imágenes genéricas ("la noche", "el silencio", "la ciudad") | Sin anclaje sensorial concreto                               | Olor, temperatura, textura, color específico  |
| Sintaxis perfecta sin coloquialismos                        | La IA evita contracciones y vulgarismos                      | "pa'", "na'", "tó", "vete", "dame"            |
| Adjetivos sobre verbos                                      | La IA describe más que narra                                 | Acción sobre adjetivo                         |
| Segunda persona distante ("tú", "usted")                    | La IA prefiere la generalización                             | Primera persona vulnerable ("yo", "me", "mí") |

## Safeguards cuantificables para el prompt

1. **30%+ rimas asonantes o libres** — contar sobre total de versos que riman
2. **Máximo 1 tríada (rule of threes) por canción**
3. **0 em dashes consecutivos** — cero uso de — como recurso
4. **≥1 coloquialismo por estrofa** — contracciones, vulgarismos, muletillas
5. **≥1 verso con métrica quebrada** — sílaba de más o de menos voluntaria
6. **No etiquetar figuras retóricas** — no escribir "una metáfora", usarla
7. **Detalles sensoriales concretos (olor, temperatura, textura)** — al menos 1 por estrofa
8. **Verbos de acción sobre adjetivos** — proporción ≥2:1 verbos/adjetivos
9. **1 imagen absurda o surrealista por canción** — algo que no encaje del todo

## Instrucción para el modelo

```
{
  "Anti_AI_Safeguards": true,
  "Verification": "Contra cada verso, marcar si viola algún safeguard. Si ≥2 violaciones, rehacer.",
  "Rules": [
    "30%+ rimas asonantes o libres",
    "Máximo 1 tríada por canción",
    "0 em dashes consecutivos",
    "Al menos 1 coloquialismo por estrofa",
    "Al menos 1 verso con métrica quebrada",
    "No etiquetar figuras retóricas",
    "Usar detalles sensoriales concretos (olor, temperatura)",
    "Preferir verbos de acción sobre adjetivos",
    "Incluir una imagen absurda o surrealista"
  ]
}
```

## Validación post-generación

```js
function validate(song) {
  return {
    asonantesOK: asonantes(song) / totalRimas(song) >= 0.3,
    sinEmDash: !song.includes("—"),
    triadas: countTriadas(song) <= 1,
    coloquialismos: coloquialismos(song) >= estrofas(song),
    metricaQuebrada: countMetricaQuebrada(song) >= 1,
    proporcionVerbos: verbos(song) / adjetivos(song) >= 2,
    imagenAbsurda: countAbsurdo(song) >= 1,
  };
}
```
