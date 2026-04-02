## Backlog Consolidado

## Actualizacion abril 2026 (nuevos avances)

- [x] BGSRP alineado a formulacion RKHS y referencia primaria (Zhang et al., 2024)
- [x] Benchmark de chequeo BGSRP vs familia Narang generado en `results/`
- [x] Reproduccion de figura principal tipo GraphTRSS generada en `results/`
- [x] Tests paper-faithful agregados en `tests/test_paper_faithful.py`
- [x] Documentacion sincronizada en README, REFERENCES y VALIDATION_REPORT

---

## Estado general

### 1. Preparacion y carga de datos
- [x] Descargar y preparar datasets principales
- [x] Estandarizar formato de senales y posiciones
- [x] Implementar carga y preprocesamiento en `src/data`
- [ ] Definir division entrenamiento/validacion/prueba para validacion final

### 2. Construccion de grafos
- [x] Wrapper de seleccion de metodo implementado
- [x] Metodos principales implementados y validados en corridas
- [x] Matrices de adyacencia generadas en experimentos
- [x] Verificacion de propiedades minimas (simetria/no-negatividad/diagonal cero)

### 3. Simulacion de canales faltantes
- [x] Enmascaramiento aleatorio implementado
- [x] Enmascaramiento sistematico implementado
- [ ] Protocolo realista final para reporte de tesis/paper (Ticket: PRT-01, Estado: ⚠ parcial)

Detalle de avance PRT-01:
- [x] PRT-01.A - Protocolo aleatorio reproducible implementado (`simulate_missing_channels`, `missing_ratio`, `random_state`)
- [x] PRT-01.B - Protocolo sistematico por lista de canales implementado (`simulate_missing_channels_systematic`, `missing_indices`)
- [x] PRT-01.C - Integracion en experimentos base (`experiment_mne_pipeline.py`, `experiment_pipeline_demo.py`, `optimize_and_benchmark.py`)
- [ ] PRT-01.D - Definir escenarios realistas por region/tipo de electrodo para analisis de tesis
- [ ] PRT-01.E - Definir bateria multi-nivel de perdida (p.ej. 10/20/30/40%) para cierre experimental
- [ ] PRT-01.F - Congelar protocolo final por dataset y documentarlo para paper/tesis

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
- [ ] Corrida final extendida con DTW completo en candidatas finales
- [x] Réplica frozen Narang 2013-like agregada
- [x] Réplica frozen Puy 2018-like agregada
- [x] Réplica BGSRP exfig4-like (aprox. Python) agregada

### 6. Analisis y reporte
- [x] Conclusiones preliminares extraidas
- [x] Tests paper-faithful ampliados para métodos TV/tiempo activos
- [x] Tests dedicados para métodos de grafo `nnk` y `aew`
- [ ] Consolidar tabla final baseline vs GSP vs TV/tiempo (media +- desviacion)
- [ ] Redactar version final de metodos, resultados y discusion

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
  - Estado Validacion: ⚠

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

- [x] `adaptive_temporal`
  - Ticket: TVT-10
  - Referencia: Bozkurt y Ortega (2022)
  - Descripcion: suavizado temporal adaptativo por coherencia mas suavidad espacial.
  - Parametros: `adjacency`, `alpha`, `beta`, `gamma`, `n_iter`.
  - Estado Validacion: ✓

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
- [ ] Validacion final de robustez con DTW completo en candidatas finales

---

## Datasets objetivo

- [x] MNE Sample Dataset
- [x] PhysioNet EEGMMIDB (loader implementado)
- [x] Sintetico propio
- [x] BCI Competition IV 2a (loader implementado)
- [ ] Integrar de forma estable todos los datasets en corrida final unificada

---

## Evidencia de resultados ya generada

- [x] `results/paper_faithful_results.csv`
- [x] `results/paper_faithful_rank_mae.csv`
- [x] `results/opt_benchmark_full.csv`
- [x] `results/opt_benchmark_rank_all.csv`
- [x] `results/opt_benchmark_best_by_family.csv`
- [x] `results/opt_benchmark_mean_by_method.csv`
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

---

## Pendientes inmediatos de cierre

- [ ] Cerrar PRT-01 (protocolo realista final de canales faltantes) y dejarlo congelado por dataset
- [ ] Ejecutar corrida final larga con DTW en candidatas top y mas ventanas temporales
- [ ] Congelar configuracion final por dataset para seccion experimental del paper
- [ ] Consolidar tabla final de comparacion (baseline vs GSP vs TV/tiempo)
- [ ] Completar redaccion final de metodos y discusion
