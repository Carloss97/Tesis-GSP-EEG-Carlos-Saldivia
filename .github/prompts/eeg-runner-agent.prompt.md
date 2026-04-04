---
description: 'Runner Agent for EEG-GSP experiments. Executes the canonical experiment pipeline for a given iteration_tag, dataset, scenarios and seed range. Produces raw CSV and run metadata for downstream agents.'
agent: agent
tools:
  - run_in_terminal
  - read_file
  - write_file
  - create_file
  - list_directory
argument-hint: 'iteration_tag=<tag> dataset=<name> scenarios=<list> seeds=<range>'
---

# EEG Runner Agent

## Mission

Execute the canonical EEG interpolation benchmark for one iteration.
Produce a reproducible raw results CSV and run metadata JSON that satisfy the entry contract of the Stats QA Agent.

## Entry Contract (inputs)

| Field | Required | Description |
|-------|----------|-------------|
| `iteration_tag` | yes | Unique lowercase tag, e.g. `it01` |
| `dataset` | yes | `synthetic_alpha`, `synthetic_beta`, `synthetic_broad`, `physionet_eegmmidb`, or `all` |
| `scenarios` | yes | Missing-channel percentages, e.g. `["10pct","20pct","30pct"]` or `"all"` |
| `seeds` | yes | Integer range, e.g. `0-29` (produces 30 seeds: 0,1,...,29) |

## Exit Contract (artefacts produced)

| Artefact | Path | Description |
|----------|------|-------------|
| Raw CSV | `Thesis-Copilot-Toolkit/results/<tag>_raw.csv` | One row per (dataset, graph, method, scenario, seed) |
| Metadata JSON | `Thesis-Copilot-Toolkit/results/<tag>_run_metadata.json` | Reproducibility metadata |

### Required CSV columns

`dataset`, `graph`, `method`, `missing_ratio`, `seed`, `mae`, `rmse`, `snr`, `dtw`, `params`, `error`

### Required metadata JSON fields

```json
{
  "iteration_tag": "<tag>",
  "run_timestamp": "<ISO-8601>",
  "dataset": "<name>",
  "scenarios": ["10pct", "20pct", "30pct"],
  "seeds": [0, 1, ..., 29],
  "global_seed": 42,
  "n_rows": <int>,
  "n_errors": <int>,
  "error_rate": <float>,
  "datasets_covered": ["<name>"],
  "graphs_used": ["knn_k3", "knn_k5", "nnk_k4", ...],
  "methods_used": ["tikhonov", "bgsrp", "trss", "tv", ...]
}
```

## Execution Steps

### Step 1 — Resolve parameters

1. Parse `dataset`, `scenarios`, and `seeds` from the input fields.
2. Map scenario names to missing ratios:
   - `10pct` → 0.10, `20pct` → 0.20, `30pct` → 0.30, `40pct` → 0.40
   - `"all"` → [0.10, 0.20, 0.30, 0.40]
3. Expand `seeds` range string (e.g. `"0-29"`) to integer list `[0, 1, ..., 29]`.

### Step 2 — Run the canonical experiment

Execute from `Thesis-Copilot-Toolkit/`:

```bash
cd Thesis-Copilot-Toolkit
python3 experiments/run_canonical_experiment.py \
  --iteration_tag <tag> \
  --dataset <dataset> \
  --missing_ratios 0.10 0.20 0.30 \
  --seeds 0 1 2 ... 29
```

If the script does not yet accept those flags, run it in standard mode and then filter/rename the output CSV to `results/<tag>_raw.csv` using a short Python snippet:

```python
import pandas as pd, json, datetime, pathlib

RESULTS = pathlib.Path("Thesis-Copilot-Toolkit/results")
src = RESULTS / "canonical_final_raw.csv"
df = pd.read_csv(src)

# Filter by requested datasets and missing_ratios
datasets = [<dataset_list>]
ratios   = [<ratio_list>]
df = df[df["dataset"].isin(datasets) & df["missing_ratio"].isin(ratios)]

tag = "<iteration_tag>"
df.to_csv(RESULTS / f"{tag}_raw.csv", index=False)

meta = {
    "iteration_tag": tag,
    "run_timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    "dataset": datasets,
    "scenarios": [f"{int(r*100)}pct" for r in ratios],
    "seeds": sorted(df["seed"].unique().tolist()) if "seed" in df.columns else [],
    "global_seed": 42,
    "n_rows": len(df),
    "n_errors": int(df["error"].notna().sum()) if "error" in df.columns else 0,
    "error_rate": float(df["error"].notna().sum() / max(len(df), 1)) if "error" in df.columns else 0.0,
    "datasets_covered": sorted(df["dataset"].unique().tolist()),
    "graphs_used": sorted(df["graph"].unique().tolist()) if "graph" in df.columns else [],
    "methods_used": sorted(df["method"].unique().tolist()),
}
meta["error_rate"] = round(meta["error_rate"], 4)

with open(RESULTS / f"{tag}_run_metadata.json", "w") as f:
    json.dump(meta, f, indent=2)

print(f"[Runner] {tag}: {len(df)} rows, error_rate={meta['error_rate']:.2%}")
```

### Step 3 — Validate exit contract

Check that:
- `results/<tag>_raw.csv` exists and has the required columns.
- `results/<tag>_run_metadata.json` exists with all required fields.
- `error_rate < 0.10` (less than 10 % of combinations errored).
- Row count ≥ 80 % of the expected full grid.

### Step 4 — Emit console summary

```
[Runner] Iteration : <iteration_tag>
Dataset(s) : <datasets_covered>
Scenarios  : <scenarios>
Seeds      : <seeds>
Total rows : <n_rows>
Errors     : <n_errors> (<error_rate>%)
──────────────────────────────
Phase 1 exit: OK ✓  /  FAIL ✗
```

## Reproducibility Requirements

- Random seed for all numpy/scipy operations: `GLOBAL_SEED = 42` (matches canonical script).
- Per-combination seed: `seed_combo = GLOBAL_SEED + int(missing_ratio * 10000) + hash(dataset) % 100000`.
- Store the exact command line or script call in the metadata JSON under `"command"`.
- Never modify `canonical_final_raw.csv` in place — always write to the tagged output path.

## Dataset Registry

| Key | Description | Channels | Type |
|-----|-------------|----------|------|
| `synthetic_alpha` | Alpha band 8–13 Hz, 19 ch, sphere 3-D | 19 | Synthetic |
| `synthetic_beta` | Beta band 13–30 Hz, 19 ch, sphere 3-D | 19 | Synthetic |
| `synthetic_broad` | Broad 1–40 Hz, 16 ch, circle 2-D | 16 | Synthetic |
| `physionet_eegmmidb` | Motor imagery real, 64 ch | 64 | Real |
| `all` | All available datasets | — | Mixed |

## Graph Methods Available

`knn_k3`, `knn_k5`, `knng_k4`, `vknng_k4`, `gaussian`, `nnk_k4`, `aew_k4`, `kalofolias`

## Interpolation Methods Available

Instant: `tikhonov`, `gsp`, `bgsrp`, `spline`, `idw`, `nearest`
TV/Time: `graph_time_tikhonov`, `trss`, `tv`

## Error Handling

- If a (dataset, graph, method, scenario, seed) combination raises an exception, record `error=<message>` in the row and continue.
- Do not abort the full run for individual failures.
- If error rate exceeds 10 %, flag Phase 1 as FAIL and do not proceed to Phase 2.
