# Integration Log: it150_035
Started: 2026-04-15T00:48:04.535666+00:00
Description: Bulk normalized run it150_035 dataset=synthetic_broad graph=gaussian miss=[0.1] mode=base

## Dataset: synthetic_broad | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=5.4881e-02 | t=0.0067s
    nearest | MR=0.1 | seed=0 | MAE=7.5105e-02 | t=0.0067s
    tikhonov | MR=0.1 | seed=0 | MAE=3.5046e-01 | t=0.0152s
    tv | MR=0.1 | seed=0 | MAE=5.4299e-02 | t=0.2867s
    trss | MR=0.1 | seed=0 | MAE=3.8383e-02 | t=0.0185s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.3299e-01 | t=0.0111s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.7244e-01 | t=4.6844s
    mean | MR=0.1 | seed=1 | MAE=5.4906e-02 | t=0.0088s
    nearest | MR=0.1 | seed=1 | MAE=7.4297e-02 | t=0.0065s
    tikhonov | MR=0.1 | seed=1 | MAE=3.5099e-01 | t=0.0167s
    tv | MR=0.1 | seed=1 | MAE=5.4315e-02 | t=0.2970s
    trss | MR=0.1 | seed=1 | MAE=3.8347e-02 | t=0.0190s

Completed: 2026-04-15T00:48:04.543552+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.