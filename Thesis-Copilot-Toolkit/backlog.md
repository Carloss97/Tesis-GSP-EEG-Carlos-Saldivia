## Pipeline experimental y de comparación

### 1. Preparación y carga de datos
- [ ] Descargar/preparar los 4 datasets seleccionados
- [ ] Estandarizar formato de señales y posiciones de electrodos
- [ ] Implementar scripts de carga y preprocesamiento en /src/data/

### 2. Construcción de grafos
- [ ] Implementar función wrapper para seleccionar método de grafo
- [ ] Generar y guardar matrices de adyacencia para cada dataset
- [ ] Validar visualmente y numéricamente los grafos generados

### 3. Simulación de canales faltantes
- [ ] Definir protocolos de enmascaramiento (aleatorio, sistemático, realista)
- [ ] Implementar función para simular canales faltantes en señales

### 4. Interpolación/reconstrucción
- [ ] Implementar función wrapper para seleccionar método de interpolación
- [ ] Ejecutar reconstrucción para cada combinación de grafo, interpolador y dataset
- [ ] Guardar señales reconstruidas y parámetros usados

### 5. Evaluación y comparación
- [ ] Calcular métricas (MAE, DTW, RMSE, SNR) para cada experimento
- [ ] Generar tablas y figuras comparativas
- [ ] Automatizar ranking de métodos por métrica

### 6. Análisis y reporte
- [ ] Analizar resultados y extraer conclusiones
- [ ] Redactar secciones de resultados y discusión para paper y tesis

## Datasets seleccionados para experimentos

1. **MNE Sample Dataset**
	- Origen: mne.datasets.sample
	- Características: EEG/MEG multimodal, eventos auditivos y visuales, formato .fif, montajes 3D.
2. **PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB)**
	- Origen: PhysioNet, vía mne.datasets.eegbci
	- Características: 109 sujetos, tareas motoras, 64 electrodos, formato .edf.
3. **Dataset sintético propio**
	- Origen: Generado artificialmente para validación controlada de métodos.
	- Características: Permite definir posiciones, canales faltantes y señales conocidas.
