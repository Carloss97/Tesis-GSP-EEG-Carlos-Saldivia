## Backlog Consolidado

## Actualizacion abril 2026 (nuevos avances)

- [x] BGSRP alineado a formulacion RKHS y referencia primaria (Zhang et al., 2024)
- [x] Benchmark de chequeo BGSRP vs familia Narang generado en `results/`
- [x] Reproduccion de figura principal tipo GraphTRSS generada en `results/`
- [x] Tests paper-faithful agregados en `tests/test_paper_faithful.py`
- [x] Documentacion sincronizada en README, REFERENCES y VALIDATION_REPORT
- [x] Cierre B1 ejecutado: PRT-01.D/E/F + MET-01 con artefactos reproducibles en `results/opt_benchmark_b1_protocol_*`
- [x] Cierre B2 ejecutado: MET-02 + INS-13.A + INS-13.B + STAT-01 con corrida full-scale por lotes y consolidacion de publicacion
- [x] Cierre B3/B4 ejecutado: STAT-02 + REP-01 + REP-02 + DOC-01 + RPL-01 + RPL-02 + REL-01
- [x] Experimento unificado final ejecutado: 2304 corridas (3 datasets × 8 grafos × 24 metodos × 4 niveles), tablas y figuras en `results/unified_*`

---

## Estado general

### 1. Preparacion y carga de datos
- [x] Descargar y preparar datasets principales
- [x] Estandarizar formato de senales y posiciones
- [x] Implementar carga y preprocesamiento en `src/data`
- [x] Definir division entrenamiento/validacion/prueba para validacion final

### 2. Construccion de grafos
- [x] Wrapper de seleccion de metodo implementado
- [x] Metodos principales implementados y validados en corridas
- [x] Matrices de adyacencia generadas en experimentos
- [x] Verificacion de propiedades minimas (simetria/no-negatividad/diagonal cero)

### 3. Simulacion de canales faltantes
- [x] Enmascaramiento aleatorio implementado
- [x] Enmascaramiento sistematico implementado
- [x] Protocolo realista final para reporte de tesis/paper (Ticket: PRT-01, Estado: ✓ done)

Detalle de avance PRT-01:
- [x] PRT-01.A - Protocolo aleatorio reproducible implementado (`simulate_missing_channels`, `missing_ratio`, `random_state`)
- [x] PRT-01.B - Protocolo sistematico por lista de canales implementado (`simulate_missing_channels_systematic`, `missing_indices`)
- [x] PRT-01.C - Integracion en experimentos base (`experiment_mne_pipeline.py`, `experiment_pipeline_demo.py`, `optimize_and_benchmark.py`)
- [x] PRT-01.D - Definir escenarios realistas por region/tipo de electrodo para analisis de tesis (`frontal_band`, `occipital_band`, `left_lateral_temporal`, `right_lateral_temporal` en `results/opt_benchmark_b1_protocol_config.json`)
- [x] PRT-01.E - Definir bateria multi-nivel de perdida (10/20/30/40%) para cierre experimental (`missing_levels` en `results/opt_benchmark_b1_protocol_config.json`)
- [x] PRT-01.F - Congelar protocolo final por dataset y documentarlo para paper/tesis (`results/opt_benchmark_b1_protocol_config.json`, `results/opt_benchmark_b1_protocol_summary.csv`)

### 4. Interpolacion y reconstruccion
- [x] Wrapper unificado implementado (`interpolate_signals`)
- [x] Metodos por instante implementados
- [x] Metodos TV/tiempo implementados
- [x] Interfaz de entrada/salida estandarizada
- [x] Correccion paper-faithful de BGSRP y consolidacion de TRSS/sobolev_temporal
- [x] Estabilización numérica de `spline_surface` con fallback controlado

### 5. Evaluacion y comparacion
- [x] Metricas MAE, RMSE, DTW, SNR implementadas
- [x] Scripts de comparacion y optimizacion implementados
- [x] Resultados guardados en `results` con rankings y figuras
- [x] Corrida final extendida con DTW completo en candidatas finales (Ticket: MET-01, evidencia en `results/opt_benchmark_b1_protocol_raw.csv` y `results/opt_benchmark_b1_protocol_summary.csv`)
- [x] Réplica frozen Narang 2013-like agregada
- [x] Réplica frozen Puy 2018-like agregada
- [x] Réplica BGSRP exfig4-like (aprox. Python) agregada
- [x] MET-02 - Corrida final extendida full-scale ejecutada con matriz completa de datasets/grafos/metodos activos
- [x] STAT-01 - Consolidacion estadistica con media, desviacion estandar y CI95 en resumen final B2

