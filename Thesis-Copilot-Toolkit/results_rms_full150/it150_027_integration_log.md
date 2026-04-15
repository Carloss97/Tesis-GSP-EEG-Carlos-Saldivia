# Integration Log: it150_027
Started: 2026-04-15T00:26:36.925474+00:00
Description: Bulk normalized run it150_027 dataset=bci_iv2a_real_s1 graph=gaussian miss=[0.1] mode=base

## Dataset: bci_iv2a_real_s1 | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.0021s
    nearest | MR=0.1 | seed=0 | MAE=3.1361e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=2.8344e-01 | t=0.0076s
    tv | MR=0.1 | seed=0 | MAE=3.5667e-02 | t=0.2589s
    trss | MR=0.1 | seed=0 | MAE=2.4354e-02 | t=0.0196s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=3.6447e-01 | t=0.0109s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.0592e-01 | t=2.0625s
    mean | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.0023s
    nearest | MR=0.1 | seed=1 | MAE=3.1289e-02 | t=0.0042s
    tikhonov | MR=0.1 | seed=1 | MAE=2.8427e-01 | t=0.0071s
    tv | MR=0.1 | seed=1 | MAE=3.3709e-02 | t=0.2638s
    trss | MR=0.1 | seed=1 | MAE=2.2962e-02 | t=0.0191s

Completed: 2026-04-15T00:26:36.926950+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.