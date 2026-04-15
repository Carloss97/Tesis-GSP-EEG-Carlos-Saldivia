# Integration Log: it150_069
Started: 2026-04-15T00:50:57.568366+00:00
Description: Bulk normalized run it150_069 dataset=synthetic_alpha graph=knng miss=[0.1] mode=base

## Dataset: synthetic_alpha | rows=14
  Graph: knng built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0039s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0116s
    tikhonov | MR=0.1 | seed=0 | MAE=2.1342e-01 | t=0.0077s
    tv | MR=0.1 | seed=0 | MAE=4.5175e-02 | t=0.2307s
    trss | MR=0.1 | seed=0 | MAE=3.3546e-02 | t=0.0808s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.2916e-01 | t=0.0081s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.5087e-01 | t=1.1642s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0034s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0024s
    tikhonov | MR=0.1 | seed=1 | MAE=2.1230e-01 | t=0.0072s
    tv | MR=0.1 | seed=1 | MAE=4.4798e-02 | t=0.2049s
    trss | MR=0.1 | seed=1 | MAE=3.2584e-02 | t=0.0167s

Completed: 2026-04-15T00:50:57.569127+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.