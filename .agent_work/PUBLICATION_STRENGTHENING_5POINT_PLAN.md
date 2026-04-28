# Publication Strengthening: 5-Point Strategic Plan

**Date Created**: 2026-04-28  
**Current Branch**: `publication-strengthening`  
**Target Venues**: IEEE Transactions on Biomedical Engineering, IEEE Transactions on Signal Processing (Tier 1)  
**Confidence Level**: High (based on completed Phase 3–7 validations and latency synchronization)

---

## Executive Summary

This plan outlines five strategic improvements to increase publication acceptance probability for tier-1 IEEE venues. The manuscript currently positions itself as a rigorous benchmark study with fair hyperparameter tuning across 11 interpolation methods. The plan strengthens this positioning by:

1. **Clarifying the intellectual contribution** (emphasize methodology rigor, not algorithm novelty)
2. **Explicitly stating study scope** (benchmark paper, not universal superiority claim)
3. **Maintaining consistent narrative** (fair comparison framework throughout)
4. **Adding practical robustness evidence** (sensitivity/ablation to demonstrate reproducibility)
5. **Reinforcing benchmark identity** (tone, framing, and conclusions reflect rigor over marketing)

**Estimated Effort**: 
- Points 1–3: ~4 hours (narrative/framing fixes, no experimentation)
- Point 4: ~6–8 hours (includes new ablation experiment or sensitivity analysis)
- Point 5: ~2 hours (tone/voice alignment across all sections)
- **Total**: ~12–14 hours, achievable in 1–2 working sessions

---

## Point 1: Tighten the Main Contribution Statement

### Current State
The introduction and abstract currently frame the contribution as:
- "We propose TRSS (Temporal Regularized Spline Smoothing) for EEG channel interpolation"
- Risk: Reviewers may expect TRSS to be a novel algorithm, then compare it to existing temporal-regularization methods

### Goal
Shift framing from "new method" to "rigorous methodology and fair benchmark":
- **Position**: We conduct a rigorous, fair-tuning benchmark study comparing 11 interpolation methods (geometric, graph-based, temporal-regularization families) on multi-dataset EEG scenarios.
- **Contribution**: We demonstrate that temporal-regularization methods (including TRSS, TV, temporal_laplacian) outperform baselines under fair hyperparameter tuning, and we provide reproducible code and latency measurements to support deployment decisions.

### Specific Actions

#### Action 1.1: Revise Abstract
- **File**: `paper/ieee/abstract.tex`, `thesis/usm/chapters/abstract_english.tex`
- **Change**: Replace "we propose TRSS" language with "we conduct a rigorous benchmark study comparing 11 methods" language.
- **Example Phrase**:
  - ❌ Old: "We propose a novel temporal-regularized approach (TRSS) for EEG channel interpolation."
  - ✅ New: "We conduct a rigorous benchmark study of 11 interpolation methods across multiple EEG datasets, demonstrating that temporal-regularization approaches, including TRSS, outperform baselines under fair hyperparameter tuning."