### 6. Analisis y reporte
- [x] Conclusiones preliminares extraidas
- [x] Tests paper-faithful ampliados para métodos TV/tiempo activos
- [x] Tests dedicados para métodos de grafo `nnk` y `aew`
- [x] Consolidar tabla final baseline vs GSP vs TV/tiempo (media +- desviacion)
- [ ] Redactar version final de metodos, resultados y discusion

### 6.1 Cierre B2 (abril 2026)

- [x] INS-13.A - Comparativa controlada BGSRP vs familia Narang actualizada (`results/bgsrp_vs_narang_check.csv`, `results/bgsrp_vs_narang_check_summary.csv`)
- [x] INS-13.B - Gap residual BGSRP cuantificado para publicacion (`results/b2_publication_bgsrp_gap_residual.csv`)
- [x] Tabla pre-final top-k por familia y escenario (`results/opt_benchmark_b2_full_scale_topk_by_family_scenario.csv`, `results/b2_publication_topk_by_family_scenario.csv`)
- [x] Ranking consolidado final de publicacion (`results/b2_publication_ranking_final.csv`)
- [x] Registro de warnings remanentes con decision fixed/accepted/deferred (`results/opt_benchmark_b2_full_scale_warnings_registry.csv`)

### 6.2 Cierre B3/B4 (abril 2026)

- [x] STAT-02 - Significancia estadistica sobre comparaciones clave (`results/b3_stat02_significance.csv`, `results/b3_stat02_summary.md`)
- [x] REP-01 - Tabla final baseline vs GSP vs TV/tiempo (`results/b3_rep01_final_table_overall.csv`, `results/b3_rep01_final_table_by_scenario.csv`)
- [x] REP-02 - Limitaciones sincronizadas en paper y tesis (`paper/ieee/sections/discussion.tex`, `thesis/usm/chapters/05_discusion.tex`)
- [x] DOC-01 - Documentacion canonica sincronizada (`README.md`, `backlog.md`, `REFERENCES.md`, `VALIDATION_REPORT.md`)
- [x] RPL-01 - Guia reproducible consolidada (`results/b3_b4_reproducibility_guide.md`)
- [x] RPL-02 - Reporte de recursos computacionales (`results/b3_b4_compute_resources.md`)
- [x] REL-01 - Checklist final de envio y decision (`results/b3_b4_submission_checklist.md`, decision: Go con limitacion INS-13)
- [x] INS-13 estricta (intento cross-stack) ejecutada con evidencia MATLAB/GSPBox (`results/ins13_strict_matlab_compare_raw.csv`, `results/ins13_strict_matlab_compare_summary.csv`, `results/ins13_strict_status.md`)
- [x] INS-13 documentada para redaccion como `proxy_or_partial` (Go con limitacion; `strict_close=False` en `results/ins13_strict_status.md`)
- [x] Trazabilidad editorial paper/tesis a artefactos (`results/b3_b4_editorial_traceability.md`)
- [x] Politica de hardening de warnings no fatales (`results/b3_b4_warning_hardening.md`)

---

## Metodos implementados

### Leyenda de tickets de validacion

- ✓: Implementado y validado en corridas internas
- ✓✓: Implementado, validado y con evidencia paper-faithful fuerte
- ⚠: Implementado, pero con validacion paper-faithful parcial o pendiente

### Nomenclatura de tickets

- GRA-xx: metodos de construccion de grafos
- INS-xx: metodos de interpolacion por instante
- TVT-xx: metodos de interpolacion TV/tiempo

### Grafos (src/graph_construction/graph_constructors.py)

- [x] `knn`
  - Ticket: GRA-01
  - Referencia: Sakiyama et al. (2016)
  - Descripcion: grafo de conectividad k-nearest neighbors sobre posiciones de electrodos.
  - Parametros: `k`.
  - Estado Validacion: ✓

- [x] `knng`
  - Ticket: GRA-02
  - Referencia: Sakiyama et al. (2016)
  - Descripcion: kNN con ponderacion gaussiana sobre las aristas activas.
  - Parametros: `k`, `sigma`.
  - Estado Validacion: ✓

- [x] `vknng`
  - Ticket: GRA-03
  - Referencia: Tamaru et al. (2024)
  - Descripcion: version adaptativa de kNN con `k_i` variable por nodo segun densidad local.
  - Parametros: `k`, `alpha`, `k_min`, `k_max`.
  - Estado Validacion: ✓

