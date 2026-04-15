# Integration Log: it150_150
Started: 2026-04-15T00:58:34.694973+00:00
Description: Bulk normalized run it150_150 dataset=iv100hz_mat graph=kalofolias miss=[0.2] mode=base

## Dataset: iv100hz_mat | rows=14
  Graph: kalofolias built OK
    mean | MR=0.2 | seed=0 | MAE=1.6829e-02 | t=0.0020s
    nearest | MR=0.2 | seed=0 | MAE=2.5741e-02 | t=0.0052s
    tikhonov | MR=0.2 | seed=0 | MAE=5.7141e-02 | t=0.0094s
    tv | MR=0.2 | seed=0 | MAE=1.6699e-02 | t=0.2304s
    trss | MR=0.2 | seed=0 | MAE=6.5772e-03 | t=0.0208s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=5.7901e-02 | t=0.0113s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=1.1593e-01 | t=1.7352s
    mean | MR=0.2 | seed=1 | MAE=1.6767e-02 | t=0.0027s
    nearest | MR=0.2 | seed=1 | MAE=2.5796e-02 | t=0.0057s
    tikhonov | MR=0.2 | seed=1 | MAE=5.6779e-02 | t=0.0084s
    tv | MR=0.2 | seed=1 | MAE=1.6501e-02 | t=0.2216s
    trss | MR=0.2 | seed=1 | MAE=6.7102e-03 | t=0.0211s

Completed: 2026-04-15T00:58:34.695918+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.