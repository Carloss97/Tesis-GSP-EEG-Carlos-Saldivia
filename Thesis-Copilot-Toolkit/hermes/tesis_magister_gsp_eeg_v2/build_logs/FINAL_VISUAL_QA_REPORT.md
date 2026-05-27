# Final visual QA report — strict figure/table pass

## Scope

Strict follow-up pass requested after visible defects remained in figures/tables, especially:

- Fig. 2.2: panel (a) clipped, panel (c) text/flecha layout broken.
- Fig. 3.1: bubbles too close and final bubble text/arrow spacing issues.
- Fig. 6.2: cost-title/value overlap in the right panel.
- Global review of all generated figures and tables.

## Main fixes applied

### Fig. 2.2 — GSP concepts

Regenerated `figures/ch2_gsp_concepts_clean.pdf` with a new layout:

- two-row layout instead of a cramped 1x3 layout;
- panel (a) has explicit margins so the head/grafo circle is not clipped;
- panel (c) is a full-width lower lane diagram;
- all boxes use short labels;
- arrows are routed between boxes, not through text;
- no text leaves its box.

QA result: approved by dedicated vision inspection and full-sheet inspection.

### Fig. 3.1 — Methodology flow

Regenerated `figures/ch3_methodology_flow.pdf`:

- wider canvas;
- separated boxes;
- larger final control box;
- arrows rerouted outside text and box interiors;
- more bottom margin.

QA result: approved by dedicated vision inspection and full-sheet inspection.

### Fig. 6.2 — Metric portfolio / temporal cost

Regenerated `figures/ch6_metric_portfolio_improvement.pdf`:

- right panel changed to horizontal bars on log-scale;
- title changed to `Costo temporal` without numeric value in the title;
- value labels moved away from the title;
- reduced minor-grid clutter;
- increased right-panel width.

QA result: approved by dedicated vision inspection and full-sheet inspection.

### PSD qualitative figure

`figures/res_opt_final__best_psd_comparison_clean.png` was replaced by a padded original rendering to avoid:

- bad UTF-8 rendering in PIL title text;
- title/subtitle crowding;
- legend/ticks near the edge;
- apparent cut-off in contact-sheet QA.

QA result: approved on the final sheet and on the final compiled pages 56--61.

### Decision map

Regenerated `figures/ch7_decision_map.pdf`:

- simplified y-axis labels;
- increased margins;
- separated frontier label from region labels;
- reduced lower-left label crowding.

QA result: approved.

### Neurophysiology figure

Regenerated `figures/capitulo2_origen_eeg.pdf` with a cleaner project-local script:

- larger text;
- cleaner topography annotations;
- less crowded subpanels;
- better margins.

QA result: approved in the final full-figure sheet and page preview.

## Validation commands executed

```bash
python3 scripts/validate_thesis.py > build_logs/validate_after_final_visual_polish.log 2>&1
latexmk -pdf -interaction=nonstopmode tesis_completa.tex > build_logs/compile_after_final_visual_polish.log 2>&1
/tmp/thesis_fig_venv/bin/python scripts/visual_qa_previews.py > build_logs/visual_qa_after_final_visual_polish.log 2>&1
```

## Final compilation status

- `latexmk` exit code: 0
- PDF generated: yes
- PDF: `tesis_completa.pdf`
- Pages: 80
- Size: 1,136,802 bytes
- Static thesis validator: PASS
- LaTeX errors: 0
- Undefined citations: 0
- Undefined references: 0
- Overfull hboxes total: 1
- Overfull hboxes >10pt: 0

Only remaining overfull:

```text
Overfull \hbox (2.28114pt too wide) in paragraph at lines 54--66
```

This is below the critical/visible threshold.

## Final visual QA

Final contact sheets reviewed:

- `build_logs/visual_qa/figures_sheet_1.png`: approved.
- `build_logs/visual_qa/figures_sheet_2.png`: approved.
- `build_logs/visual_qa/figures_sheet_3.png`: approved.
- `build_logs/visual_qa/pages_theory_methods_12_31.png`: approved.
- `build_logs/visual_qa/pages_results_33_46.png`: approved.
- `build_logs/visual_qa/pages_discussion_conclusion_47_57.png`: approved.
- `build_logs/visual_qa/pages_56_61_final.png`: approved, including Fig. 6.8, Fig. 6.9, Tabla 6.2 and Fig. 6.10.

Final verdict: no serious remaining visual problems detected in figures or tables.
