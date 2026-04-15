# Integration Log: it150_046
Started: 2026-04-15T00:48:51.088231+00:00
Description: Bulk normalized run it150_046 dataset=synthetic_beta graph=gaussian miss=[0.1] mode=base

## Dataset: synthetic_beta | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0030s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0029s
    tikhonov | MR=0.1 | seed=0 | MAE=2.0161e-01 | t=0.0081s
    tv | MR=0.1 | seed=0 | MAE=4.3871e-02 | t=0.2200s
    trss | MR=0.1 | seed=0 | MAE=3.2901e-02 | t=0.0158s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=4.1904e-01 | t=0.0112s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=6.3454e-01 | t=1.1862s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0038s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0050s
    tikhonov | MR=0.1 | seed=1 | MAE=2.0053e-01 | t=0.0141s
    tv | MR=0.1 | seed=1 | MAE=4.3702e-02 | t=0.4729s
    trss | MR=0.1 | seed=1 | MAE=3.2230e-02 | t=0.0414s

Completed: 2026-04-15T00:48:51.089092+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.