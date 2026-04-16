# Integration Log: it150_037
Started: 2026-04-15T00:48:31.974961+00:00
Description: Bulk normalized run it150_037 dataset=mne_sample graph=gaussian miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0109s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0102s
    tikhonov | MR=0.1 | seed=0 | MAE=6.5292e-01 | t=0.0153s
    tv | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.5643s
    trss | MR=0.1 | seed=0 | MAE=5.2616e-02 | t=0.0181s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=8.3278e-01 | t=0.0123s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.3934e-01 | t=4.6915s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0052s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0137s
    tikhonov | MR=0.1 | seed=1 | MAE=6.5248e-01 | t=0.0157s
    tv | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.3902s
    trss | MR=0.1 | seed=1 | MAE=5.2264e-02 | t=0.0196s

Completed: 2026-04-15T00:48:31.976882+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.