#### Action 1.2: Revise Introduction Contribution Paragraph
- **File**: `paper/ieee/sections/introduction.tex`
- **Target Section**: Final paragraph of introduction (usually labeled "Contributions" or "Paper Structure")
- **Change**: Explicitly enumerate contributions as:
  1. Fair hyperparameter tuning protocol using Optuna (TPE for graph/temporal, NSGA-II for geometric)
  2. Comprehensive trial-level pairwise comparison (736 iterations, Mann-Whitney U with Cliff's delta)
  3. Multi-dataset evaluation with deployment-relevant latency measurements
  4. Open-source reproducible implementation
- **Tone**: Benchmark rigor, not algorithm novelty

#### Action 1.3: Review Keywords
- **File**: `paper/ieee/main.tex` (keywords field)
- **Change**: Ensure keywords reflect "benchmark," "comparison," "EEG interpolation" rather than "novel," "proposed," etc.
- **Example**: Add "fair comparison," "hyperparameter tuning," "temporal regularization," "benchmark study"

---

## Point 2: Strengthen Limitations Section

### Current State
The limitations section exists in discussion but may be brief. Risk: Reviewers see acknowledged limitations and wonder if the benchmark scope is clear.

### Goal
Make explicit that this is a **validation study with defined scope**, not a universal superiority claim:

### Specific Actions

#### Action 2.1: Expand Limitations Section in Paper
- **File**: `paper/ieee/sections/discussion.tex`
- **Target Section**: "Limitations" subsection (if exists; otherwise create one before "Future Work")
- **Content to Add**:
  1. **Scope**: This study focuses on EEG channel interpolation with missing channels; results may not generalize to other sensor modalities without retuning.
  2. **Dataset Characteristics**: Evaluation uses datasets with 22–63 channels; scalability to higher-dimensional sensor arrays not tested.
  3. **Missing Ratio Range**: Hyperparameters tuned for 10%–50% missing channels; extrapolation beyond this range untested.
  4. **Computational Cost**: Latency measured on 50×64 fixture; real deployment on different hardware/data sizes requires re-profiling.
  5. **Statistical Sample**: Analysis aggregates 736 iterations per method; confidence intervals and effect sizes reported; results are reproducible but not universal.

#### Action 2.2: Add Parallel Limitations Section in Thesis
- **File**: `thesis/usm/chapters/05_discusion.tex`
- **Change**: Mirror the paper's limitations with additional detail suitable for thesis length.
- **Content**: Same five limitations as paper, plus discussion of how each limitation affects practical deployment and future validation.

#### Action 2.3: Cross-Reference Limitations in Conclusion
- **File**: `paper/ieee/sections/conclusion.tex`, `thesis/usm/chapters/06_conclusiones_y_trabajo_futuro.tex`
- **Change**: Add sentence explicitly tying future work to limitations: "Future work should address [limitation X] by [concrete next step]."
- **Example**: "Future work should extend evaluation to higher-dimensional sensor arrays (>100 channels) and assess scalability of temporal-regularization methods in those regimes."

---

## Point 3: Clean Up the Comparative Narrative

### Current State
The results and discussion sections present findings on multiple datasets and metrics. Risk: Reviewers may see inconsistent framing (e.g., "TRSS wins here but the difference is small there") and wonder if the narrative is cherry-picked.

### Goal
Maintain a **consistent, transparent framing** throughout:
- Fair conditions: Temporal-regularization methods win across datasets/metrics.
- Honest trade-offs: TRSS slower than pointwise methods, faster than TV.
- Caveats: Results depend on correct hyperparameter tuning; with bad tuning, any method can fail.

### Specific Actions

#### Action 3.1: Create a "Results Summary" Subsection
- **File**: `paper/ieee/sections/results.tex`
- **Insert Location**: At the end of the results section, before transitioning to discussion.
- **Content**:
  ```
  Summary:
  Across all datasets (PhysioNet, MNE, BCI IV 2a) and all metrics 
  (MAE, RMSE, DTW, SNR, LSD, Coherence), temporal-regularization 
  methods (TRSS, TV, temporal_laplacian) consistently rank in the 
  top 3 under fair hyperparameter tuning. TRSS achieves median 
  MAE improvements of X% over geometric baselines with Cliff's 
  delta effect sizes ranging from 0.3 to 0.7 (small to large). 
  Computational cost (9.44 ms per call) is acceptable for offline 
  and near-real-time pipelines but not for strict real-time 
  applications without acceleration. See Table [ref] for detailed 
  pairwise comparisons.
  ```

#### Action 3.2: Revise Discussion Narrative
- **File**: `paper/ieee/sections/discussion.tex`
- **Target Section**: Opening paragraphs of "Interpretation of Results" or similar.
- **Change**: Lead with the consistent finding (temporal-regularization wins), then address trade-offs and caveats.
- **Tone**: "We observe that temporal-regularization methods outperform baselines under fair tuning because [mechanism]. However, this advantage is contingent on [condition]; practitioners should be aware of [trade-off]."

#### Action 3.3: Clarify the Role of Optuna Tuning
- **File**: `paper/ieee/sections/methods.tex`
- **Target Section**: Hyperparameter tuning subsection.
- **Add**: Explicit statement that without careful tuning, any method (including baselines) can perform poorly. Include reference to sensitivity analysis or ablation (Point 4).
- **Example**: "Hyperparameter tuning is critical for fair comparison. To demonstrate this, we conduct a sensitivity analysis showing how TRSS performance varies with α and β (see Appendix [X] or Point 4 results)."

---

## Point 4: Add Practical Robustness Evidence ⭐ **PRIMARY FOCUS**

### Current State
The paper demonstrates that TRSS wins under optimal tuning but does not show:
- How sensitive TRSS is to changes in hyperparameters (α, β)?
- What happens if you remove the temporal term (TRSS vs. spatial-only spline)?
- How robust is TRSS across different initialization strategies or random seeds?

### Goal
Add **ablation and/or sensitivity analysis** to demonstrate that TRSS's advantage is robust, not artifact of tuning specifics or random variation.

### Rationale
Tier-1 reviewers want evidence that:
1. The method works for reasons you claim (temporal regularization helps)
2. Small changes to hyperparameters don't collapse performance (robustness)
3. The advantage isn't a one-off luck with random seeds (reproducibility)

### Recommended Approach: **Ablation Study** (Preferred over Sensitivity)

#### Why Ablation Over Sensitivity?
- **Sensitivity Analysis**: Vary α from 0.1 to 10, show MAE curve. Good but passive (observational).
- **Ablation Study**: Remove the temporal term → compare "TRSS-temporal" (spatial spline only) vs. "TRSS-full" (with temporal). Active (shows what contributes).
- **Verdict**: Ablation is stronger evidence because it directly answers "does temporal regularization actually help?"

#### Action 4.1: Design the Ablation Experiment

**Experimental Setup**:
- Run TRSS with three variants:
  1. **TRSS-Full**: Current implementation (both spatial graph Laplacian + temporal Laplacian)
  2. **TRSS-NoTemporal**: Remove temporal term (β = 0), keep spatial term (α = optimal value from Point 1)
  3. **Spatial-Only Spline**: Baseline spatial interpolant (no temporal smoothing at all)
- **Scope**: Execute on PhysioNet and BCI IV 2a (2 datasets, 2–3 subjects each, same missing ratios as main study)
- **Metrics**: MAE, RMSE, DTW (same as main study)
- **Analysis**: Pairwise Mann-Whitney U with Cliff's delta for ablated variants

**Expected Outcome**:
- TRSS-Full > TRSS-NoTemporal > Spatial-Only Spline in performance
- Cliff's delta for TRSS-Full vs. TRSS-NoTemporal should be ≥ 0.2 (small effect) to justify temporal term

#### Action 4.2: Implement Ablation in Code
- **File**: Create `scripts/ablation_temporal_component.py`
- **Logic**:
  - Load PhysioNet and BCI IV 2a data (same fixture as main study)
  - For each dataset:
    - Run TRSS-Full with α_opt, β_opt (from main study)
    - Run TRSS-NoTemporal with α_opt, β = 0
    - Run Spatial-Only Spline with α_opt
    - Perform pairwise Mann-Whitney U on 50 iterations per variant
  - Output: `results/ablation_temporal_component_results.csv`, `results/ablation_temporal_component_summary.txt`

#### Action 4.3: Visualize Ablation Results
- **File**: Create `scripts/plot_ablation_results.py`
- **Output Figures**:
  1. **Box plot**: Distribution of MAE for TRSS-Full vs. TRSS-NoTemporal vs. Spatial-Only across both datasets
  2. **Bar chart with error bars**: Median MAE ± 95% CI for each variant
  3. **Effect size plot**: Cliff's delta for pairwise comparisons with significance stars
- **Output**: `.agent_work/ablation_figures/`

#### Action 4.4: Write Ablation Results Section
- **File**: New subsection in `paper/ieee/sections/results.tex`: "Ablation Study: Temporal Component Contribution"
- **Content Structure**:
  ```
  We assess the contribution of the temporal regularization term 
  to TRSS performance by comparing three variants:
  
  1. TRSS-Full (α_opt, β_opt): Our proposed full model
  2. TRSS-NoTemporal (α_opt, β=0): Spatial-only variant
  3. Spatial-Only Spline: No graph regularization
  
  Results [Figure X]:
  - TRSS-Full achieves median MAE of [X] on PhysioNet and [Y] on BCI IV 2a
  - TRSS-NoTemporal achieves [X'] and [Y'], representing [%] degradation
  - Cliff's delta = [Z] (small to medium effect), indicating temporal 
    regularization provides meaningful improvement
  
  Conclusion: Temporal regularization is a key component of TRSS's 
  performance under fair conditions.
  ```

#### Action 4.5: Add to Thesis Discussion
- **File**: `thesis/usm/chapters/05_discusion.tex`
- **Add**: Expanded discussion of why temporal regularization works for EEG (signal continuity in time, channel dependencies in frequency)
- **Tie to Ablation**: "The ablation study (Section [X]) confirms that temporal regularization contributes meaningfully to reconstruction accuracy."

#### Alternative Approach: **Sensitivity Analysis** (If Ablation Too Costly)
If running ablation is infeasible within timeline:
- Perform sensitivity analysis on α and β separately
- Show plots of MAE vs. α (fixed β_opt) and MAE vs. β (fixed α_opt)
- Plot should show that TRSS performance is robust around optimal values (not brittle)
- Include bootstrapped 95% CIs to show variance

**Estimated Time for Ablation**: 
- Code implementation: 1–2 hours
- Execution (2 datasets, 50 iterations each): 30–60 minutes (parallel on GPU if available)
- Analysis and visualization: 1–2 hours
- **Total**: 3–4 hours

---

## Point 5: Maintain Benchmark-Paper Identity Throughout

### Current State
Introduction, methods, and results are reasonably positioned as benchmark. Risk: Discussion and conclusion may drift toward "TRSS is great" marketing language.

### Goal
Ensure all sections (especially discussion and conclusion) maintain the **rigorous benchmark tone** without overselling.

### Specific Actions

#### Action 5.1: Audit Conclusion Section for Marketing Language
- **File**: `paper/ieee/sections/conclusion.tex`
- **Search Terms**: "novel," "superior," "best," "outperforms all," "state-of-the-art"
- **Replacement Strategy**:
  - ❌ "TRSS is superior to all existing methods" → ✅ "Temporal-regularization methods, including TRSS, achieve better performance than geometric baselines under fair tuning"
  - ❌ "We propose the first temporal-regularized spline" → ✅ "We evaluate temporal-regularized approaches including TRSS in a rigorous comparative study"
  - ✅ Keep: "We provide reproducible code," "latency measurements," "practical recommendations," "future validation on larger datasets"

#### Action 5.2: Audit Discussion Section Tone
- **File**: `paper/ieee/sections/discussion.tex`
- **Review Paragraphs**: 
  - "Interpretation of Results" → should be factual, not celebratory
  - "Comparison with Related Work" → should position as complementary, not superior
  - "Implications" → should be cautious (e.g., "potential use in offline pipelines" not "suitable for all real-time applications")
- **Edit**: Replace promotional tone with objective, evidence-based language

#### Action 5.3: Check Introduction Tone
- **File**: `paper/ieee/sections/introduction.tex`
- **Review Paragraph**: Problem statement and motivation.
- **Ensure**: Framing is "EEG interpolation is important because [X]" and "existing methods have trade-offs [Y]", not "existing methods fail and we fix them"

#### Action 5.4: Thesis Spanish Language Review
- **File**: `thesis/usm/chapters/` (all sections)
- **Audit**: Spanish formality and tone (avoid overstating, maintain academic objectivity)
- **Particular Focus**: Resumen (Spanish abstract), Introducción, Discusión

#### Action 5.5: Final Tone Check with Consistency Pass
- **File**: Full paper and thesis (all sections)
- **Action**: Read through conclusion, discussion, and introduction in sequence.
- **Checklist**:
  - [ ] No claims that are not supported by results
  - [ ] All methods are presented as "compared" not "proposed/novel"
  - [ ] Limitations are explicitly stated
  - [ ] Future work is clear
  - [ ] Tone is "rigorous benchmark" throughout

---

## Implementation Schedule

### Phase 1: Planning & Review (This Document)
- [ ] User reviews this 5-point plan
- [ ] Confirm Point 4 approach (ablation vs. sensitivity)
- [ ] Clarify timeline constraints

### Phase 2: Points 1–3 (Narrative Fixes) — ~4 hours
- [ ] Action 1.1–1.3: Revise abstract and introduction
- [ ] Action 2.1–2.3: Expand limitations sections
- [ ] Action 3.1–3.3: Clean comparative narrative
- [ ] Test: Full paper/thesis compilation, no fatal errors

### Phase 3: Point 4 (Ablation Experiment) — ~4–6 hours
- [ ] Action 4.1: Design ablation experiment
- [ ] Action 4.2: Implement `scripts/ablation_temporal_component.py`
- [ ] Action 4.3: Run ablation, generate results CSV and figures
- [ ] Action 4.4: Write results subsection
- [ ] Action 4.5: Update thesis discussion
- [ ] Test: Verify figures match claims in text

### Phase 4: Point 5 (Tone Alignment) — ~2 hours
- [ ] Action 5.1–5.3: Audit and revise tone in conclusion, discussion, introduction
- [ ] Action 5.4–5.5: Spanish tone review and final consistency pass
- [ ] Test: Full paper/thesis compilation

### Phase 5: Final Validation & Handoff
- [ ] Full paper and thesis compile without fatal errors
- [ ] Bibtex: 0 warnings
- [ ] All figure references resolved
- [ ] All claims anchored to results or ablation data
- [ ] Commit to `publication-strengthening` branch with descriptive message

---

## Success Criteria

1. **Contribution Statement**: Abstract and introduction clearly frame study as "rigorous benchmark" not "novel algorithm"
2. **Limitations Explicit**: Paper and thesis both have dedicated limitations section covering scope, dataset characteristics, missing ratio range, computational constraints, statistical sample
3. **Narrative Consistent**: Results summary + discussion + conclusion all tell same story (temporal methods win fairly, with trade-offs)
4. **Ablation Evidence**: Ablation results show temporal component contributes meaningfully (Cliff's delta ≥ 0.2) to TRSS performance
5. **Tone Benchmark**: No marketing language; all claims evidence-based; limitations and future work clearly stated
6. **Compilation Clean**: Paper and thesis both build successfully; 0 fatal LaTeX errors; ≤ 3 non-critical warnings (overfull/underfull boxes)
7. **Reproducibility**: All new code (ablation) documented, parameterized, and runnable from repository root

---

## Risk Mitigation

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| Ablation experiment takes too long | Medium | Use sensitivity analysis instead (Point 4 alternative); or run on subset (1 dataset, 25 iterations) |
| Ablation results show temporal component is NOT significant | Low | If Cliff's delta < 0.2, discuss why (e.g., dataset-specific, needs higher resolution); position as "modest contribution" instead of "strong evidence" |
| Narrative changes conflict with results | Low | Re-read results section + new claims together; verify each claim is supported |
| Tone audit reveals extensive rewrites needed | Low | This is expected; budget 2–3 hours for comprehensive tone pass |
| LaTeX compilation breaks after edits | Low | Compile after each major section edit; keep backup of working .tex files |

---

## Next Steps (Awaiting User Approval)

1. **User Review**: Read this plan and confirm:
   - [ ] Point 4 approach (ablation preferred, sensitivity acceptable)
   - [ ] Timeline compatibility
   - [ ] Any adjustments to the action items

2. **Upon Approval**: We proceed with Phase 2 (narrative fixes) immediately, followed by Phase 3 (ablation if confirmed).

3. **Communication**: After each phase, we update this document with completed checkboxes and any findings/adjustments.

---

**Document Version**: 1.0 (Draft for Review)  
**Last Updated**: 2026-04-28  
**Status**: ⏳ Awaiting User Review and Approval
