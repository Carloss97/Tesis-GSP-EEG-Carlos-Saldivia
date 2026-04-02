# Reproducibility Package (RPL-01)

## Environment
- python: 3.14.3
- platform: Windows-11-10.0.26200-SP0
- cpu_count: 12
- numpy: 2.4.4
- pandas: 3.0.2
- scipy: 1.17.1

## Commands
```powershell
$env:PYTHONPATH='.../Thesis-Copilot-Toolkit'
$env:INCLUDE_MNE='1'
$env:MAX_TIME_SAMPLES='220'
$env:B2_DTW_MAX_POINTS='80'
$env:B2_TOP_K='3'
$env:B2_RANDOM_SEED='42'
python experiments/run_b2_batched.py
python experiments/consolidate_b2_publication.py
python experiments/finalize_b3_b4.py
```

## Core artifacts
- results/opt_benchmark_b2_full_scale_raw.csv
- results/opt_benchmark_b2_full_scale_summary.csv
- results/b2_publication_ranking_final.csv
- results/b3_stat02_significance.csv
- results/b3_rep01_final_table_overall.csv
