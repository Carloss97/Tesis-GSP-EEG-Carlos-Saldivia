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

## Arquitectura documental (paper y tesis)

### Componentes
- `paper/ieee/main.tex`: punto de entrada del paper en formato IEEE.
- `paper/ieee/sections/*`: unidades modulares para escritura colaborativa.
- `thesis/usm/main.tex`: punto de entrada de la tesis en formato base LaTeX.
- `thesis/usm/frontmatter/*`: portada, resumenes y secciones preliminares.
- `thesis/usm/chapters/*`: capitulos de desarrollo de la investigacion.
- `*/bibliography/references.bib`: bibliografias separadas por entregable.

### Flujo de datos documental
- Resultados cuantitativos en `results/` -> seleccion de evidencia -> tablas/figuras de LaTeX -> redaccion de resultados y discusion.

### Riesgos documentales
- Divergencia entre paper y tesis en cifras reportadas.
- Inconsistencia de claves BibTeX entre entregables.
- Cambios tardios en formato institucional.

### Mitigacion documental
- Definir una politica de trazabilidad resultado-a-artefacto.
- Mantener sincronizada la base bibliografica por claves estables.
- Partir con plantilla compilable base y ajustar luego al formato institucional final.
