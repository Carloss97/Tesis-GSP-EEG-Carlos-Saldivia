# SELECTIONS README — It05/It20 (B1–B4; it1–it150; umbrales 5% / 20%)

Objetivo
- Documentar y reproducir el flujo usado para seleccionar combinaciones (combo = `graph|method`) a partir de la agregación multicriterio de los experimentos (it05 + it20 y reruns).

Entradas principales
- `experiments/analysis_it05_it20_multicriteria_agg.csv` — agregación multicriterio (salida de `analyze_it05_it20_multicriteria.ps1`).
- `results/it05_all_datasets_raw.csv` — resultados por dataset/seed para it05.
- `results/it20_synthetic_alpha_high_missing_raw.csv` — resultados por dataset/seed para it20.

Scripts usados
- `experiments/analyze_it05_it20_multicriteria.ps1` — genera la agregación multicriterio con las secciones B1..B4.
- `experiments/filter_and_export_compact.ps1` — aplica umbrales y exporta CSV/JSON/MD compactos. (Se ejecutó durante esta sesión.)

Resumen del procedimiento
1) Generación de agregados (B1–B4)
   - Ejecutar `analyze_it05_it20_multicriteria.ps1` para producir `analysis_it05_it20_multicriteria_agg.csv` y las recomendaciones por criterio.
   - Criterios (B1–B4) usados en el agregado:
     - B1 — `mean_based`: ordena por `mean_mae` (valor medio de error), favorece valores bajos.
     - B2 — `real_only_mean`: igual que B1 pero sólo usando datasets reales (ignora sintéticos).
     - B3 — `median_based`: usa `median_mae` (robusto frente a outliers).
     - B4 — `stability_first`: prioriza baja `std_mae` (consistencia), luego `mean_mae`.

2) Filtrado por umbrales (ejecutado aquí)
   - Script: `filter_and_export_compact.ps1` (ubicado en `experiments/`).
   - Umbrales por defecto aplicados en el script actual:
     - Filtro A: `median_mae < 0.05` (5%) y `datasets_count >= 3`.
     - Filtro B: `mean_mae < 0.05` (5%) y `real_obs_count >= 3`.
   - Salidas producidas:
     - `experiments/filtered_threshold_median.csv`
     - `experiments/filtered_mean_realobs.csv`
     - `experiments/filtered_selections.json`
     - `experiments/filtered_selections_compact.md`

3) Aplicar un cutoff alternativo (20%)
   - Para ejecutar con cutoff 0.20 (20%), edita `filter_and_export_compact.ps1` y cambia `\$th_med` y/o `\$th_mean` a `0.20`, luego vuelve a ejecutar el script.

4) Alcance `it1–it150`
   - El flujo es el mismo si tus CSV de entrada contienen iteraciones `it1`..`it150` (fusiona o ajusta las entradas para incluir esas iteraciones antes de generar la agregación).
   - Si necesitas, puedo generar un script auxiliar para combinar `results/it*.csv` en un agregado único y re-ejecutar el análisis automáticamente.

Comandos reproducibles
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "Thesis-Copilot-Toolkit\experiments\analyze_it05_it20_multicriteria.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "Thesis-Copilot-Toolkit\experiments\filter_and_export_compact.ps1"
```

Notas y recomendaciones
- Los umbrales afectan cobertura: umbrales más estrictos (p.ej. 0.05) reducen el número de combos seleccionados. Revisa `filtered_selections_compact.md` para una vista legible.
- Si quieres que ejecute automáticamente versiones con ambos cutoffs (0.05 y 0.20) y te deje los CSV/MD separados, indícamelo y lo automatizo.

Archivos relevantes (ubicación relativa)
- `experiments/analysis_it05_it20_multicriteria_agg.csv`
- `experiments/filtered_threshold_median.csv`
- `experiments/filtered_mean_realobs.csv`
- `experiments/filtered_selections.json`
- `experiments/filtered_selections_compact.md`

Contacto/Próximo paso
- He generado las exportaciones por defecto. ¿Quieres que lance ahora la variante con cutoff 0.20 y deje otro conjunto de archivos resultado? 
