# Integration Log: it150_060
Started: 2026-04-15T00:50:35.004752+00:00
Description: Bulk normalized run it150_060 dataset=synthetic_16ch graph=kalofolias miss=[0.1] mode=base

## Dataset: synthetic_16ch | rows=14
  Graph: kalofolias built OK
    mean | MR=0.1 | seed=0 | MAE=4.3607e-02 | t=0.0066s
    nearest | MR=0.1 | seed=0 | MAE=5.6541e-02 | t=0.0059s
    tikhonov | MR=0.1 | seed=0 | MAE=6.3170e-01 | t=0.0104s
    tv | MR=0.1 | seed=0 | MAE=4.3608e-02 | t=0.3641s
    trss | MR=0.1 | seed=0 | MAE=4.2793e-02 | t=0.1750s
    graph_time_tikhonov | MR=0.1 | seed=0 | MAE=6.3419e-01 | t=0.0093s
    temporal_laplacian | MR=0.1 | seed=0 | MAE=8.8943e-01 | t=1.1609s
    mean | MR=0.1 | seed=1 | MAE=4.3636e-02 | t=0.0025s
    nearest | MR=0.1 | seed=1 | MAE=5.7009e-02 | t=0.0030s
    tikhonov | MR=0.1 | seed=1 | MAE=6.3089e-01 | t=0.0081s
    tv | MR=0.1 | seed=1 | MAE=4.3637e-02 | t=0.1679s
    trss | MR=0.1 | seed=1 | MAE=4.1501e-02 | t=0.0279s

Completed: 2026-04-15T00:50:35.005890+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.