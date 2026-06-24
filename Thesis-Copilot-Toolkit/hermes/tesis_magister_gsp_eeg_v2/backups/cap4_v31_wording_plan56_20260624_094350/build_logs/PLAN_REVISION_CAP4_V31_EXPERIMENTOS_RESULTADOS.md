# Plan V3.1 — Convertir Capítulo 4 en “Experimentos y Resultados”

Fecha: 2026-06-24  
Backup: `backups/cap4_experiments_results_v31_20260624_084953/`

## 1. Diagnóstico después de V3

La versión V3 resolvió el problema principal indicado por el profesor: el capítulo dejó de depender de pruebas de hipótesis y agregó resultados descriptivos, señales representativas, PSD original--interpolado, contribución temporal, costo y frontera práctica TRSS--MNE.

Sin embargo, la revisión detallada muestra una brecha narrativa: el capítulo todavía se lee más como “Resultados” que como “Experimentos y Resultados”. La metodología de los capítulos 1--3 menciona una fase exploratoria amplia, optimización de métodos y reducción de candidatos, pero el capítulo 4 no documenta suficientemente esa trayectoria experimental antes del benchmark final.

## 2. Objetivo de la revisión V3.1

Reestructurar el capítulo 4 para que documente la fase experimental completa:

1. cribado preliminar de métodos y grafos;
2. reducción de candidatos por desempeño, costo, reproducibilidad y circularidad;
3. optimización intermedia y congelamiento de variantes;
4. benchmark final TRSS--MNE;
5. inspección temporal/espectral de casos representativos;
6. síntesis práctica.

La comparación final se mantiene sin análisis estadístico como eje narrativo. Los resultados preliminares se presentan como evidencia de diseño experimental, no como conclusión principal.

## 3. Artefactos reales identificados

### Cribado amplio

- `results/tablas_resumen/top5_combinaciones_recomendadas_gsp.csv`
- `results/tablas_resumen/resumen_familias_stats.csv`
- `results/tablas_resumen/resumen_combinaciones_mediana.csv`
- `results/tablas_resumen/phase2_iteration_metrics_pivot.csv`

### Reducción por costo/estabilidad

- `results/tablas_resumen/phase2_microbench_latency.csv`
- `experiments/filtered_selections_compact.md`
- `experiments/active_schedule.json`

### Optimización intermedia

- `results_optuna_final/optuna_best_results.csv`
- `results_optuna_final/global_hyperparams_evaluation.csv`
- `results/final_grid_search_ranking.csv`

### Comparación final

- `results/trss_vs_mne_bads_extensive/raw_balanced.csv`
- `results/trss_vs_mne_bads_extensive/derived_balanced.csv`
- `results/trss_vs_mne_bads_extensive/summary_overall_balanced.csv`
- `results/trss_vs_mne_bads_extensive/mae_winrate_by_scenario_balanced.csv`
- `results/trss_vs_mne_bads_extensive/robust_stats/robust_pairwise_summary.csv`
- `results/trss_vs_mne_bads_extensive/EXPERIMENT_LOG_TRSS_MNE_balanced.md`

## 4. Nuevas tablas V3.1

Generadas con `scripts/generate_ch4_v31_experiment_artifacts.py`:

- `tables/ch4_experimental_phase_overview.tex`
- `tables/ch4_preliminary_screening_top_candidates.tex`
- `tables/ch4_runtime_screening_summary.tex`
- `tables/ch4_candidate_reduction_decisions.tex`

Estas tablas deben insertarse al inicio del capítulo 4 para explicar cómo se llegó al conjunto final de métodos y grafos.

## 5. Nueva estructura propuesta del capítulo 4

1. **Experimentos y resultados** — apertura con alcance completo.
2. **Mapa de fases experimentales** — tabla de fases y artefactos.
3. **Cribado preliminar de métodos y grafos** — mejores combinaciones método--grafo por dataset.
4. **Reducción de candidatos para la fase comparativa** — costo, circularidad, reproducibilidad y decisión metodológica.
5. **Optimización intermedia y congelamiento de variantes** — Optuna/grillas y separación entre exploración y evidencia final.
6. **Inventario de escenarios, métodos y métricas de la comparación final**.
7. **Resumen descriptivo TRSS--MNE**.
8. **Dependencia del resultado respecto del escenario de pérdida**.
9. **Reconstrucciones temporales representativas**.
10. **Preservación espectral**.
11. **Contribución del término temporal**.
12. **Costo computacional y complejidad**.
13. **Síntesis: frontera práctica TRSS vs MNE**.

## 6. Ajustes necesarios en capítulos 1--3

- **Capítulo 1:** actualizar estructura/alcance para decir explícitamente que el capítulo 4 documenta experimentos preliminares, reducción de candidatos y benchmark final, no solo resultados finales.
- **Capítulo 2:** en construcción de grafos, aclarar que los grafos data-driven y de correlación se discuten teóricamente pero su paso a la fase final fue decidido experimentalmente en el capítulo 4.
- **Capítulo 3:** reforzar que el diseño consta de fases sucesivas: screening amplio, reducción de candidatos, optimización intermedia y comparación final pareada.

## 7. Revisión de forma y trazabilidad

Después de editar:

1. verificar que toda tabla/figura insertada sea mencionada en el texto;
2. compilar `tesis_completa.tex` y `tesis_caps_1_5.tex`;
3. revisar errores, refs/citas indefinidas y overfull hbox;
4. ejecutar `scripts/validate_thesis.py`;
5. ejecutar QA visual para comprobar que no haya texto superpuesto, leyendas cortadas ni flotantes fuera de sección.

## 8. Criterio de término V3.1

La revisión se considera lista cuando el capítulo 4 pueda leerse como una bitácora experimental completa: primero se entiende cómo se redujo el espacio de métodos y grafos, luego se entiende cómo se eligió el benchmark final y finalmente se interpretan los resultados finales TRSS--MNE con evidencia descriptiva, temporal, espectral y práctica.