- [x] `gaussian`
  - Ticket: GRA-04
  - Referencia: Karasuyama y Mamitsuka (2017)
  - Descripcion: grafo denso con pesos gausianos para todos los pares de nodos.
  - Parametros: `sigma`.
  - Estado Validacion: ✓

- [x] `epsilon_ball`
  - Ticket: GRA-05
  - Referencia: Shuman et al. (2013)
  - Descripcion: conecta nodos dentro de radio `epsilon`.
  - Parametros: `epsilon`.
  - Estado Validacion: ✓

- [x] `mst`
  - Ticket: GRA-06
  - Referencia: Ortega et al. (2018)
  - Descripcion: minimum spanning tree para garantizar conectividad minima sin ciclos.
  - Parametros: sin hiperparametros principales.
  - Estado Validacion: ✓

- [x] `fully_connected_inverse_distance`
  - Ticket: GRA-07
  - Referencia: baseline clasico (sin paper unico)
  - Descripcion: grafo completamente conectado con pesos `1/d`.
  - Parametros: regularizacion numerica interna sobre distancia cero.
  - Estado Validacion: ⚠

- [x] `nnk`
  - Ticket: GRA-08
  - Referencia: Shekkizhar y Ortega (2020/2023)
  - Descripcion: non-negative kernel regression con solucion NNLS local y simetrizacion.
  - Parametros: `k`, `sigma`, `reg`, `weight_threshold`, `backend`.
  - Estado Validacion: ✓✓

- [x] `aew`
  - Ticket: GRA-09
  - Referencia: Karasuyama y Mamitsuka (2017)
  - Descripcion: ponderacion adaptativa combinando cercania espacial y similitud de senal.
  - Parametros: `k`, `sigma_dist`, `sigma_corr`.
  - Estado Validacion: ✓

- [x] `kalofolias`
  - Ticket: GRA-10
  - Referencia: Kalofolias (2016), Kalofolias et al. (2017)
  - Descripcion: aprendizaje de pesos con modelo log-degree + regularizacion Frobenius.
  - Parametros: `distance_scale`, `a`, `b`, `max_iter`, `lr`, `tol`.
  - Estado Validacion: ✓

### Interpolacion por instante (src/interpolation_methods.py)

- [x] `linear`
  - Ticket: INS-01
  - Descripcion: interpolacion lineal por indice de canal.
  - Parametros: sin hiperparametros principales.
  - Estado Validacion: ✓

- [x] `nearest`
  - Ticket: INS-02
  - Descripcion: relleno por vecino mas cercano en indice de canal.
  - Parametros: sin hiperparametros principales.
  - Estado Validacion: ✓

- [x] `mean`
  - Ticket: INS-03
  - Descripcion: baseline que rellena faltantes con la media de observados por instante.
  - Parametros: sin hiperparametros principales.
  - Estado Validacion: ✓

- [x] `random`
  - Ticket: INS-04
  - Descripcion: baseline estocastico uniforme en rango observado.
  - Parametros: `random_state`.
  - Estado Validacion: ✓

- [x] `idw`
  - Ticket: INS-05
  - Descripcion: inverse distance weighting en espacio de electrodos.
  - Parametros: `positions`, `power`.
  - Estado Validacion: ✓

- [x] `spherical_spline`
  - Ticket: INS-06
  - Referencia: Perrin et al. (1989)
  - Descripcion: spline esferico EEG con funcion de Green tipo Perrin.
  - Parametros: `positions` (orden y numero de terminos internos fijos en implementacion).
  - Estado Validacion: ✓✓

- [x] `rbfi_tps`
  - Ticket: INS-07
  - Referencia: Jager et al. (2016)
  - Descripcion: RBF thin-plate spline.
  - Parametros: `positions`.
  - Estado Validacion: ✓

- [x] `rbfi_mq`
  - Ticket: INS-08
  - Referencia: Jager et al. (2016)
  - Descripcion: RBF multiquadric.
  - Parametros: `positions`.
  - Estado Validacion: ✓

- [x] `spline_surface`
  - Ticket: INS-09
  - Descripcion: smooth bivariate spline sobre coordenadas de electrodos.
  - Parametros: `positions`, `s` (interno adaptativo).
  - Estado Validacion: ✓

