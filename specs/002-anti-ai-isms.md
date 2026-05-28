# Especificación: Safeguards Anti-AI en Composición Lírica

Basado en Wikipedia:Signs of AI writing (WikiProject AI Cleanup), repositorios humanizer/blader y avoid-ai-writing/conorbronsdon.

## Problema

La canción "Velocidad Cero" sonó a IA. Identificar y corregir los patrones que delatan origen sintético.

## Patrones detectados en la primera versión

| Patrón                  | Ejemplo en la canción                                          | Corrección                      |
| ----------------------- | -------------------------------------------------------------- | ------------------------------- |
| Inflated symbolism      | "no es X, es Y" implícito                                      | Decir directamente              |
| Parallel negation       | "no sé dónde pisar, no puedo respirar" encadenado              | Variar estructura               |
| Em dash overuse         | — usado 4+ veces                                               | Reemplazar con pausas naturales |
| Rule of threes          | "de acero y de cristal", "correr, gritar, avanzar"             | Romper la tríada                |
| Hedging                 | "casi", "quizás", "parece" ausente pero presente en estructura | Más contundencia                |
| Generic concrete        | "la ciudad", "el silencio" sin anclaje sensorial               | Detalles específicos            |
| Over-explained metaphor | Explicación retórica en el mismo verso                         | Dejar respirar la imagen        |
| Perfect rhyme           | Todas las rimas consonantes perfectas                          | Mezclar con asonantes           |

## Safeguards para el prompt del compositor

1. **Rima imperfecta**: Preferir asonante sobre consonante en al menos 30% de las rimas
2. **Detalles sensoriales concretos**: olor, temperatura, textura, color específico
3. **Coloquialismos y contracciones**: "pa'", "na'", "tó", "dame", "vete"
4. **Sintaxis rota**: Frases fragmentadas, asíndeton extremo, anacolutos
5. **Un verso imperfecto**: Una línea que voluntariamente "cojea" en métrica
6. **Sin etiquetas retóricas**: No nombrar la figura, usarla sin marcar
7. **Primera persona vulnerable**: "yo", "me", "mí", no "el alma", "el corazón"
8. **Una imagen absurda o extraña**: Algo que no encaje del todo (surrealismo)
9. **Menos adjetivos, más verbos**: Acción sobre descripción

## Instrucción para el modelo

```
{
  "Anti_AI_Safeguards": true,
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
