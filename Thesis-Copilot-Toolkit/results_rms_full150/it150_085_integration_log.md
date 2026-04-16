# Integration Log: it150_085
Started: 2026-04-15T00:52:54.508491+00:00
Description: Bulk normalized run it150_085 dataset=mne_sample graph=aew miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: aew built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0043s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0053s
    tikhonov | MR=0.1 | seed=0 | MAE=2.3576e-01 | t=0.0211s
    tv | MR=0.1 | seed=0 | MAE=7.9632e-02 | t=0.2185s
    trss | MR=0.1 | seed=0 | MAE=6.2225e-02 | t=0.0197s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.8235e-01 | t=0.0123s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=5.9248e-01 | t=2.2876s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0022s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0033s
    tikhonov | MR=0.1 | seed=1 | MAE=2.3715e-01 | t=0.0073s
    tv | MR=0.1 | seed=1 | MAE=7.9124e-02 | t=0.2021s
    trss | MR=0.1 | seed=1 | MAE=6.3167e-02 | t=0.0190s

Completed: 2026-04-15T00:52:54.509420+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.