# Integration Log: it150_033
Started: 2026-04-15T00:47:35.909954+00:00
Description: Bulk normalized run it150_033 dataset=synthetic_alpha graph=gaussian miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0032s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0034s
    tikhonov | MR=0.1 | seed=0 | MAE=2.9126e-01 | t=0.0075s
    tv | MR=0.1 | seed=0 | MAE=4.2968e-02 | t=0.2375s
    trss | MR=0.1 | seed=0 | MAE=3.1082e-02 | t=0.0173s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=5.0594e-01 | t=0.0122s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=7.3147e-01 | t=1.1536s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0039s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0032s
    tikhonov | MR=0.1 | seed=1 | MAE=2.9071e-01 | t=0.0097s
    tv | MR=0.1 | seed=1 | MAE=4.3066e-02 | t=0.2087s
    trss | MR=0.1 | seed=1 | MAE=3.0874e-02 | t=0.0162s

Completed: 2026-04-15T00:47:35.911616+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.