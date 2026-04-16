# Integration Log: it150_025
Started: 2026-04-15T00:47:25.944717+00:00
Description: Bulk normalized run it150_025 dataset=mne_sample graph=gaussian miss=[0.1] mode=base

## Dataset: mne_sample | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.0033s
    nearest | MR=0.1 | seed=0 | MAE=1.0002e-01 | t=0.0063s
    tikhonov | MR=0.1 | seed=0 | MAE=6.5534e-01 | t=0.0124s
    tv | MR=0.1 | seed=0 | MAE=7.9366e-02 | t=0.5405s
    trss | MR=0.1 | seed=0 | MAE=5.2620e-02 | t=0.0799s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=8.3361e-01 | t=0.0291s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.4003e-01 | t=2.2347s
    mean | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.0031s
    nearest | MR=0.1 | seed=1 | MAE=1.0381e-01 | t=0.0027s
    tikhonov | MR=0.1 | seed=1 | MAE=6.5489e-01 | t=0.0134s
    tv | MR=0.1 | seed=1 | MAE=7.8687e-02 | t=0.6055s
    trss | MR=0.1 | seed=1 | MAE=5.2273e-02 | t=0.1525s

Completed: 2026-04-15T00:47:25.945566+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.