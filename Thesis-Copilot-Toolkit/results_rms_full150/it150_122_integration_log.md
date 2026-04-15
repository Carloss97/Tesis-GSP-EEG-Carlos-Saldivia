# Integration Log: it150_122
Started: 2026-04-15T00:44:26.813321+00:00
Description: Bulk normalized run it150_122 dataset=physionet_real graph=gaussian miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=42
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.0032s
    nearest | MR=0.2 | seed=0 | MAE=8.9975e-02 | t=0.0061s
    tikhonov | MR=0.2 | seed=0 | MAE=3.3910e-01 | t=0.0096s
    tv | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.2974s
    trss | MR=0.2 | seed=0 | MAE=5.7907e-02 | t=0.0242s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2159e-01 | t=0.0250s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4792e-01 | t=7.1228s
    mean | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.0029s
    nearest | MR=0.2 | seed=1 | MAE=8.7931e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=1 | MAE=3.3978e-01 | t=0.0078s
    tv | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.2674s
    trss | MR=0.2 | seed=1 | MAE=5.7276e-02 | t=0.0219s

Completed: 2026-04-15T00:44:26.814261+00:00
Total rows: 42
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.