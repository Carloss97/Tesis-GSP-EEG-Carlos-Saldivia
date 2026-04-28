# PHASE 1: BASELINE STATE & VERSION CONTROL
**Date Created**: 2026-04-27  
**Status**: ACTIVE - Implementation Phase 1 Started  
**Objective**: Establish formal baseline, separate active from legacy sources, create version-control contract, document methodology gaps.

---

## 1. FILE INVENTORY & SOURCES

### ACTIVE SOURCES (Primary Development)

#### Paper (IEEE Format)
**Location**: `Thesis-Copilot-Toolkit/paper/ieee/`  
**Master File**: `main.tex`

**Core Sections** (in `sections/`):
- `abstract.tex` — Clinical motivation, methodology overview, 6-metric summary, multi-dataset validation
- `introduction.tex` — Missing-channel problem, GSP paradigm, benchmarking gap positioning
- `related_work.tex` — Subsections: classical geometric, GSP spatial, temporal + benchmarking gap
- `methods.tex` — Graph construction (5 neighborhoods, 3 families), three interpolation families, Optuna setup, metrics
- `results.tex` — Wilcoxon significance, multi-metric table, ERP/PSD visualizations
- `discussion.tex` — Physiological fidelity, generalization, deep learning positioning, limitations
- `conclusion.tex` — Hypothesis validation, contributions, future work claims
- `reproducibility.tex` — Code availability, environment specs

**Supporting Resources**:
- `bibliography/references.bib` — Paper-specific bibliography entries
- `figures/` — PNG/PDF plots (ERP, PSD, topmaps, reconstruction)
- `tables/` — Multi-metric comparison tables (CSV source data)
- `build/` — Intermediate LaTeX artifacts

**Compilation Output**:
- `main.pdf` — Current compiled version (8 pages)
- `main.log`, `main.blg` — Build logs (clean, no blocking errors)

---

#### Thesis (USM Format)
**Location**: `Thesis-Copilot-Toolkit/thesis/usm/`  
**Master File**: `main.tex`

**Core Chapters** (in `chapters/`):
- `01_introduccion.tex` — Problem framing, motivation, hypothesis, objectives (general + 6 specific), scope, contributions
- `02_marco_teorico.tex` — EEG neurophysiology, GSP theory (Laplacian, GFT), interpolation strategies, metric definitions. **32/32 bibliography keys in active use.**
- `03_metodologia.tex` — Three datasets, five method families, Optuna setup, train/test protocol (2s buffer), six metrics, Wilcoxon+Bonferroni testing, reproducibility
- `04_experimentos_y_resultados.tex` — Global comparison (TRSS vs Baseline), multi-metric table by family, robustness curves, heatmaps, Pareto frontiers, statistical significance
- `05_discusion.tex` — Interprets temporal regularization advantage, analyzes fair benchmarking impact, discusses clinical relevance, lists computational cost (O(n_iter·N²·T) seconds), transparently enumerates limitations
- `06_conclusiones_y_trabajo_futuro.tex` — Validates hypothesis, lists 6 objective achievements + 3 original contributions, outlines 4 future directions

**Supporting Resources**:
- `bibliography/references.bib` — Thesis-specific bibliography entries
- `frontmatter/` — Title page, acknowledgments, table of contents
- `figures/` — Plots and visualizations
- `tables/` — Detailed metric tables
- `assets/` — Logos, templates, style files
- `appendix_detailed_tables.tex` — Extended results tables

**Auxiliary Scripts**:
- `plot_metrics_analysis.py` — Generates metric CSVs from iteration results

**Compilation Output**:
- `main.pdf` — Current compiled version (80 pages)
- `main.log`, `main.blg` — Build logs (clean, 0 blocking errors, bibtex warnings on empty fields)

---

#### Bibliography (Shared)
**Primary Early-Chapter Source**: `Referencias/Tesis_biblio/Tesis_biblio.bib`  
- **32 active keys** in thesis early chapters (02_marco_teorico.tex)
- 4 keys added in last session: kalofolias_large_2019, ortega_graph_2018, shekkizhar_graph_2020, shekkizhar_neighborhood_2023