- [x] `gsp`
  - Ticket: INS-10
  - Descripcion: interpolacion laplaciana resolviendo bloques `L_uu` y `L_uk`.
  - Parametros: `adjacency`.
  - Estado Validacion: ✓

- [x] `tikhonov`
  - Ticket: INS-11
  - Descripcion: solucion regularizada con termino `alpha * L`.
  - Parametros: `adjacency`, `alpha`.
  - Estado Validacion: ✓

- [x] `gsmooth`
  - Ticket: INS-12
  - Descripcion: suavizado iterativo en grafo con matriz de transicion.
  - Parametros: `adjacency`, `lam`, `n_iter`.
  - Estado Validacion: ✓

- [x] `bgsrp`
  - Ticket: INS-13
  - Referencia: Zhang et al. (2024)
  - Descripcion: reconstruccion RKHS bandlimited (sin DC) con regularizacion `gamma`.
  - Parametros: `adjacency`, `bandwidth`, `gamma`, `reg`.
  - Estado Validacion: ⚠ (cierre operativo en modo proxy Python; equivalencia 1:1 MATLAB/GSPBox pendiente)

- [x] `puy`
  - Ticket: INS-14
  - Referencia: Puy et al. (2018)
  - Descripcion: aproximacion armonica regularizada en grafo.
  - Parametros: `adjacency`, `alpha`.
  - Estado Validacion: ✓

- [x] `sobolev`
  - Ticket: INS-15
  - Referencia: Giraldo et al. (2022)
  - Descripcion: regularizacion sobolev espacial con potencia de operador.
  - Parametros: `adjacency`, `alpha`, `order`.
  - Estado Validacion: ✓

Notas paper-faithful:
- `bgsrp`: actualizado a referencia primaria RKHS (Zhang et al., 2024) y estructura de algoritmo alineada a `gsp_BGSRP_recon.m`.
- `spherical_spline`: implementacion basada en formulacion de Perrin et al. (1989).

### Interpolacion TV/tiempo (src/interpolation_methods.py)

- [x] `graph_time_tikhonov`
  - Ticket: TVT-01
  - Descripcion: Tikhonov por instante + suavizado temporal por canal.
  - Parametros: `adjacency`, `alpha`, `beta`.
  - Estado Validacion: ✓

- [x] `trss`
  - Ticket: TVT-02
  - Referencia: Giraldo et al. (2022)
  - Descripcion: optimizacion espaciotemporal con terminos de datos, suavidad espacial y sobolev temporal.
  - Parametros: `adjacency`, `alpha`, `beta`, `n_iter`, `lr`.
  - Estado Validacion: ✓✓

- [x] `sobolev_temporal` (alias de `trss`)
  - Ticket: TVT-03
  - Descripcion: alias funcional directo de `trss`.
  - Parametros: `adjacency`, `alpha`, `beta`, `n_iter`, `lr`.
  - Estado Validacion: ✓✓

- [x] `tv`
  - Ticket: TVT-04
  - Descripcion: graph total variation via IRLS.
  - Parametros: `adjacency`, `lam`, `n_iter`, `eps`.
  - Estado Validacion: ✓

- [x] `temporal_laplacian`
  - Ticket: TVT-05
  - Descripcion: regularizacion en grafo producto espacio-tiempo con Kronecker.
  - Parametros: `adjacency`, `alpha`, `beta`.
  - Estado Validacion: ✓

- [x] `heat_diffusion_temporal`
  - Ticket: TVT-06
  - Descripcion: difusion temporal tipo kernel de calor + suavidad espacial.
  - Parametros: `adjacency`, `alpha`, `beta`, `n_iter`.
  - Estado Validacion: ✓

- [x] `spline_temporal`
  - Ticket: TVT-07
  - Descripcion: spline temporal por canal con regularizacion espacial posterior.
  - Parametros: `adjacency`, `alpha`, `s_temporal`.
  - Estado Validacion: ✓

- [x] `wavelet_temporal`
  - Ticket: TVT-08
  - Descripcion: filtrado temporal tipo Haar + regularizacion espacial.
  - Parametros: `adjacency`, `alpha`, `wavelet_level`.
  - Estado Validacion: ✓

- [x] `directed_tv`
  - Ticket: TVT-09
  - Referencia: Schultz y Villafane-Delgado (2020)
  - Descripcion: variacion total dirigida con termino temporal.
  - Parametros: `adjacency`, `alpha`, `beta`, `n_iter`, `eps`.
  - Estado Validacion: ✓

