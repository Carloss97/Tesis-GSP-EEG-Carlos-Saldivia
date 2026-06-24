# Inventario técnico inicial — Capítulo 4 V3

Fecha: 2026-06-24

## 1. Comentarios activos

`chapters/04_resultados.tex` contiene 14 comentarios activos del profesor. Los capítulos 1, 2, 3, 5 y 6 no contienen comentarios activos del profesor.

Comentarios críticos agrupados:

1. Capítulo difícil de entender; análisis estadístico no corresponde como eje.
2. Faltan señales interpoladas representativas.
3. Falta explicar/evitar “ablación”.
4. Se debe eliminar test de hipótesis como marco principal.
5. Hay etiquetas poco claras: tasa de victoria y celdas de mapa de calor.
6. El caso TRSS malo debe explicarse.
7. El PSD debe mostrar original versus interpolado.
8. Complejidad debe definir variables y justificar expresiones.
9. Replanteamiento global del capítulo.

## 2. Estructura actual del capítulo 4

1. Relación entre Fases Experimentales.
2. Inventario de Evidencia Experimental.
3. Comparación Pareada TRSS--MNE.
4. Estratificación por Conjunto de Datos.
5. Efecto del Patrón y Severidad de Pérdida.
6. Componente Temporal de TRSS.
7. Preservación Morfológica y Espectral.
8. Tiempo de Cómputo y Complejidad.
9. Síntesis de Resultados.

## 3. Tablas actuales

Todas existen en `tables/`:

- `ch6_phase_map.tex`
- `ch6_global_summary.tex`
- `ch6_robust_main.tex`
- `ch6_metric_portfolio.tex`
- `ch6_by_dataset_mae.tex`
- `ch6_selected_scenarios_mae.tex`
- `ch6_runtime_complexity.tex`

## 4. Figuras actuales

Todas existen en `figures/`:

- `ch6_runtime_mae_tradeoff.pdf`
- `ch6_metric_portfolio_improvement.pdf`
- `ch6_boxplot_nrmse_balanced.pdf`
- `ch6_robust_improvement_ci.pdf`
- `ch6_dataset_mae_improvement.pdf`
- `ch6_scenario_heatmap_mae.pdf`
- `ch6_ablation_temporal_component.pdf`
- `res_opt_final__erp_comparison_static_mne_trss_filtered.pdf`
- `res_opt_final__best_psd_comparison_clean.pdf`
- `ch6_boxplot_runtime_balanced.pdf`

## 5. Script generador identificado

- `scripts/generate_ch6_artifacts.py`

Este script copia CSV fuente desde `results/`, regenera tablas `ch6_*` y escribe figuras `ch6_*`.

## 6. CSV fuente principales

### `results/trss_vs_mne_bads_extensive/raw_balanced.csv`

- Filas: 2700.
- Columnas relevantes:
  - `row_id`, `dataset`, `source_dataset`, `sfreq`, `n_times`, `n_channels`,
  - `missing_mode`, `missing_value`, `n_missing`, `missing_ratio_actual`, `seed`, `bad_idx`,
  - `method`, `method_family`, `params`,
  - `mae`, `rmse`, `dtw`, `snr`, `lsd`, `coherence_mean`, `nrmse`, `corr_mean`, `r2`,
  - `runtime_s`, `success`, `error`.

### `results/trss_vs_mne_bads_extensive/derived_balanced.csv`

- Filas: 3300.
- Mismas columnas base de `raw_balanced.csv` más:
  - `select_score`, `chosen_method`.

### `results/trss_vs_mne_bads_extensive/pairwise_comparisons_balanced.csv`

- Filas: 30.
- Contiene comparación por método/métrica:
  - `method_a`, `method_b`, `metric`, `n_pairs`,
  - medias, diferencias, intervalos, mejora relativa, `a_win_rate`,
  - `p_value`, `test`.

### `results/trss_vs_mne_bads_extensive/summary_by_scenario_balanced.csv`

- Filas: 400.
- Resume por método, dataset, patrón y severidad.

### `results/trss_vs_mne_bads_extensive/mae_winrate_by_scenario_balanced.csv`

- Filas: 60.
- Contiene directamente:
  - `missing_mode`, `missing_value`, `n_pairs`,
  - `a_win_rate_mae`, `median_rel_improve_mae`, `mean_rel_improve_mae`.

### `results/trss_vs_mne_bads_extensive/robust_stats/robust_pairwise_summary.csv`

- Filas: 30.
- Tiene columnas descriptivas y estadísticas:
  - `median_improvement`, `mean_improvement`, `win_rate`,
  - intervalos bootstrap,
  - `wilcoxon_p`, `p_fdr_bh`, `significant_fdr05`.

Para V3, usar como principales: `median_improvement`, `win_rate`, intervalos bootstrap y `n_pairs`. No usar `wilcoxon_p`, `p_fdr_bh` ni `significant_fdr05` como eje narrativo.

## 7. Señales reconstruidas / artefactos temporales

Búsqueda inicial:

- No se encontraron `.npz` ni `.npy` bajo el repositorio con búsqueda simple.
- Sí existen figuras y scripts relacionados con ERP/PSD:
  - `results_optuna_final/erp_comparison_static_mne_trss_filtered.png`
  - `results_optuna_final/erp_comparison_static_mne_trss.png`
  - `results_optuna_final/erp_timeseries_mne_sample_random_0.1.png`
  - `results_optuna_final/erp_timeseries_mne_sample_random_0.4.png`
  - `results_optuna_final/erp_timeseries_mne_sample_nearby_0.1.png`
  - `results_optuna_final/erp_timeseries_mne_sample_nearby_0.4.png`
  - `results_optuna_final/erp_physionet_cz_random_0.1.png`
  - `results_optuna_final/erp_physionet_cz_random_0.1_psd.png`
  - `experiments/plot_erp_time_series.py`
  - `scratch_plot_erp.py`

Conclusión inicial: las métricas para seleccionar casos están disponibles en CSV, pero las señales originales/reconstruidas podrían requerir regeneración desde código o recuperación desde scripts/figuras previas, porque no aparecen como `.npz`/`.npy` simples en `results/`.

## 8. Implicancias para la ejecución

1. Para tablas y resúmenes descriptivos, los CSV existentes son suficientes.
2. Para selección de casos representativos, `derived_balanced.csv` y `raw_balanced.csv` son suficientes como índice de casos y métricas.
3. Para figuras temporales y PSD V3, hay que inspeccionar `experiments/plot_erp_time_series.py` y los scripts relacionados para ver si pueden regenerar señales original/MNE/TRSS.
4. Si no hay señales guardadas, habrá que re-ejecutar métodos para los casos seleccionados usando dataset, máscara, semilla, canal y método.

## 9. Próximo paso técnico

1. Leer `experiments/plot_erp_time_series.py`, `scratch_plot_erp.py` y cualquier script que genere `results_optuna_final/*erp*`.
2. Determinar si esos scripts reconstruyen desde datos crudos o solo grafican archivos ya existentes.
3. Crear un script nuevo `scripts/select_cap4_representative_cases.py` que produzca:
   - `tables/ch4_representative_cases.csv`;
   - `tables/ch4_representative_cases.tex`.
4. Luego crear o adaptar un script de figuras:
   - `scripts/generate_ch4_v3_figures.py`.
