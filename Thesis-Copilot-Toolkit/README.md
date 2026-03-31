# Tesis: Reconstrucción de EEG usando GSP e Interpolación

## Hipótesis
El uso de técnicas de interpolación basadas en grafos (GSP) permite reconstruir señales de EEG de manera más precisa que los métodos clásicos.

## Objetivos
1. Implementar y comparar distintos métodos de construcción de grafos para EEG.
2. Implementar y comparar métodos de interpolación (GSP y clásicos).
3. Evaluar el desempeño usando métricas objetivas (MAE, DTW, etc.).
4. Redactar paper científico y tesis extendida.

## Pipeline general
1. Input: Señal EEG y localización de electrodos
2. Construcción de grafo (varios métodos)
3. Interpolación de electrodos faltantes (varios métodos)
4. Evaluación cuantitativa (métricas)
5. Comparación y análisis de resultados
6. Redacción de resultados y discusión

## Estructura de carpetas
- /experiments: scripts y notebooks de experimentos
- /src: implementación modular de métodos
- /results: resultados, logs, figuras
- /paper: borrador del paper
- /thesis: borrador de la tesis
- /backlog.md: lista de tareas y métodos