- [x] `visibility_graphs`
  - Ticket: TVT-10
  - Referencia: Bozkurt y Ortega (2022)
  - Descripcion: Visibility graphs + NNK: construcción de visibilidad (NVG/HVG), extracción de características (grado, clustering), similitud por NNK y suavizado temporal adaptativo.
  - Parametros: `adjacency`, `alpha`, `beta`, `gamma`, `n_iter`.
  - Estado Validacion: ✓ (paper-aligned)

Notas paper-faithful:
- `trss` y `sobolev_temporal` comparten implementacion (alias directo).
- `trss` usa costo espacio-temporal con Laplaciano espacial y diferencias temporales.

---

## Criterios de exito (estado)

- [x] Cada metodo de grafo retorna adyacencia valida (simetrica/no-negativa/diagonal cero, segun metodo)
- [x] Metodos data-driven aceptan senales y generan grafos validos
- [x] Metodos de interpolacion aceptan NaN y retornan mismo shape de entrada
- [x] Separacion de familias de reconstruccion para analisis (`instant` y `tv_time`)
- [x] Optimizacion de parametros en grilla ejecutable
- [x] Ranking global y ranking por familia disponibles
- [x] Test unitario paper-faithful creado (`tests/test_paper_faithful.py`)
- [ ] Cierre de validacion paper-faithful para todos los metodos activos
- [x] Validacion final de robustez con DTW completo en candidatas finales

---

## Datasets objetivo

- [x] MNE Sample Dataset
- [x] PhysioNet EEGMMIDB (loader implementado)
- [x] Sintetico propio
- [x] BCI Competition IV 2a (loader implementado)
- [x] Integrar de forma estable todos los datasets en corrida final unificada

---

## Evidencia de resultados ya generada

- [x] `results/paper_faithful_results.csv`
- [x] `results/paper_faithful_rank_mae.csv`
- [x] `results/opt_benchmark_full.csv`
- [x] `results/opt_benchmark_rank_all.csv`
- [x] `results/opt_benchmark_best_by_family.csv`
- [x] `results/opt_benchmark_mean_by_method.csv`
- [x] `results/opt_benchmark_b1_protocol_raw.csv`
- [x] `results/opt_benchmark_b1_protocol_summary.csv`
- [x] `results/opt_benchmark_b1_protocol_config.json`
- [x] `results/robust_top10_runs.csv`
- [x] `results/robust_top10_summary.csv`
- [x] `results/mae_by_method_dataset.png`
- [x] `results/heatmap_mae_method_graph.png`
- [x] `results/heatmap_snr_method_graph.png`
- [x] `results/opt_family_mae_boxplot.png`
- [x] `results/opt_heatmap_mae_graph_method.png`
- [x] `results/bgsrp_vs_narang_check.csv`
- [x] `results/bgsrp_vs_narang_check_summary.csv`
- [x] `results/graphtrss_main_figure_raw.csv`
- [x] `results/graphtrss_main_figure_summary.csv`
- [x] `results/graphtrss_main_figure.png`
- [x] `results/unified_final_raw.csv` (2304 corridas: 3 datasets × 8 grafos × 24 metodos × 4 niveles)
- [x] `results/unified_final_ranking.csv` (ranking global con MAE/DTW/RMSE/SNR)
- [x] `results/unified_final_topk.csv` (top-5 por dataset × nivel × familia)
- [x] `results/unified_final_dataset_best.csv` (mejor metodo por dataset × nivel)
- [x] `results/unified_final_graph_sensitivity.csv` (sensibilidad al metodo de grafo)
- [x] `results/unified_mae_ranking_bar.png`
- [x] `results/unified_mae_vs_missing_ratio.png`
- [x] `results/unified_heatmap_mae_graph_method.png`
- [x] `results/unified_family_boxplot.png`
- [x] `results/unified_dataset_comparison.png`
- [x] `results/unified_snr_ranking_bar.png`
- [x] `results/RESULTS_FINAL_REPORT.md` (reporte final con tablas y graficos)

---

## Pendientes inmediatos de cierre

- [x] Cerrar PRT-01 (protocolo realista final de canales faltantes) y dejarlo congelado por dataset
- [x] Ejecutar corrida reproducible B1 con DTW en candidatas finales (configuracion acotada para cierre de bloque)
- [x] Congelar configuracion final por dataset para seccion experimental del paper
- [x] Consolidar tabla final de comparacion (baseline vs GSP vs TV/tiempo)
- [ ] Completar redaccion final de metodos y discusion