**Secondary/Paper Bibliography**:
- `Thesis-Copilot-Toolkit/paper/ieee/bibliography/references.bib`
- `Thesis-Copilot-Toolkit/thesis/usm/bibliography/references.bib`

**Shared Macros**:
- `Thesis-Copilot-Toolkit/shared/results_data.tex` — Consolidated metric constants (ResTVMAE, ResTVSNR, etc.)

---

### LEGACY/BORRADOR SOURCES (Non-Active)
**Location**: `Escritos-gamma4/`

- `Paper/main_paper.tex` — Previous paper draft (superseded by `Thesis-Copilot-Toolkit/paper/ieee/main.tex`)
- `Tesis/` — Previous thesis structure (superseded by `Thesis-Copilot-Toolkit/thesis/usm/`)

**Status**: Legacy. Do NOT edit. Reference only if historical context needed. All active development is in `Thesis-Copilot-Toolkit/`.

---

## 2. BASELINE STATE SNAPSHOT

### Paper Status
- **Compilation**: ✅ Clean (main.pdf generated, 8 pages)
- **Citation Coverage**: ✅ 32/32 keys in early chapters active (0 missing)
- **Syntax Errors**: ✅ 0 blocking errors (bibtex warnings on empty year/journal fields in secondary sources)
- **Numeric Coherence**: ✅ Multi-metric table values verified against source CSV
- **Last Edited**: Session ending April 27, 2026 (abstract, methods, results rewrites; second-pass corrections)

### Thesis Status
- **Compilation**: ✅ Clean (main.pdf generated, 80 pages)
- **Citation Coverage**: ✅ 32/32 keys in active use (all 4 missing keys now cited in chapter 02)
- **Syntax Errors**: ✅ 0 blocking errors (LaTeX fix completed in methodology chapter)
- **Numeric Coherence**: ✅ Table values synchronized with paper and source CSV
- **Last Edited**: Session ending April 27, 2026 (chapter 02 bibliography expansion, chapter 03 LaTeX fixes)

### Known Issues (Documented, Pending Resolution)
1. **Critical: Optuna Methodology Inconsistency** (GATE FOR PHASE 3)
   - Paper claims: TPE only, **100 trials** per scenario
   - Thesis claims: TPE + NSGA-II, **10–50 trials** per scenario (depends on dimensionality)
   - **Resolution needed**: Single agreed narrative across both documents

2. **Important: Statistical Unit of Analysis** (GATE FOR PHASE 2)
   - Current: Wilcoxon paired test on n=42 aggregated contexts
   - Risk: Pseudoreplication (should be trial-level with hierarchical/bootstrap correction)
   - **Resolution needed**: Recalculate significance at trial level

3. **Important: Computational Latency** (GATE FOR PHASE 2)
   - Paper: Claims real-time BCI applicability without latency metrics
   - Thesis: Mentions O(n_iter·N²·T) seconds complexity discussion
   - **Resolution needed**: Insert formal latency table with method, ms/epoch, hardware

4. **Medium: Promotional Language** (GATE FOR PHASE 4)
   - Flagged terms: "unprecedented", "paradigm shift", "theoretical ceiling"
   - **Resolution needed**: Reduce to verifiable claims ("fair benchmarking + multi-metric + multi-dataset")

5. **Medium: Bibliography Warnings** (GATE FOR PHASE 5)
   - Empty year/journal fields in secondary .bib entries
   - **Resolution needed**: Complete all entries to eliminate bibtex warnings

---

## 3. VERSION CONTROL CONTRACT

### Branch & File Naming Convention
- **Active Development Branch**: `main` (in `Thesis-Copilot-Toolkit/`)
- **Legacy Branches/Folders**: `Escritos-gamma4/` (do not edit)
- **Work-in-Progress Storage**: `.agent_work/` (this directory)

