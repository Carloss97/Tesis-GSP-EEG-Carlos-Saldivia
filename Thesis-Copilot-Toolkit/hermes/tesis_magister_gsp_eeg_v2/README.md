# Tesis de Magíster — Hermes v2

Workspace autocontenido para la tesis de magíster:
**"Reconstrucción de Canales EEG Faltantes mediante Procesamiento de Señales en Grafos con Regularización Temporal"**

## Archivos principales

| Archivo | Contenido |
|---------|-----------|
| `tesis_completa.tex` | Tesis completa: 8 capítulos + 5 apéndices + bibliografía |
| `tesis_caps_1_5.tex` | Versión recortada: capítulos 1--5 (desde introducción hasta diseño experimental), para revisión del profesor |

## Compilación

```bash
cd /mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia/Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_v2

# Opción 1: latexmk
latexmk -pdf -interaction=nonstopmode tesis_completa.tex

# Opción 2: manual
pdflatex -interaction=nonstopmode tesis_completa.tex
bibtex tesis_completa
pdflatex -interaction=nonstopmode tesis_completa.tex
pdflatex -interaction=nonstopmode tesis_completa.tex
```

## Validación

```bash
python3 scripts/validate_thesis.py
```

O con Make:

```bash
make validate
make pdf
```

## Estructura

```
tesis_magister_gsp_eeg_v2/
  config/             # packages.tex, metadata.tex, results_data.tex (fuente única de verdad)
  frontmatter/        # portada, resumen, abstract, agradecimientos
  chapters/           # 8 capítulos + 5 apéndices
  figures/            # gráficos generados (PNG raster + PDF vectorial)
  tables/             # tablas LaTeX y datos CSV
  bibliography/       # archivo .bib autocontenido
  scripts/            # validate_thesis.py + helpers
  build_logs/         # registros de compilación y validación
```

## Notas

- Workspace 100% autocontenido: no depende de archivos fuera de este directorio.
- Todas las rutas de \\input e \\includegraphics son locales.
- Macros de resultados en `config/results_data.tex` — actualizar ahí cuando se obtengan nuevos resultados numéricos.
- Para compilar se requiere TinyTeX (user-local en WSL: `~/.TinyTeX`) o TeX Live completo con `latexmk`, `pdflatex`, `bibtex`.

## Generado por

Hermes Agent usando el skill `research-paper-writing` de Orchestra Research.
