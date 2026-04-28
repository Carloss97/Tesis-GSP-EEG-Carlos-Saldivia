# PHASE 6: PAPER-THESIS MAPPING MATRIX
**Created**: 2026-04-27
**Purpose**: Record the section-level correspondence between the paper and the thesis for synchronization review.

## 6.1 Structural Mapping

| Paper | Thesis | Status | Notes |
|---|---|---|---|
| `abstract.tex` | `01_introduccion.tex` opening summary + thesis intro framing | Aligned | Same high-level contribution story; thesis is longer and more contextual. |
| `introduction.tex` | `01_introduccion.tex` | Aligned | Same motivation, GSP framing, and contribution set; thesis adds broader background and objectives. |
| `related_work.tex` | `02_marco_teorico.tex` | Aligned | Thesis expands the theory and adds more Spanish-language exposition. |
| `methods.tex` | `03_metodologia.tex` | Aligned | Same method families, graph construction, and optimization story; thesis is more detailed. |
| `experiments.tex` | `04_experimentos_y_resultados.tex` | Aligned | Same datasets, metrics, and evaluation structure; thesis contains more granular tables and Spanish labels. |
| `results.tex` | `04_experimentos_y_resultados.tex` | Aligned after Phase 6 edits | Trial-level counts now match the regenerated 11-method / 55-comparison analysis. |
| `discussion.tex` | `05_discusion.tex` | Aligned | Thesis adds more interpretive and contextual detail. |
| `conclusion.tex` | `06_conclusiones_y_trabajo_futuro.tex` | Aligned after Phase 6 edits | Trial-level validation narrative now reflects the excluded visibility-based outlier. |
| `reproducibility.tex` | Appendix and methodological notes in thesis | Partially aligned | Paper has a compact reproducibility section; thesis distributes the material across methodology and appendix. |

## 6.2 Numeric Consistency Review

### Confirmed consistent
- Datasets: PhysioNet, BCI IV 2a, MNE Sample
- Core evaluation metrics: MAE, RMSE, DTW, SNR, LSD, Coherence
- Phase 3 raw aggregation: 736 iterations, 4,336 aggregated samples
- Phase 5 bibliography state: paper 23 cited entries, thesis 41 cited entries, 0 missing citations, 0 unused entries

### Corrected in Phase 6
- Trial-level comparison count: 55 comparisons after excluding the visibility-based outlier
- Method count in the trial-level summary: 11 methods
- Visibility-based outlier: retained only as a decision note, not as a comparative result

## 6.3 Narrative Alignment Notes

- Paper and thesis now tell the same story about the trial-level ranking: temporal and spatial-temporal methods form the top tier, while the visibility-based method is excluded from the published comparison set.
- The paper remains concise and metric-focused; the thesis keeps the more explanatory Spanish narrative, but the claims and numbers now match.
- No additional substantive paper-only or thesis-only claims were introduced in this phase.

## 6.4 Validation Summary

- Paper and thesis were edited to remove stale 12-method / 66-comparison references.
- Phase 6 now has a documented mapping, numeric alignment, and narrative alignment record.
- Final compilation validation is the next step before closing Phase 6.
