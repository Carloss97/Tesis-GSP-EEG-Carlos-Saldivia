# Build Summary — Hermes v2 Tesis Magíster

Generated: 2026-05-21

## Documents

| Document | Pages | Size | Undefined Citations | Status |
|----------|-------|------|---------------------|--------|
| tesis_completa.pdf | 107 | 3.96 MB | 0 | PASS |
| tesis_caps_1_5.pdf | 55 | 587 KB | 11 (expected: forward refs to ch6-8, appendices) | PASS |

## Compilation

- Engine: pdfLaTeX (TeX Live 2026 via TinyTeX)
- BibTeX: IEEEtran.bst
- Passes: pdflatex → bibtex → pdflatex × 2
- All citations resolved (0 undefined in full version)

## Content Stats

- TeX files loaded: 28 (full), 12 (short)
- Words (approx): 16,494 (full), 9,855 (short)
- Figures: 17 (full, all PNG), 2 (short, PDF diagrams)
- Citations: 25 unique cite keys, all resolved
- Labels: 80 (full), 32 (short)
- No duplicate labels
- No missing inputs
- No missing figures

## File Inventory

```
tesis_magister_gsp_eeg_v2/
  tesis_completa.tex          (1.1 KB) — full thesis driver
  tesis_caps_1_5.tex          (0.7 KB) — short version driver
  config/
    packages.tex              (1.8 KB) — LaTeX packages
    metadata.tex              (1.1 KB) — author, title, institution
    results_data.tex          (1.6 KB) — quantitative result macros
  chapters/
    01_introduccion.tex       (26.5 KB) — intro, chronology, MNE section, AI mention
    02_marco_teorico.tex      (27.8 KB) — EEG fundamentals, GSP, state of art, MNE internals
    03_metodologia.tex        (18.9 KB) — datasets, 18 methods, metrics, Optuna, confirmatory protocol
    04_arquitectura_y_trazabilidad.tex (6.2 KB) — pipeline architecture, traceability
    05_diseno_experimental.tex (7.8 KB) — experimental design, hypotheses, statistical plan
    06_resultados.tex         (20.5 KB) — global comparison, degradation, ERPs, PSD, ablation, MNE benchmark
    07_discusion.tex          (11.5 KB) — hypothesis validation, mechanisms, limitations
    08_conclusiones.tex        (7.8 KB) — 5 conclusions, 6 future work lines
  appendices/
    A_derivaciones.tex        (5.1 KB) — mathematical derivations
    B_tablas_extensas.tex     (1.9 KB) — extended result tables
    C_reproducibilidad.tex    (3.1 KB) — reproducibility protocol
    D_inventario_artefactos.tex (4.2 KB) — artifact inventory
    E_apendice_tablas_originales_adaptado.tex (1.4 KB) — historical tables
  frontmatter/                — cover, title, approval, abstracts, acknowledgements
  figures/                    — 19 PNGs + 2 PDFs (all local)
  tables/                     — LaTeX tables + CSV data
  bibliography/references.bib — 62 entries (43 original + 19 added)
  scripts/validate_thesis.py  — automated validation
  Makefile, compile.sh, README.md
