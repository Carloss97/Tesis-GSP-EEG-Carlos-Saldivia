# Plan de trabajo incremental para el pipeline EEG-GSP

## Fase 1: Preparación y carga de datos
- Implementar scripts de carga y estandarización para los 4 datasets en /src/data/.
- Validar acceso uniforme a señales y posiciones de electrodos.

## Fase 2: Construcción de grafos
- Implementar función wrapper para seleccionar método de grafo.
- Implementar al menos 2 métodos base (distancia euclidiana y kNN).
- Validar y guardar matrices de adyacencia.

## Fase 3: Simulación de canales faltantes
- Implementar función para enmascarar canales (aleatorio y sistemático).
- Validar que los NaN se introducen correctamente.

## Fase 4: Interpolación/reconstrucción
- Implementar función wrapper para seleccionar método de interpolación.
- Implementar al menos 2 métodos base (GSP y lineal clásico).
- Validar reconstrucción y guardar resultados.

## Fase 5: Evaluación y comparación
- Implementar cálculo de métricas (MAE, DTW, RMSE, SNR).
- Automatizar generación de tablas, figuras y ranking.

## Fase 6: Análisis y reporte
- Documentar resultados y pipeline.
- Redactar secciones de resultados y discusión.

## Fase 7: Estructura editorial paper/tesis
- Crear base LaTeX modular para paper en formato IEEE.
- Crear base LaTeX modular para tesis en formato institucional (base report + adaptacion USM).
- Definir workflow de fuentes bibliograficas y convenciones de lenguaje por entregable.
- Definir checklist de cierre para pre-submission del paper y entrega de tesis.

---

Cada fase debe incluir pruebas mínimas y scripts de ejemplo en /experiments. El avance es incremental: no avanzar a la siguiente fase sin pruebas básicas de la anterior.