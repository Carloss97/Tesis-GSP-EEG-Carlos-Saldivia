# Dependencias y riesgos del pipeline EEG-GSP

## Dependencias
- Librerías de procesamiento de señales y EEG: numpy, scipy, mne, pandas.
- Implementaciones de métodos de grafos: networkx, PyGSP, PyNNK (si aplica).
- Datasets públicos: acceso a MNE, PhysioNet, BCI Competition IV.
- Scripts de visualización: matplotlib, seaborn.
- Estandarización de formatos de datos entre datasets.

## Riesgos
- Formatos de datasets heterogéneos: riesgo de incompatibilidad o pérdida de información.
- Complejidad en la implementación de métodos avanzados (NNK, GSP): riesgo de errores sutiles o falta de soporte.
- Volumen de datos: riesgo de tiempos de cómputo elevados.
- Validación insuficiente: riesgo de resultados no reproducibles o poco robustos.
- Dependencia de librerías externas: riesgo de cambios o deprecaciones.

## Mitigación
- Priorizar pruebas unitarias y scripts de validación en cada fase.
- Documentar claramente los formatos de entrada/salida.
- Modularizar el código para facilitar cambios y pruebas.
- Mantener versiones fijas de dependencias críticas.
