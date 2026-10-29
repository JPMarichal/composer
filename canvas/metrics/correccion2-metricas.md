# Métricas — segunda corrección (plano 3 de ambos Canvas)

Motivo: usuario detectó (tras el render) corbata ausente en el rostro de "Los postes de la calle central 2" y un farol flotante en la sirena de "Canto de sirena".

| Etapa | Tiempo |
|---|---|
| Regenerar s3_rostro (postes) | 60 s |
| Regenerar s3_sirena (sirena) | 60 s |
| Re-render de ambos videos (2 × ≈ 2–3 min, sin cronometrar por separado) | ≈ 4–5 min |
| Arranque de ComfyUI | ≈ 1 min |

Coste de la corrección: ≈ 7–8 min en total, evitable con la puerta de revisión (autorrevisión del agente + aprobación del usuario antes de renderizar), ahora en el paso 5b del skill. Los tiempos de re-render son estimados, no medidos con epoch.