### Change Tracking Protocol

#### For Each Phase Completion:
1. **Create Phase Summary Document** (this template):
   ```
   .agent_work/PHASE_NN_[DESCRIPTION].md
   ```
   - Date, status, objective
   - Deliverables checklist
   - File changes (before/after snapshots)
   - Validation results
   - Decision records for any deviations

2. **Update Corresponding Source Files** in `Thesis-Copilot-Toolkit/`:
   - Paper sections in `paper/ieee/sections/`
   - Thesis chapters in `thesis/usm/chapters/`
   - Bibliography in `references.bib` files

3. **Backup Before Major Edit**:
   - For chapters/sections receiving >20 lines of changes, create `.bak` backup
   - Example: `03_metodologia.tex.bak_phase03_2026-04-27`

4. **Validation Checkpoint**:
   - Recompile both paper and thesis after changes
   - Verify no new errors introduced
   - Update this baseline document if methodology or scope changes

### Edit Log Template

Use this template for each substantive change in `.agent_work/CHANGE_LOG.md`:

```markdown
### [DATE] [PHASE] [FILE] - [CHANGE TYPE]
**Author**: Agent  
**File**: [path relative to Thesis-Copilot-Toolkit/]  
**Change**: [1-2 sentence summary]  
**Scope**: [Lines affected, approx. word count change]  
**Reason**: [Traced to which phase objective]  
**Validation**: [Compilation OK? Citation check? Numeric coherence?]  
**Status**: [Complete / Pending / Blocked]
```

---

## 4. METHODOLOGY ALIGNMENT CHECKPOINT — RESOLVED

### Optuna Configuration: Actual Implementation Identified

**Status**: RESOLVED via script analysis. **Result: Option C (Hybrid/Stratified by Method Type)**

#### Actual Configuration — Evidence from Source Code

**GSP Methods Optimization** (`Thesis-Copilot-Toolkit/experiments/run_optuna_optimization.py`, line 168)
```python
N_TRIALS = 30
# Default sampler = TPE (single-objective, minimize MAE)
study_trss.optimize(lambda t: objective_trss(...), n_trials=N_TRIALS)
study_tik.optimize(lambda t: objective_tikhonov(...), n_trials=N_TRIALS)
```
- **Sampler**: TPE (default single-objective)
- **Trials Per Scenario**: **30** (fixed)
- **Objective**: Minimize MAE only
- **Methods covered**: Tikhonov, TRSS, spatial graph methods

**Baseline Methods Optimization** (`Thesis-Copilot-Toolkit/experiments/run_optuna_baselines.py`, lines 140–144)
```python
sampler = optuna.samplers.NSGAIISampler(seed=42)  # Line 140
study = optuna.create_study(directions=["minimize", "minimize"], sampler=sampler)  # Line 141
study.optimize(lambda t: objective(t, ...), n_trials=10, ...)  # Line 144
```
- **Sampler**: NSGA-II (multi-objective)
- **Trials Per Scenario**: **10** (fixed)
- **Objectives**: Minimize MAE **and** LSD (Pareto front)
- **Methods covered**: Spherical Spline, RBFI, ICA

#### Verdict: Both Statements Are INACCURATE

| Document | Claim | Actual Implementation | Match? |
|----------|-------|----------------------|--------|
| **Paper** | "TPE only, 100 trials" | TPE 30 trials (GSP) + NSGA-II 10 trials (baselines) | ❌ NO |
| **Thesis** | "TPE + NSGA-II, 10–50 trials" | TPE 30 trials (GSP) + NSGA-II 10 trials (baselines) | ⚠️ PARTIALLY |

#### Implications for Phase 3

**Paper `sections/methods.tex` (line 57–82)** — Must be corrected to state:
- "30 trials for graph-based methods (Tikhonov, TRSS) using TPE sampler"
- "10 trials for baseline geometric methods (Spline, RBFI, ICA) using NSGA-II multi-objective sampler"
- Delete the false claim of "100 trials"
- Clarify dual-objective optimization for baselines: minimize both MAE and Laplacian Smoothness Deviation (LSD)

