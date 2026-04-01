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
- [ ] Protocolo realista final para reporte de tesis/paper

### 4. Interpolacion y reconstruccion
- [x] Wrapper unificado implementado (`interpolate_signals`)
- [x] Metodos por instante implementados
- [x] Metodos TV/tiempo implementados
- [x] Interfaz de entrada/salida estandarizada
- [x] Correccion paper-faithful de BGSRP y consolidacion de TRSS/sobolev_temporal

### 5. Evaluacion y comparacion
- [x] Metricas MAE, RMSE, DTW, SNR implementadas
- [x] Scripts de comparacion y optimizacion implementados
- [x] Resultados guardados en `results` con rankings y figuras
- [ ] Corrida final extendida con DTW completo en candidatas finales

### 6. Analisis y reporte
- [x] Conclusiones preliminares extraidas
- [ ] Consolidar tabla final baseline vs GSP vs TV/tiempo (media +- desviacion)
- [ ] Redactar version final de metodos, resultados y discusion

---

## Metodos implementados

### Grafos (src/graph_construction/graph_constructors.py)

- [x] `knn`  
  Referencia: Sakiyama et al. (2016)  
  Estado: paper-aligned (implementacion kNN estandar)

- [x] `knng`  
  Referencia: Sakiyama et al. (2016)  
  Estado: paper-aligned (kNN + kernel gaussiano en aristas)

- [x] `vknng`  
  Referencia: Tamaru et al. (2024)  
  Estado: adaptacion inspirada en literatura (k variable por nodo)

- [x] `gaussian`  
  Referencia: Karasuyama y Mamitsuka (2017)  
  Estado: baseline gaussiano denso

- [x] `epsilon_ball`  
  Referencia: Shuman et al. (2013)  
  Estado: baseline clasico epsilon-neighborhood

- [x] `mst`  
  Referencia: Ortega et al. (2018)  
  Estado: baseline topologico (minimum spanning tree)

- [x] `fully_connected_inverse_distance`  
  Referencia: baseline clasico (sin paper unico)

- [x] `nnk`  
  Referencia: Shekkizhar y Ortega (2020/2023)  
  Estado: paper-aligned (NNLS local + simetrizacion)

- [x] `aew`  
  Referencia: Karasuyama y Mamitsuka (2017)  
  Estado: implementacion inspirada en minimizacion local de reconstruccion

- [x] `kalofolias`  
  Referencia: Kalofolias (2016), Kalofolias et al. (2017)  
  Estado: aproximacion numerica interna (log-degree + norma Frobenius)

### Interpolacion por instante (src/interpolation_methods.py)

- [x] Baselines clasicos: `linear`, `nearest`, `mean`, `random`
- [x] Geometricos/RBF: `idw`, `spherical_spline`, `rbfi_tps`, `rbfi_mq`, `spline_surface`
- [x] GSP: `gsp`, `tikhonov`, `gsmooth`, `bgsrp`, `puy`, `sobolev`

Notas paper-faithful:
- `bgsrp`: actualizado a referencia primaria RKHS (Zhang et al., 2024) y estructura de algoritmo alineada a `gsp_BGSRP_recon.m`.
- `spherical_spline`: implementacion basada en formulacion de Perrin et al. (1989).

### Interpolacion TV/tiempo (src/interpolation_methods.py)

- [x] `graph_time_tikhonov`
- [x] `trss` (alias funcional: `sobolev_temporal`)
- [x] `tv`
- [x] `temporal_laplacian`
- [x] `heat_diffusion_temporal`
- [x] `spline_temporal`
- [x] `wavelet_temporal`
- [x] `directed_tv`
- [x] `adaptive_temporal`

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

- [ ] Ejecutar corrida final larga con DTW en candidatas top y mas ventanas temporales
- [ ] Congelar configuracion final por dataset para seccion experimental del paper
- [ ] Consolidar tabla final de comparacion (baseline vs GSP vs TV/tiempo)
- [ ] Completar redaccion final de metodos y discusion
