# Análisis y procesos realizados — Resumen operativo

Este documento resume las acciones y criterios que se aplicaron hasta llegar a los resultados actuales (análisis de `it05` y `it20`), incluyendo la generación de mapeos, el monitoreo de progreso, y los criterios usados para seleccionar combinaciones candidatas.

## Objetivo
- Re-ejecutar/validar `LT20` y producir un análisis comparativo entre `it05` e `it20`.
- Seleccionar al menos 3 combinaciones por cada clase (generalistas, variantes temporales, instantáneas) y comparar contra baselines.
- Producir entregables: CSV agregados, JSON de recomendaciones y un resumen en Markdown.

## Artefactos generados (ubicación)
- `Thesis-Copilot-Toolkit/experiments/analysis_it05_it20_multicriteria_agg.csv` — métricas agregadas por `combo` (it05+it20).
- `Thesis-Copilot-Toolkit/experiments/analysis_it05_it20_multicriteria_recommendations.json` — recomendaciones por criterio.
- `Thesis-Copilot-Toolkit/experiments/analysis_it05_it20_multicriteria.md` — resumen legible con top candidatos por criterio.
- `Thesis-Copilot-Toolkit/experiments/ANALYSIS_PROCESS.md` — este documento (explicación del procedimiento).

## Línea temporal y acciones principales
1. Diagnóstico: se identificaron problemas de *dataset-name mismatches* entre runner y engine, motivo por el que algunas ejecuciones no casaban con los nombres esperados.
2. Implementación del *mapping proposer* y runner-wrapper: heurísticas de alias y fallback a synthetic/forced cuando no hay match.
3. Ejecución light-mode de pruebas mapeadas (LT20 ligero) para validar mapeos y parámetros.
4. Implementación del *progress monitor* y scripts PowerShell robustos (`count_reruns2.ps1`, `check_ids.ps1`) para contar DONE/MISSING y tail de logs.
5. Lanzamiento de re-ejecuciones (reruns) y almacenamiento en `results/` — se produjeron artefactos rerun_0..rerun_208.
6. Creación de scripts de análisis (`analyze_it05_it20.ps1` y versión multicriterio `analyze_it05_it20_multicriteria.ps1`) para agregar métricas y seleccionar candidatos.

## Notas sobre iteraciones y convenciones (it1..it150)
- En la campaña se trabajó con iteraciones numeradas; el resumen histórico relevante:
  - it1..it60: fases iniciales con proxies y tests sintéticos/real.
  - it61..it100: validaciones cross-dataset y calibraciones.
  - it101..it150: corridas de validación finales y comparación entre métodos (esta numeración se usa como referencia operativa para agrupar experimentos).
- En la práctica, el análisis actual agrupa y toma resultados de `it05` e `it20` (nombres de artefactos CSV presentes en `results/`).

## Definición de "B1–B4" (agrupaciones usadas en informes)
Para mantener trazabilidad en los informes y en la selección, se usan las siguientes bandas lógicas (B1–B4):
- B1 — Baselines: métodos triviales/comunes (`mean`, `nearest`, `linear`).
- B2 — Métodos instantáneos / espaciales: interpoladores que no usan dinámica temporal explícita (p. ej. `gsmooth`, `nnk`, `kalofolias` cuando aplican por sample).
- B3 — Métodos temporales / variantes en el tiempo: métodos que explotan dependencia temporal o regularización TV temporal (p. ej. `heat_diffusion_temporal`, `spline_temporal`, `temporal_laplacian`).
- B4 — Métodos híbridos/avanzados: combinaciones o métodos entrenables/iterativos tipo `trss`, `tv` con ajustes complejos.

> Estas etiquetas son agrupaciones lógicas para el informe; los nombres concretos de métodos provienen de las columnas `graph` y `method` en los CSV de `results/`.

## Nota sobre normalización en el análisis

Antes de agregar resultados o calcular rankings multicriterio, verifique el campo `normalization` en cada `*_run_metadata.json`. Solo agregue y compare ejecuciones que compartan el mismo valor de `normalization` (o `null`). Mezclar normalizaciones diferentes conducirá a comparaciones no válidas de métricas absolutas. Consulte `../docs/normalization_and_dataset_policy.md` para la convención de metadatos y ejemplos.

## Umbrales y cortes referenciados ("<5" y "<20")
En informes y cortes rápidos se usan filtros por error/MAE y por cobertura:
- `<5` y `<20` se usan como ejemplos de umbrales para candidaturas (p. ej. seleccionar combos con MAE < 0.05 o < 0.20 según la métrica y la escala del dataset). En este análisis se priorizaron comparaciones relativas (ordenamiento por métricas) más que umbrales hard-coded, pero los scripts dejan fácil parametrización para aplicar dichos cortes.

## Criterios multicriterio aplicados (lo ejecutado ahora)
Se calcularon y compararon las combinaciones (combos = `graph|method`) usando cuatro criterios representativos:

1. `mean_based` — ranking por `mean_mae` combinado con `std` (metodología original: `mean + 0.5*std`).
2. `real_only_mean` — igual que `mean_based` pero computado solo con registros de datasets reales (se excluyen filas cuyo dataset empieza por `synthetic`).
3. `median_based` — ranking por mediana de MAE (robusto frente a outliers).
4. `stability_first` — prioridad a la robustez: ranking por `mean + std` (penaliza alta varianza).

Para cada criterio se seleccionaron: Top-3 generalistas (presencia mínima de datasets), Top-3 temporales, Top-3 instantáneos y resumen de baselines.

## Cómo reproducir (comandos)
En el root del repositorio (ruta desde la que trabajamos):

```powershell
# Ejecutar análisis multicriterio (ya creado y probado)
powershell -NoProfile -ExecutionPolicy Bypass -File "Thesis-Copilot-Toolkit\experiments\analyze_it05_it20_multicriteria.ps1"
```

Los archivos resultantes estarán en `Thesis-Copilot-Toolkit/experiments/`.

## Observaciones y siguientes pasos sugeridos
- Si quieres cortes por umbral (`<5` o `<20`) explícitos, lo añado como criterio adicional y re-ejecuto (p. ej. filtrar combos cuya median_mae < 0.05).
- Si prefieres usar solo `it05` o solo `it20` (no combinados), lo parametrizo.
- Puedo preparar un CSV/Markdown listo para pegar en la sección de resultados del informe (versión compacta con: combo, criterio, mean, median, std, top-datasets).

---
Documento generado automáticamente para trazabilidad de experimentos.
