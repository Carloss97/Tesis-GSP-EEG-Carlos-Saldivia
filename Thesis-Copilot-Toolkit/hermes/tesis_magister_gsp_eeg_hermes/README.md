# Tesis de Magíster generada por Hermes

Carpeta independiente: `hermes/tesis_magister_gsp_eeg_hermes`

Archivo principal: `tesis_magister_hermes.tex`

## Compilación sugerida

```bash
cd /mnt/c/Users/sarlo/OneDrive/Escritorio/Proyectos/Tesis-GSP-EEG-Carlos-Saldivia/Thesis-Copilot-Toolkit/hermes/tesis_magister_gsp_eeg_hermes
latexmk -pdf -interaction=nonstopmode tesis_magister_hermes.tex
```

Si no hay `latexmk` disponible:

```bash
pdflatex -interaction=nonstopmode tesis_magister_hermes.tex
bibtex tesis_magister_hermes
pdflatex -interaction=nonstopmode tesis_magister_hermes.tex
pdflatex -interaction=nonstopmode tesis_magister_hermes.tex
```

## Estructura

- `config/`: paquetes, metadatos y macros de resultados copiadas localmente.
- `frontmatter/`: portada, resumen, abstract, agradecimientos.
- `chapters/`: capítulos principales.
- `appendices/`: derivaciones, tablas extensas, reproducibilidad e inventario de artefactos.
- `figures/`: figuras copiadas desde resultados finales/baselines.
- `tables/`: tablas generadas o copiadas para uso autónomo del documento.
- `bibliography/`: BibTeX propio del documento.

## Nota

Este documento se generó como borrador extenso de nivel de magíster. Antes de entrega formal se debe revisar estilo institucional USM, nombres de comisión, numeración final de páginas y consistencia visual tras compilar.
