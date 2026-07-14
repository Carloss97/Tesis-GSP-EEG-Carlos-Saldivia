# Tesis GSP-EEG — Carlos Saldivia

Repositorio público asociado a la tesis de magíster:

**Reconstrucción de Canales EEG Faltantes Mediante Procesamiento de Señales en Grafos con Regularización Temporal**

Autor: Carlos Saldivia Heinz  
Institución: Universidad Técnica Federico Santa María, Departamento de Electrónica

## Contenido público curado

Este repositorio conserva solo el material necesario para entender y reproducir la investigación documentada en la tesis:

- `Thesis-Copilot-Toolkit/src/`: implementación modular de construcción de grafos, interpolación y evaluación.
- `Thesis-Copilot-Toolkit/scripts/`: utilidades de análisis y generación de tablas/resultados derivados.
- `Thesis-Copilot-Toolkit/experiments/`: scripts y configuraciones de experimentos reproducibles.
- `Thesis-Copilot-Toolkit/docs/`: notas metodológicas y políticas de datos.
- `Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2/`: fuente LaTeX, figuras finales, tablas finales, scripts generadores y PDF de tesis.
- `PUBLICATION_MANIFEST.md`: criterio de inclusión/exclusión para la versión pública.

## Qué no se versiona

Para que el repositorio sea público, auditable y liviano, se excluyen:

- datasets crudos o redistribución de bases externas;
- resultados intermedios, caches y ejecuciones exploratorias masivas;
- carpetas personales de trabajo, papers descargados y PDFs de referencia;
- auxiliares de compilación LaTeX y entornos virtuales.

Los datasets usados en la tesis son públicos, pero deben descargarse desde sus fuentes originales respetando sus licencias y términos de uso.

## Compilar la tesis

Desde el directorio de la tesis:

```bash
cd Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2
latexmk -pdf -interaction=nonstopmode tesis_completa.tex
```

También existe un driver parcial para capítulos 1--4:

```bash
latexmk -pdf -interaction=nonstopmode tesis_caps_1_4.tex
```

## Validación estructural

```bash
cd Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2
python3 scripts/validate_thesis.py
```

## Estado del repositorio

Este repositorio no incluye los datos crudos ni todos los resultados generados; conserva el código, los artefactos finales de tesis y la documentación necesaria para revisar la metodología. Las afirmaciones cuantitativas del documento se trazan a tablas, figuras y scripts descritos en la tesis y sus apéndices.

## Licencia

No se declara una licencia abierta por defecto. Para reutilización de código, texto o figuras, contactar al autor o añadir una licencia explícita antes de distribución derivada.