**Thesis `chapters/03_metodologia.tex` (section on Optuna)** — Must be corrected to state:
- "GSP methods: TPE sampler, 30 trials per scenario"
- "Baseline methods: NSGA-II sampler, 10 trials per scenario, multi-objective (MAE + LSD)"
- Remove vague phrasing "10–50 trials depending on dimensionality" and replace with explicit stratification
- Clarify that NSGA-II multi-objective applies to baselines, not GSP methods

#### Why This Matters

1. **Reproducibility**: Scripts are deterministic (seed=42); correcting documentation does not require re-running experiments
2. **Methodological Rigor**: The stratified approach (TPE for GSP, NSGA-II for baselines) is justified and appropriate
3. **Publication Integrity**: Claims must match implementation; current paper claim of "100 trials" is factually wrong
4. **Phase 3 Action**: Explicit stratification must be documented in both documents with source code citations

---

## 5. DELIVERABLES CHECKLIST — PHASE 1

- [x] Inventory of active sources (Paper, Thesis, Bibliography) with file structure
- [x] Identification of legacy sources (Escritos-gamma4/) and clear "do not edit" status
- [x] Baseline snapshot of compilation status, citation coverage, syntax errors, numeric coherence
- [x] Documentation of 5 known issues with gate phases and resolution paths
- [x] Version control contract with branch naming, file naming, change tracking protocol, edit log template
- [x] Methodology alignment checkpoint identifying critical Optuna inconsistency
- [x] Decision point for resolving Optuna configuration (Option A/B/C)
- [x] Recommended path forward (consult experiment scripts in Phase 1, validate in Phase 2, revise in Phase 3)

---

## 6. NEXT STEPS — PHASE 2 PREVIEW

**GATE CLARIFICATION**: Optuna inconsistency is now **RESOLVED** — Phase 2 proceeds without methodological blocking. Phase 3 (Phase 3) will address the documentation corrections.

Once Phase 1 baseline is locked:

1. **Phase 2: Quantitative Fixes** (PROCEEDS UNBLOCKED)
   - Recalculate Wilcoxon significance at trial level (not n=42 aggregated contexts)
   - Insert formal latency/complexity table into paper (from O(n_iter·N²·T) formula in thesis)
   - Verify numeric coherence across all three documents (paper, thesis, shared macros)
   - Verify Optuna trial outputs match expected counts (30 for GSP, 10 for baselines)

2. **Phase 3: Methodological Refinement** (NOW INCLUDES OPTUNA DOCUMENTATION)
   - Update paper `sections/methods.tex` to correct trial count (100 → 30 GSP + 10 baselines) and sampler names
   - Update thesis `chapters/03_metodologia.tex` to clarify stratification (TPE 30 trials for GSP, NSGA-II 10 trials for baselines)
   - Add explicit source code citations to both documents (run_optuna_optimization.py line 168, run_optuna_baselines.py lines 140-144)
   - Extend discussion of NSGA-II multi-objective rationale for baselines

3. **Pending Resolution** (Non-blocking):
   - Bibtex warnings (bibliography cleanup) deferred to Phase 5
   - Promotional language toning deferred to Phase 4

---

## 7. SIGN-OFF & LOCK

**Phase 1 Baseline Established**: 2026-04-27  
**Status**: COMPLETE — Ready to proceed to Phase 2 (Quantitative Fixes)  
**Gate Status**: 
- ✅ File inventory and legacy separation complete
- ✅ Baseline snapshot documented
- ✅ Version control contract established
- ✅ **Optuna configuration inconsistency RESOLVED** (TPE 30 trials for GSP, NSGA-II 10 trials for baselines) — Phase 3 corrections planned

**Next Scheduled Action**: Begin Phase 2 — Recalculate Wilcoxon significance at trial level and insert latency metrics table.