4. **BCI Competition IV Dataset 2a**
	- Origen: BCI Competition IV (https://www.bbci.de/competition/iv/)
	- Características: EEG de 9 sujetos, 22 canales, tareas de imaginación motora, formato .gdf.

---

## Protocolos de entrada/salida para métodos

### Entrada estándar para métodos de construcción de grafo
- Matriz de posiciones de electrodos: shape (N_electrodos, 3) para coordenadas 3D (o 2D si aplica)
- (Opcional) Matriz de señales EEG: shape (N_instantes, N_electrodos) para métodos data-driven
- Parámetros específicos del método (k, sigma, etc.)

### Salida estándar de métodos de construcción de grafo
- Matriz de adyacencia (N_electrodos, N_electrodos), formato denso o disperso
- (Opcional) Matriz de pesos o afinidades

### Entrada estándar para métodos de interpolación
- Señal EEG incompleta: vector (N_electrodos,) o matriz (N_instantes, N_electrodos) con NaN en canales faltantes
- Grafo (matriz de adyacencia) correspondiente
- (Opcional) Parámetros del método (regularización, kernel, etc.)

### Salida estándar de métodos de interpolación
- Señal EEG reconstruida: vector o matriz del mismo shape que la entrada, con valores estimados en los canales faltantes
- (Opcional) Métricas de error si se compara con señal original

## Organización general del pipeline experimental y de comparación

### 1. Preparación de datos
- [ ] Selección y preprocesamiento de datasets EEG
- [ ] Estandarización de formatos de entrada (señales, posiciones de electrodos)
- [ ] División en conjuntos de entrenamiento, validación y prueba (si aplica)

### 2. Construcción de grafos
- [ ] Implementar y validar todos los métodos de construcción de grafo listados
- [ ] Documentar parámetros y supuestos de cada método

### 3. Interpolación/reconstrucción de señales
- [ ] Implementar y validar todos los métodos de interpolación listados
- [ ] Definir protocolos para simular canales faltantes o dañados
- [ ] Estandarizar la interfaz de entrada/salida de los métodos

### 4. Evaluación y comparación
- [ ] Implementar scripts/notebooks para comparar métodos de grafo e interpolación
- [ ] Calcular métricas (MAE, DTW, RMSE, SNR, etc.) para cada combinación
- [ ] Generar tablas y figuras comparativas
- [ ] Guardar resultados en /results

### 5. Análisis y redacción
- [ ] Analizar resultados y extraer conclusiones
- [ ] Redactar secciones de métodos, resultados y discusión para paper y tesis

## Backlog de Métodos y Experimentos

### Métodos de construcción de grafo a implementar
- Distancia euclidiana entre electrodos
- Kernel gaussiano (global, local scaling, median scaling)
- kNNG (k-Nearest Neighbor Graph)
- vkNNG (variable k-Nearest Neighbor Graph)
- NNK (Non-Negative Kernel Graph)
- Adaptive Edge Weighting (AEW)
- Kaliofólias (optimización de grafos)
- knn_graph y nnk_graph (PyNNK)
- Basados en datos: covarianza, correlación
- Afinidad basada en kernel
- Otros (especificar)

### Métodos de interpolación
- Interpolación Laplaciana (GSP)
- Interpolación Tikhonov (regularización en grafo)
- Interpolación BGSRP (Bandlimited Graph Signal Reconstruction Problem)
- Interpolación Graph Regularization (gsmooth)
- Interpolación Graph-Time Tikhonov
- Interpolación Qiu batch
- Interpolación Puy
- Interpolación Sobolev
- Interpolación NNI (Natural Neighbor Interpolation)
- Interpolación por Spherical Spline
- RBFI TPS (Radial Basis Function Interpolation, Thin Plate Spline)
- RBFI MQ (Multiquadric)
- Spline Superficie
- Métodos clásicos (ej: interpolación lineal, spline)
- Otros métodos GSP (especificar)

### Métricas de evaluación
- MAE (Mean Absolute Error)
- DTW (Dynamic Time Warping)
- RMSE (Root Mean Square Error)
- SNR (Signal-to-Noise Ratio)
- Otras métricas relevantes

### Experimentos clave
- Reconstrucción de un instante de tiempo
- Reconstrucción de la señal completa
- Comparación baseline vs GSP
- Variación de parámetros y optimización


### Tareas detalladas y criterios de éxito

#### 1. Implementar método de grafo: Distancia euclidiana
- [ ] Definir formato de entrada (coordenadas de electrodos)
- [ ] Calcular matriz de distancias euclidianas
- [ ] Generar matriz de adyacencia (opcional: umbralizar o normalizar)
- [ ] Escribir función en /src/graph_construction/euclidean.py
- [ ] Crear test unitario para validar matriz
- [ ] Documentar uso y parámetros

#### 2. Implementar método de grafo: Kernel gaussiano
- [ ] Definir sigma y parámetros del kernel
- [ ] Calcular matriz de afinidad usando kernel gaussiano sobre distancias
- [ ] Escribir función en /src/graph_construction/gaussian.py
- [ ] Crear test unitario para validar matriz
- [ ] Documentar uso y parámetros

#### 3. Implementar método de grafo: Basado en covarianza/correlación
- [ ] Definir formato de entrada (matriz de señales EEG)
- [ ] Calcular matriz de covarianza/correlación
- [ ] Generar matriz de adyacencia
- [ ] Escribir función en /src/graph_construction/covariance.py
- [ ] Crear test unitario para validar matriz
- [ ] Documentar uso y parámetros

#### 4. Implementar interpolación Laplaciana (GSP)
- [ ] Definir entrada: grafo y señales con canales faltantes
- [ ] Implementar algoritmo de interpolación Laplaciana
- [ ] Escribir función en /src/interpolation/laplacian.py
- [ ] Crear test unitario con datos sintéticos
- [ ] Documentar uso y parámetros

#### 5. Implementar baseline clásico (ej: interpolación lineal)
- [ ] Definir entrada: señales con canales faltantes
- [ ] Implementar interpolación lineal/spline
- [ ] Escribir función en /src/interpolation/classic.py
- [ ] Crear test unitario con datos sintéticos
- [ ] Documentar uso y parámetros

#### 6. Crear pipeline de evaluación
- [ ] Definir estructura de pipeline (input → grafo → interpolación → métrica)
- [ ] Implementar script/notebook en /experiments/
- [ ] Permitir selección de métodos y parámetros
- [ ] Guardar resultados en /results/
- [ ] Crear test de integración

#### 7. Redactar sección de métodos en el paper
- [ ] Esquematizar secciones y subsecciones
- [ ] Redactar descripción de cada método implementado
- [ ] Incluir figuras/tablas de ejemplo

#### 8. Evaluar y comparar resultados
- [ ] Ejecutar pipeline para todas las combinaciones relevantes
- [ ] Analizar resultados y extraer conclusiones
- [ ] Generar tablas/figuras para el paper y la tesis