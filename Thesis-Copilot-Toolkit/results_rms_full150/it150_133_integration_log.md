# Integration Log: it150_133
Started: 2026-04-15T00:56:31.911761+00:00
Description: Bulk normalized run it150_133 dataset=mne_sample graph=gaussian miss=[0.2] mode=base

## Dataset: mne_sample | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.0021s
    nearest | MR=0.2 | seed=0 | MAE=2.0800e-01 | t=0.0051s
    tikhonov | MR=0.2 | seed=0 | MAE=6.7648e-01 | t=0.0066s
    tv | MR=0.2 | seed=0 | MAE=1.5569e-01 | t=0.2396s
    trss | MR=0.2 | seed=0 | MAE=1.0631e-01 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=8.3925e-01 | t=0.0102s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.4474e-01 | t=1.9129s
    mean | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.0023s
    nearest | MR=0.2 | seed=1 | MAE=2.1365e-01 | t=0.0059s
    tikhonov | MR=0.2 | seed=1 | MAE=6.7674e-01 | t=0.0068s
    tv | MR=0.2 | seed=1 | MAE=1.5761e-01 | t=0.2269s
    trss | MR=0.2 | seed=1 | MAE=1.0851e-01 | t=0.0199s

Completed: 2026-04-15T00:56:31.912515+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.