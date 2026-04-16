# Integration Log: it150_049
Started: 2026-04-15T00:49:44.636053+00:00
Description: Bulk normalized run it150_049 dataset=mne_sample graph=kalofolias miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0027s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0036s
    tikhonov | MR=0.1 | seed=0 | MAE=4.1848e-01 | t=0.0072s
    tv | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.2980s
    trss | MR=0.1 | seed=0 | MAE=5.2622e-02 | t=0.0192s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=7.1705e-01 | t=0.0118s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.4709e-01 | t=8.3936s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0037s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0049s
    tikhonov | MR=0.1 | seed=1 | MAE=4.1794e-01 | t=0.0106s
    tv | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.3008s
    trss | MR=0.1 | seed=1 | MAE=5.2278e-02 | t=0.0189s

Completed: 2026-04-15T00:49:44.637163+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.