# Bitácora de evidencia para capítulos 6--8

## Contribución práctica en una frase
TRSS mejora la reconstrucción de canales EEG ocultos frente a la interpolación estándar de MNE en métricas de amplitud y ajuste temporal, especialmente en regímenes difíciles, pero no domina la fidelidad espectral LSD y exige mayor tiempo de cómputo.

## Benchmark confirmatorio TRSS vs MNE
- **Fuente:** `results/trss_vs_mne_bads_extensive/derived_balanced.csv` y `robust_stats/robust_pairwise_summary.csv`.
- **Tamaño:** 100 estratos, 300 casos pareados y 3300 evaluaciones crudas; 2700 de ellas corresponden a variantes TRSS de grilla o perfiles alternativos.
- **Método de referencia:** `MNE interpolate_bads(method='spline')`.
- **Resultado principal TRSS fijo:** MAE mejora mediana 12.4% (IC95 7.8, 17.4), tasa de victoria 72.0%, qBH=1.03e-22.
- **NRMSE:** mejora mediana 13.9%, tasa de victoria 70.3%.
- **LSD:** mejora mediana -2.3%, tasa de victoria 40.7%; este resultado favorece a MNE y debe aparecer como caveat.
- **Tiempo:** mejora mediana -1004.1%; TRSS es más lento que MNE, aunque sigue en escala sub-segundo por ventana.
- **TRSS calibrado:** MAE mejora mediana 12.0%, tasa de victoria 70.0%; la calibración no cambia la conclusión central.

## Figuras generadas
- `figures/ch6_robust_improvement_ci.pdf`: mejoras medianas con IC95.
- `figures/ch6_dataset_mae_improvement.pdf`: heterogeneidad por conjunto de datos.
- `figures/ch6_scenario_heatmap_mae.pdf`: patrón/severidad de pérdida.
- `figures/ch6_runtime_mae_tradeoff.pdf`: compromiso precisión--tiempo.
- `figures/ch6_ablation_temporal_component.pdf`: contribución del término temporal.

## Tablas generadas
- `tables/ch6_phase_map.tex`: relación entre fase exploratoria, optimización final, confirmatoria y ablación.
- `tables/ch6_global_summary.tex`: resumen global MNE/TRSS fijo/TRSS calibrado/oráculo.
- `tables/ch6_robust_main.tex`: Wilcoxon, bootstrap y efectos para TRSS vs MNE.
- `tables/ch6_metric_portfolio.tex`: portafolio completo de métricas confirmatorias para TRSS fijo.
- `tables/ch6_by_dataset_mae.tex`: estratificación por conjunto de datos.
- `tables/ch6_selected_scenarios_mae.tex`: escenarios representativos por patrón y severidad.
- `tables/ch6_runtime_complexity.tex`: complejidad y tiempo mediano.
- `tables/ch8_objective_evidence_matrix.tex`: matriz de cumplimiento de objetivos e hipótesis.

## Decisión narrativa
Usar una conclusión condicional. TRSS se justifica cuando el objetivo es reconstrucción precisa bajo pérdida agrupada, periférica o severa; MNE sigue siendo preferible para preprocesamiento estándar rápido y para señales donde el supuesto de suavidad espacial es dominante.
