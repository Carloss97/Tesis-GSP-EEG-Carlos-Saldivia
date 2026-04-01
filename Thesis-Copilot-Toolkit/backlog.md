## Backlog Consolidado

## Estado general

### 1. Preparación y carga de datos
- [x] Descargar y preparar datasets principales
- [x] Estandarizar formato de señales y posiciones
- [x] Implementar carga y preprocesamiento en src/data
- [ ] Definir división entrenamiento/validación/prueba para validación final

### 2. Construcción de grafos
- [x] Wrapper de selección de método implementado
- [x] Métodos principales implementados y validados en corridas
- [x] Matrices de adyacencia generadas en experimentos
- [ ] Cierre de validación paper-faithful para todos los métodos secundarios

### 3. Simulación de canales faltantes
- [x] Enmascaramiento aleatorio implementado
- [x] Enmascaramiento sistemático implementado
- [ ] Protocolo realista final para reporte de tesis/paper

### 4. Interpolación y reconstrucción
- [x] Wrapper unificado implementado
- [x] Métodos por instante implementados
- [x] Métodos TV/tiempo implementados
- [x] Interfaz de entrada/salida estandarizada
- [ ] NNI exacto con backend natural-neighbor en este entorno

### 5. Evaluación y comparación
- [x] Métricas MAE, RMSE, DTW, SNR implementadas
- [x] Scripts de comparación y optimización implementados
- [x] Resultados guardados en results con rankings y figuras
- [ ] Corrida final extendida con DTW completo en candidatas finales

### 6. Análisis y reporte
- [x] Conclusiones preliminares extraídas
- [ ] Consolidar tabla final baseline vs GSP vs TV/tiempo (media +- desviación)
- [ ] Redactar versión final de métodos, resultados y discusión

---

## Métodos implementados

### Grafos
- [x] knn
- [x] knng
- [x] vknng
- [x] gaussian
- [x] epsilon_ball
- [x] mst
- [x] fully_connected_inverse_distance
- [x] nnk (backend interno NNLS + fallback opcional)
- [x] aew
- [x] kalofolias (optimización interna log-degree)

### Interpolación por instante
- [x] linear
- [x] nearest
- [x] mean
- [x] random
- [x] idw
- [x] nni (fallback local cuando backend exacto no está disponible)
- [x] spherical_spline
- [x] rbfi_tps
- [x] rbfi_mq
- [x] spline_surface
- [x] gsp
- [x] tikhonov
- [x] bgsrp
- [x] gsmooth
- [x] qiu_batch
- [x] puy
- [x] sobolev

### Interpolación TV/tiempo
- [x] graph_time_tikhonov
- [x] trss
- [x] tv

---

## Criterios de éxito (estado)

- [x] Cada método de grafo retorna adyacencia simétrica, no negativa y diagonal cero
- [x] Métodos data-driven aceptan señales y generan grafos válidos
- [x] Métodos de interpolación aceptan NaN y retornan mismo shape de entrada
- [x] Separación de familias de reconstrucción para análisis (instant y tv_time)
- [x] Optimización de parámetros en grilla ejecutable
- [x] Ranking global y ranking por familia disponibles
- [ ] Validación final de robustez con DTW completo en candidatas finales

---

## Datasets objetivo

- [x] MNE Sample Dataset
- [x] PhysioNet EEGMMIDB (loader implementado)
- [x] Sintético propio
- [x] BCI Competition IV 2a (loader implementado)
- [ ] Integrar de forma estable todos los datasets en corrida final unificada

---

## Evidencia de resultados ya generada

- [x] results/paper_faithful_results.csv
- [x] results/paper_faithful_rank_mae.csv
- [x] results/opt_benchmark_full.csv
- [x] results/opt_benchmark_rank_all.csv
- [x] results/opt_benchmark_best_by_family.csv
- [x] results/opt_benchmark_mean_by_method.csv
- [x] results/robust_top10_runs.csv
- [x] results/robust_top10_summary.csv
- [x] results/mae_by_method_dataset.png
- [x] results/heatmap_mae_method_graph.png
- [x] results/heatmap_snr_method_graph.png
- [x] results/opt_family_mae_boxplot.png
- [x] results/opt_heatmap_mae_graph_method.png

---

## Pendientes inmediatos de cierre

- [ ] Ejecutar corrida final larga con DTW en candidatas top y más ventanas temporales
- [ ] Congelar configuración final por dataset para sección experimental del paper
- [ ] Consolidar tabla final de comparación (baseline vs GSP vs TV/tiempo)
- [ ] Completar redacción final de métodos y discusión
