# Requisitos del pipeline de reconstrucción EEG (EARS)

## 1. Preparación y carga de datos
- WHEN el usuario selecciona un dataset, THE SYSTEM SHALL cargar y estandarizar las señales EEG y las posiciones de electrodos en un formato común.
- WHEN se cargan los datos, THE SYSTEM SHALL permitir acceder a las señales y posiciones desde un módulo único (/src/data/).

## 2. Construcción de grafos
- WHEN se solicita construir un grafo, THE SYSTEM SHALL permitir seleccionar el método de construcción (distancia, kNN, NNK, etc.).
- WHEN se construye el grafo, THE SYSTEM SHALL generar y guardar la matriz de adyacencia correspondiente.
- WHEN se construye el grafo, THE SYSTEM SHALL validar visualmente y numéricamente la estructura generada.

## 3. Simulación de canales faltantes
- WHEN se requiere simular canales faltantes, THE SYSTEM SHALL permitir definir el protocolo de enmascaramiento (aleatorio, sistemático, realista).
- WHEN se aplica el enmascaramiento, THE SYSTEM SHALL modificar las señales EEG introduciendo NaN en los canales seleccionados.

## 4. Interpolación/reconstrucción
- WHEN se solicita interpolar, THE SYSTEM SHALL permitir seleccionar el método de interpolación (GSP, clásico, etc.).
- WHEN se ejecuta la interpolación, THE SYSTEM SHALL reconstruir los canales faltantes y guardar los resultados.

## 5. Evaluación y comparación
- WHEN se dispone de señales originales y reconstruidas, THE SYSTEM SHALL calcular métricas de desempeño (MAE, DTW, RMSE, SNR).
- WHEN se calculan las métricas, THE SYSTEM SHALL generar tablas y figuras comparativas y un ranking automatizado de métodos.

## 6. Análisis y reporte
- WHEN se completan los experimentos, THE SYSTEM SHALL facilitar la extracción de conclusiones y la redacción de resultados para paper y tesis.
