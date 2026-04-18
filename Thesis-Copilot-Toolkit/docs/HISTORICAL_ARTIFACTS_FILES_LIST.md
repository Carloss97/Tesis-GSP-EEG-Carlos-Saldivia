# Historical artifacts referencing excluded methods/datasets

Found occurrences for the excluded tokens: `heat_diffusion_temporal`, `wavelet_temporal`, `directed_tv`, `iv100hz_mat`.

Summary (sample of matches):

- informes/weekly_summary_2026-04-01_2026-04-07/results_inventory_with_status.json — multiple references to `directed_tv` (figures, tables, run_metadata).
- Thesis-Copilot-Toolkit/ITERATIONS_COMPREHENSIVE_REPORT.md — occurrences of `heat_diffusion_temporal` in TV/Time table.
- Thesis-Copilot-Toolkit/AGENT_ITERATION_GUIDE.md — historical result rows mentioning `heat_diffusion_temporal`.
- Thesis-Copilot-Toolkit/thesis/usm/chapters/04_experimentos_y_resultados.tex (+ several .bak files) — textual mentions of `heat_diffusion_temporal` in reported results.
- Thesis-Copilot-Toolkit/experiments/selections_archive_2026-04-14/* — many CSV/JSON/MD files listing `heat_diffusion_temporal` in selections and filtered tables.
- Thesis-Copilot-Toolkit/results/it18_directed_tv_vs_trss_* — result folders referenced from reports.
- informes/weekly_summary_2026-04-01_2026-04-07/figures/unified_final_ranking.csv — contains `heat_diffusion_temporal` rows.

What I did:
- Collected matches across the repo (search for the four tokens).
- Created this file listing the main affected paths and examples.

Next steps (done automatically if you want):
- Insert a one-line header in each found historical file pointing to `Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_NOTICE.md` (I can apply these small annotations in-place if you confirm).

File created: Thesis-Copilot-Toolkit/docs/HISTORICAL_ARTIFACTS_FILES_LIST.md
