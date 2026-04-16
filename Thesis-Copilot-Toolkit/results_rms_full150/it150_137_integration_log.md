# Integration Log: it150_137
Started: 2026-04-15T00:57:04.461949+00:00
Description: Bulk normalized run it150_137 dataset=bci_iv2a_real_s3 graph=gaussian miss=[0.2] mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.0033s
    nearest | MR=0.2 | seed=0 | MAE=6.1045e-02 | t=0.0050s
    tikhonov | MR=0.2 | seed=0 | MAE=2.9914e-01 | t=0.0067s
    tv | MR=0.2 | seed=0 | MAE=6.5815e-02 | t=0.2350s
    trss | MR=0.2 | seed=0 | MAE=4.8316e-02 | t=0.0200s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=3.7966e-01 | t=0.0089s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.3605e-01 | t=1.7369s
    mean | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=5.9347e-02 | t=0.0048s
    tikhonov | MR=0.2 | seed=1 | MAE=3.0000e-01 | t=0.0067s
    tv | MR=0.2 | seed=1 | MAE=6.8917e-02 | t=0.2460s
    trss | MR=0.2 | seed=1 | MAE=5.1312e-02 | t=0.0209s

Completed: 2026-04-15T00:57:04.462683+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.