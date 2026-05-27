# Build Summary — tesis_magister_gsp_eeg_v2

Fecha: 2026-05-27T10:36:09-04:00

## Estado

- `tesis_completa.tex`: compila correctamente.
- `tesis_caps_1_5.tex`: compila correctamente.
- Validación estática (`python3 scripts/validate_thesis.py`): PASS para ambos drivers.

## PDFs generados

- `tesis_completa.pdf`: 73 páginas, 1,412,920 bytes.
- `tesis_caps_1_5.pdf`: 43 páginas, 469,181 bytes.

## Calidad del log LaTeX

| Documento | Errores | Citas indefinidas | Referencias indefinidas | Overfull total | Overfull >10pt |
|---|---:|---:|---:|---:|---:|
| `tesis_completa` | 0 | 0 | 0 | 5 | 0 |
| `tesis_caps_1_5` | 0 | 0 | 0 | 4 | 0 |

## Cambios principales de esta pasada

- Reescritura de `chapters/06_resultados.tex`, `chapters/07_discusion.tex` y `chapters/08_conclusiones.tex` con narrativa condicional TRSS vs MNE.
- Generación de tablas y figuras trazables para capítulos prácticos desde `results/trss_vs_mne_bads_extensive/` y ablation CSVs.
- Actualización de abstracts ES/EN para evitar dominancia universal y reportar números confirmatorios.
- Corrección de `tesis_completa.tex` para usar `appendices/C_reproducibilidad.tex`.
- Eliminación del duplicado BibTeX `gramfort2013meg`.
- Mejora de `scripts/validate_thesis.py` para resolver `\include{}` además de `\input{}` y detectar claves BibTeX duplicadas.
