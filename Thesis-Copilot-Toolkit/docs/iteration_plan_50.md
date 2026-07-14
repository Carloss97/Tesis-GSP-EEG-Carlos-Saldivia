# Plan Maestro: 50 Iteraciones Definitivas

Objetivo: entregar un plan experiment al completo (exactamente 50 iteraciones) que cubra: sanity checks, barridos de parámetros (MR, k, graph density), familia temporal, datasets proxy→canónicos, tests en datos reales, replicaciones para significancia, backfill metadata histórico, y pasos de análisis y validación posterior.

**Defaults y convenciones**
- **Métodos canónicos (baseline group)**: ["linear","ica","spherical_spline","rbfi_tps"] — estos deben estar siempre incluidos en el grupo baseline.
- **Métodos excluidos**: `mean`, `nearest` (no programar en scheduling activo; mantener implementaciones para reproducibilidad histórica sólo).
- **Familia TV**: incluir métodos de la familia TV (p.ej. `temporal_laplacian`, `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`). Excluir explícitamente del scheduling activo: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`. Los demás métodos TV (p.ej. `temporal_laplacian`, `trss`, `graph_time_tikhonov`, `sobolev_temporal`) pueden programarse y deben validarse mediante pilotos controlados; registrar una Decision Record antes de su adopción amplia.
- **Constructores deshabilitados**: `mst`, `fully_connected_inverse_distance` (guardas aplicadas en tiempo de ejecución).
- **Nomenclatura datasets canónicos**: `mne_sample`, `physionet_real`, `bci_iv2a_real_sXX` (por sujeto), `iris_graph_signal`.
- **Metadata obligatoria en nuevos _run_metadata.json**: `normalization`, `missing_mode` (ver sección Metadata Schema).
- **Política artefactos históricos**: *no sobrescribir*; crear sidecar `*_run_metadata_deprecation_map.json` cuando sea necesario.

**Schema de metadata recomendada (campos mínimos en cada `*_run_metadata.json`)**
- **experiment_id**: string (ej. "it01_sanity")
- **dataset_key**: string (ej. "mne_sample")
- **graph_constructor**: string (ej. "nnk(k=8)")
- **method_list**: list[string]
- **missing_pattern**: string ("MCAR", "MAR", "temporal_window", "sensor_dropout", "structured_sensor_dropout")
- **missing_ratios**: list[number]
- **normalization**: string ("zscore_channel", "per_channel_meanstd", "none")
- **missing_mode**: string (matches missing_pattern semantic)
- **seeds**: list[int]
- **runtime_seconds**: number (cuando esté disponible)
- **notes**: string (libre)

**Naming y outputs esperados por iteración**
- Raw results CSV: `confirm_XXX_<shortname>_raw.csv`
- Run metadata: `confirm_XXX_<shortname>_run_metadata.json` (con los campos obligatorios)
- Figures: `confirm_XXX_<shortname>_fig01.pdf`, ...
- Significance: `confirm_XXX_<shortname>_significance.csv`

---

**Pre-experiment (antes de it01)**
- Verificar disponibilidad de datos y mapear proxies: asegurarse `datasets/` contiene `MNE-eegbci-data` o proxies y registrar `iris_graph_signal` loader.
- Actualizar `.gitignore` para `results/` y figuras grandes; usar Git LFS para binarios si se requiere (no versionar resultados en commits de código).
- Ejecutar lint y pruebas unitarias del runner (si existen).
- Confirmar `BASELINE_METHODS` central en: [Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py](Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py) o el módulo base correspondiente.

---

**Evaluación: Enfoque comparativo (mejora sobre baselines)**

- Objetivo general: cada iteración está diseñada para evaluar si uno o varios métodos propuestos mejoran (o no) el rendimiento respecto al grupo baseline. El objetivo principal no es recopilar métricas de los baselines en sí, sino cuantificar la diferencia (delta) entre método y baseline y evaluar su significancia y tamaño de efecto.

- Protocolo de comparación (aplica a todas las iteraciones):
    - Para cada combinación (dataset, graph, MR, seed) calcule:
        - Métricas por método: MAE, RMSE, SSIM (si aplica), `runtime_seconds`.
        - Métricas baseline: mismas métricas para cada método en `baseline group`.
        - Delta: diferencia en la métrica principal (ej. `MAE_baseline_best - MAE_method`). Un delta positivo indica mejora relativa.
        - Tamaño de efecto: Cohen's d (o Cliff's delta si distribución no paramétrica).
        - Prueba estadística: paired Wilcoxon signed-rank test (por seed/configuración pareada). Calcular p-value y aplicar corrección FDR para comparaciones múltiples.
        - Intervalos de confianza: bootstrap (n=1000) sobre la métrica principal para estimar incertidumbre del delta.
    - Criterio de decisión:
        - Método considerado mejora si `p_corr < 0.05` y `cohen_d >= 0.2` y delta mediano consistente en seeds.
    - Reporte por iteración:
        - `*_raw.csv` debe incluir columnas: `method`, `seed`, `metric_MAE`, `metric_RMSE`, `runtime_seconds`, `is_baseline` (bool).
        - `*_run_metadata.json` incluirá campo `baseline_group` con lista de métodos baselines usados para comparación.
        - `*_analysis_delta.csv` resumen de deltas agregados por método (median, mean, CI, p_val, p_corr, cohen_d).
    - Visualización mínima por iteración:
        - Boxplot comparativo method vs baseline para la métrica principal.
        - Plot delta vs missing_ratio o parámetro relevante.
        - Tabla de significancia con p-values y effect sizes.

- Notas operacionales:
    - Mantener baselines en cada corrida para referencia; en reporting final mostrar sólo las comparaciones (mejora/no-mejora).
    - Si un método falla en >50% de seeds para una configuración, marcar como `unstable` y reportar; no incluir en replicaciones de significancia.

**Iteraciones (it01 — it50)**
- Notación por entrada: `itNN — Nombre corta`: Dataset(s); Graph(s); Missing pattern(s); MR; Methods; Seeds; Objetivo/Salida.

1. it01 — Sanity (toy)
   - Dataset: iris_graph_signal
   - Graph: knn(k=3)
   - Missing pattern: MCAR
   - MR: [0.10]
   - Methods: baseline group
   - Seeds: [0]
   - Objetivo: probar pipeline, formatos de metadata y naming; salida mínima.

2. it02 — Iris sweep
   - Dataset: iris_graph_signal
   - Graphs: knn(3), nnk(3)
   - Missing pattern: MCAR
   - MR: [0.05, 0.20]
   - Methods: baseline group
   - Seeds: [0,1,2]
   - Objetivo: comprobar variabilidad pequeña y asegurar reproducibilidad.

3. it03 — MNE baseline integration
   - Dataset: mne_sample
   - Graph: nnk(k=5)
   - Missing pattern: MCAR
   - MR: [0.10]
   - Methods: baseline group + tikhonov
   - Seeds: [0,1]
   - Objetivo: validar loader `mne_sample` y cálculos básicos.

4. it04 — Temporal family smoke test
   - Dataset: mne_sample
   - Graph: knn(k=10)
   - Missing pattern: temporal_window (contiguous)
   - MR: [0.10]
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
   - Seeds: [0,1,2]
   - Objetivo: chequear familia temporal y produce figuras temporales.

5. it05 — Physionet small realistic
   - Dataset: physionet_real
   - Graph: nnk(k=8)
   - Missing pattern: structured_sensor_dropout
   - MR: [0.10,0.20]
   - Methods: baseline group + trss + tikhonov
   - Seeds: [0,1,2]
   - Objetivo: validar ejecución en datos reales.

6. it06 — BCI subject 01 (real)
   - Dataset: bci_iv2a_real_s01
   - Graph: nnk(k=8)
   - Missing pattern: realistic (sensor dropout)
   - MR: [0.10]
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
   - Seeds: [0,1,2]
   - Objetivo: subject-level validation.

7. it07 — BCI subject 02 (real)
   - Dataset: bci_iv2a_real_s02
   - Graph: nnk(k=8)
   - Missing pattern: realistic
   - MR: [0.10]
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
   - Seeds: [0,1,2]
   - Objetivo: comparar sujetos.

8. it08 — Graph sensitivity (k small)
   - Dataset: mne_sample
   - Graphs: knn(k=3), nnk(k=3), radius(r=0.20)
   - MR: [0.10]
   - Methods: baseline group
   - Seeds: [0,1]
   - Objetivo: sensibilidad a grafos de baja densidad.

9. it09 — MR sweep (mne_sample)
   - Dataset: mne_sample
   - Graph: knn(k=5)
   - MR: [0.05,0.10,0.20,0.40]
   - Methods: baseline group + tikhonov
   - Seeds: [0,1,2]
   - Objetivo: comportamiento ante incremento de missing ratio.

10. it10 — MR sweep (physionet)
    - Dataset: physionet_real
    - Graph: nnk(k=8)
    - MR: [0.05,0.10,0.20]
    - Methods: baseline group + trss
    - Seeds: [0,1,2]
    - Objetivo: robustez en datos reales.

11. it11 — Graph density sweep
    - Dataset: mne_sample
    - Graph: knn(k) with k∈[3,5,10,15]
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: efecto de densidad en reconstrucción.

12. it12 — Constructor guard check
    - Dataset: mne_sample
    - Graph: fully_connected (generic); evitar fully_connected_inverse_distance
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0]
    - Objetivo: confirmar que `fully_connected_inverse_distance` está bloqueado por guardas.

13. it13 — Temporal vs spatial (physionet)
    - Dataset: physionet_real
    - Graph: nnk(8)
    - MR: [0.10,0.20]
    - Methods: baseline group vs TV-family methods vs trss (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1,2]
    - Objetivo: comparar enfoques temporales y espaciales.

14. it14 — Cross-dataset transfer (light)
    - Train dataset: mne_sample
    - Eval dataset: physionet_real (small subset)
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: top-2 métodos observados en pilotos
    - Seeds: [0,1]
    - Objetivo: evaluar generalización entre dominios.

15. it15 — Replicación para significancia (selected configs)
    - Dataset: physionet_real (config ganadora)
    - MR: [0.10]
    - Methods: 3 mejores configuraciones
    - Seeds: [0..4] (5 seeds)
    - Objetivo: estimar varianza y preparar test estadístico.

16. it16 — Subject variability (BCI multi-subj)
    - Dataset: bci_iv2a_real_s01..s04
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1,2]
    - Objetivo: medir consistencia entre sujetos.

17. it17 — Light-profile representative sweep
    - Dataset: stratified subset (mne_sample, physionet_real, bci_s01)
    - Graphs: knn(5), nnk(8)
    - MR: [0.10, 0.20]
    - Methods: baseline group + trss + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0]
    - Objetivo: validar ejecución a escala reducida (10% combinaciones).

18. it18 — Sidecar metadata backfill (historic sample)
    - Action: generar sidecars `*_run_metadata_deprecation_map.json` para 5 artefactos históricos representativos
    - Objetivo: validar script de backfill sin tocar archivos originales.

19. it19 — Non-Gaussian noise robustness
    - Dataset: mne_sample
    - Graph: knn(5)
    - Noise: impulsive/non-gaussian (cierta proporción de outliers)
    - MR: [0.10]
    - Methods: baseline group + robust variants (trss)
    - Seeds: [0,1,2]
    - Objetivo: robustez frente a ruido de tipo real.

20. it20 — High MR stress test
    - Dataset: mne_sample
    - Graph: nnk(5)
    - MR: [0.40,0.60]
    - Methods: baseline group + trss + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1]
    - Objetivo: comportamiento extremo.

21. it21 — Interpolator ablation (compare fallback)
    - Dataset: mne_sample
    - Graph: knn(5)
    - MR: [0.10]
    - Methods: baseline group + tikhonov + trss
    - Seeds: [0,1]
    - Objetivo: comparar fallback strategies (evitar mean/nearest).

22. it22 — KNN interpolation hyper (k sweep)
    - Dataset: physionet_real
    - Graph: knn(k) with k∈[3,5,8,12]
    - MR: [0.10,0.20]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: k óptimo para grafos knn.

23. it23 — Radius graph sensitivity
    - Dataset: mne_sample
    - Graph: radius(r) with r∈[0.15,0.25,0.35]
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: impacto de radios en generación de grafos.

24. it24 — Edge-pruning robustness
    - Dataset: physionet_real
    - Graph: nnk(8) + pruning (remove top x% edges)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: sensibilidad a sparsificación.

25. it25 — TRSS tuning (regularization sweep)
    - Dataset: mne_sample
    - Graph: nnk(5)
    - MR: [0.10]
    - Methods: trss with lambda∈[1e-3,1e-2,1e-1]
    - Seeds: [0,1]
    - Objetivo: sensibilidad a hiperparámetro.

26. it26 — Transfer BCI → MNE (light)
    - Train: bci_iv2a_real_s01
    - Eval: mne_sample small
    - MR: [0.10]
    - Methods: top-2 observed
    - Seeds: [0,1]
    - Objetivo: transferencia cross-domain.

27. it27 — Multi-method ensemble (voting)
    - Dataset: physionet_real
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group + ensemble (majority/voting)
    - Seeds: [0,1,2]
    - Objetivo: evaluar si ensemble mejora estabilidad.

28. it28 — Temporal window size sweep
    - Dataset: mne_sample
    - Graph: knn(10)
    - Missing pattern: temporal_window with window_size∈[10,25,50] samples
    - MR: [0.10]
    - Methods: TV-family methods + baseline group (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1]
    - Objetivo: sensibilidad a ventana temporal.

29. it29 — MAR pattern (missing at random dependent)
    - Dataset: physionet_real
    - Graph: nnk(8)
    - Missing pattern: MAR
    - MR: [0.10,0.20]
    - Methods: baseline group + trss
    - Seeds: [0,1,2]
    - Objetivo: comportamiento ante MAR.

30. it30 — Sensor cluster dropout
    - Dataset: bci_iv2a_real_s01
    - Graph: nnk(8)
    - Missing pattern: spatial_cluster_dropout (contiguous sensors)
    - MR: [0.10]
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1]
    - Objetivo: evaluar recuperación cuando faltan regiones de sensores.

31. it31 — Cross-validation stability
    - Dataset: mne_sample
    - Graph: knn(5)
    - MR: [0.10]
    - Methods: baseline group
    - CV: k-fold (k=5)
    - Seeds: [0]
    - Objetivo: estabilidad de métricas bajo CV.

32. it32 — Compute-time profiling
    - Dataset: mne_sample
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0]
    - Objetivo: medir tiempos por método (por canal y por sample).

33. it33 — Memory profiling (big sample)
    - Dataset: large proxy (if available)
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0]
    - Objetivo: identificar hot-spots de memoria.

34. it34 — Realistic pipeline (end-to-end)
    - Dataset: physionet_real
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group + trss + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1,2]
    - Objetivo: ensayo completo de producción.

35. it35 — Statistical test battery
    - Dataset: outputs combinados de it15 + it34
    - Acción: aplicar Wilcoxon pairwise, correction (FDR)
    - Objetivo: preparar tablas de significancia para paper.

36. it36 — Ablation: remove baseline component
    - Dataset: mne_sample
    - Graph: knn(5)
    - MR: [0.10]
    - Methods: ablate one baseline a la vez (p.ej. remove ica)
    - Seeds: [0,1]
    - Objetivo: medir contribución individual.

37. it37 — Synthetic signal interpolation test
    - Dataset: synthetic (known ground-truth)
    - Graph: knn(5)
    - MR: [0.10,0.20]
    - Methods: baseline group
    - Seeds: [0..2]
    - Objetivo: comparar con ground-truth cuantitativo.

38. it38 — Random graph baseline
    - Dataset: mne_sample
    - Graph: random_graph(ρ=0.05)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: establecer baseline de referencia sin estructura.

39. it39 — Edge-weight scheme comparison
    - Dataset: physionet_real
    - Graphs: weight schemes (corr, cos, euclidean)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: impacto de esquema de pesos.

40. it40 — Multi-metric report (MAE, RMSE, SSIM)
    - Dataset: seleccionada (mne_sample)
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1,2]
    - Objetivo: entregar reporte completo de métricas.

41. it41 — Non-stationary missing (time-varying MR)
    - Dataset: mne_sample
    - Missing pattern: MR cambiante en tiempo (0→0.3)
    - Graph: knn(10)
    - Methods: baseline group + TV-family methods (exclude: `directed_tv`, `heat_diffusion_temporal`, `wavelet_temporal`)
    - Seeds: [0,1]
    - Objetivo: resiliencia ante no-estacionariedad.

42. it42 — Long-run stability (multiple seeds ext)
    - Dataset: physionet_real
    - Graph: nnk(8)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0..9] (10 seeds)
    - Objetivo: estimar distribución empírica de métricas.

43. it43 — Worst-case missing geometry
    - Dataset: synthetic grid
    - Missing pattern: structured worst-case (remove sensors maximizing uncertainty)
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: stress adversarial.

44. it44 — Repro pipeline (container test)
    - Acción: ejecutar subset en contenedor (Docker) para validar reproducibilidad de entorno
    - Objetivo: verificar que runs son reproducibles en imagen.

45. it45 — Data-augmentation effect
    - Dataset: mne_sample
    - Augment: small perturbations en train
    - MR: [0.10]
    - Methods: baseline group
    - Seeds: [0,1]
    - Objetivo: comprobar si augmentation mejora reconstrucción.

46. it46 — Backfill sidecars (full sweep sample)
    - Acción: ejecutar script de backfill contra 20 artefactos históricos representativos
    - Objetivo: validar que sidecars contienen `normalization` y `missing_mode` y no alteran originales.

47. it47 — QA y verificación de metadatos
    - Acción: validar que todos `*_run_metadata.json` generados en it01–it46 cumplen schema
    - Objetivo: pasar checklist de calidad para análisis.

48. it48 — Pilot final (full light-profile run)
    - Acción: ejecutar `it17` ampliado (subconjunto 10% representativo) para validar pipeline completo
    - Objetivo: conseguir report inicial `pilot_validation_report.md`.

49. it49 — Análisis y agregación (pilot results)
    - Acción: agrupar outputs, calcular métricas agregadas, preparar tablas y figuras para revisión
    - Objetivo: decidir ajustes finales antes de producción.

50. it50 — Producción: schedule final y estimación recursos
    - Acción: fijar schedule completo (todas combinaciones seleccionadas), estimar nodo‑horas, espacio en disco, crear tickets/PR con cambios solo de código y docs
    - Objetivo: dejar listo para ejecución a escala en cluster o nube.

---

**Análisis posterior (qué viene después)**
- Ejecutar pipeline de agregación: concatenar `*_raw.csv` por familia y generar `confirm_summary.csv` y `confirm_pairwise_wilcoxon.csv`.
- Tests estadísticos: pairwise Wilcoxon o permutación, corrección FDR y reportes de efecto (Cohen's d cuando corresponda).
- Visualización: figuras temporales, topomaps, error-vs-MR plots, heatmaps de sensibilidad por graph/method.
- QA: revisar `pilot_validation_report.md`, asegurar que `run_metadata` tiene `normalization` y `missing_mode` en todas las entradas nuevas.
- Documentar decisiones: Decision Record para cualquier cambio (por qué se excluyeron métodos, por qué parámetros seleccionados).

**Criterios de aceptación por iteración**
- El `*_run_metadata.json` existe y contiene campos obligatorios.
- El `*_raw.csv` se genera y contiene filas por método y seed.
- No excepciones fatales durante ejecución; logs con tracebacks almacenados.
- Métricas principales (MAE/RMSE) calculadas; tiempo de ejecución registrado.

**Comandos y ejecuciones sugeridas (ejemplo)**
- Generar schedule (placeholder):
```
python Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py --generate-schedule --out schedule_it1-50.json
```
- Ejecutar iteración única (ejemplo it03):
```
python Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py --run-it it03 --light-profile
```
- Ejecutar piloto representativo (it48):
```
python Thesis-Copilot-Toolkit/experiments/run_future_work_it121_it130.py --run-subset pilot --profile light
```
(Adaptar a los argumentos reales del runner; estos son comandos recomendados como plantilla.)

**Estimación de recursos (orientativa)**
- Iteraciones pequeñas (iris, toy): ~5–15 min cada una (CPU).
- Iteraciones medias (mne_sample, small physionet): 30–90 min por configuración/seed.
- Iteraciones grandes (BCI multi-subj, producción): 2–6 horas por configuración/seed si no se paraleliza.
- Total estimado para toda la campaña (si se ejecuta sin paralelismo): semanas. Con cluster paralelo y perfilado `light → full`, se reduce sustancialmente.

**Política de Git y artefactos**
- Sólo commitear código y docs (README, iteration_plan_50.md, scripts). No commitear `results/` ni figuras grandes.
- Para grandes artefactos usar Git LFS o almacenamiento externo (Drive/Zenodo) y añadir referencias en `HISTORICAL_ARTIFACTS_NOTICE.md`.
- Antes de push: revisar `git status` y hacer `git add` selectivo.

**Siguientes pasos recomendados**
1. Revisar este plan y confirmar aceptabilidad (param ranges, datasets disponibles).
2. Implementar (o adaptar) el generador `IterDef` para producir las 50 entradas y el flag `--light-profile` (subconjunto reproducible).
3. Implementar script de backfill de metadata y ejecutar `it18` e `it46` sobre muestras históricas.
4. Ejecutar `it17` / `it48` (piloto ligero) y revisar `pilot_validation_report.md`.
5. Ajustar plan si el piloto muestra incompatibilidades y luego proceder a `it50` (schedule final).

---

Archivo creado: [Thesis-Copilot-Toolkit/docs/iteration_plan_50.md](Thesis-Copilot-Toolkit/docs/iteration_plan_50.md)

Si quieres, lo guardo también en un PR preliminar o lo commiteo en una rama `experiment/it-plan-50` (solo código/docs). ¿Procedo con: (A) implementar el generador IterDef + --light-profile ahora, (B) crear el script de backfill metadata, o (C) ejecutar el piloto ligero (it48)? Indica la letra deseada.