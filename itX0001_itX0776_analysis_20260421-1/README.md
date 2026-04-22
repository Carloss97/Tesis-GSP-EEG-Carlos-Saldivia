# Análisis de runs actuales (itX0001 a itX0776)

Este directorio contiene el análisis de los archivos generados por los runs actuales, bajo el patrón `itX0001_*`, `itX0002_*`, ..., `itX0776_*` en `Thesis-Copilot-Toolkit/results/`.

## Instrucciones

- El script `analisis_rerun_actuales.py` agrega y visualiza los resultados de los archivos de la serie `itX####_*`.
- Los resultados y figuras generadas aquí corresponden **solo** a los runs actuales, no a análisis previos ni a archivos unificados antiguos.

## Ejecución

```bash
python analisis_rerun_actuales.py
```

## Archivos procesados
- Todos los archivos `itX####_raw.csv`, `itX####_significance.csv`, `itX####_stats.csv`, `itX####_run_metadata.json`, etc.

## Salidas
- Figuras comparativas (boxplots de MAE y SNR por método y dataset, excluyendo outliers extremos para mejor visualización).
- Tablas resumen de mejores métodos por dataset (top 3, expandido a top 6 si hay baseline en el top 3, garantizando al menos 3 no baseline).
- Tabla y análisis de combinaciones dataset-grafo-método cuando corresponda.
- Reporte de mejores métodos y combinaciones.

## Criterios de visualización y reporte
- Los boxplots de MAE y SNR excluyen outliers extremos para que la escala del eje y permita comparar los métodos relevantes.
- El top de métodos por dataset se expande a top 6 si hay métodos baseline en el top 3, para mostrar siempre al menos 3 métodos no baseline.
- Se incluye análisis de combinaciones dataset-grafo-método si la estructura de los datos lo permite.

---

> Actualizado automáticamente el 2026-04-21.