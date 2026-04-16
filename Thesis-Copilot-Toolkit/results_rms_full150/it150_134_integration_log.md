# Integration Log: it150_134
Started: 2026-04-15T00:56:39.635401+00:00
Description: Bulk normalized run it150_134 dataset=physionet_real graph=gaussian miss=[0.2] mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.0022s
    nearest | MR=0.2 | seed=0 | MAE=8.9975e-02 | t=0.0068s
    tikhonov | MR=0.2 | seed=0 | MAE=3.3759e-01 | t=0.0075s
    tv | MR=0.2 | seed=0 | MAE=7.8019e-02 | t=0.2279s
    trss | MR=0.2 | seed=0 | MAE=5.7729e-02 | t=0.0213s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.2108e-01 | t=0.0102s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=7.4721e-01 | t=1.8949s
    mean | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.0025s
    nearest | MR=0.2 | seed=1 | MAE=8.7931e-02 | t=0.0054s
    tikhonov | MR=0.2 | seed=1 | MAE=3.3826e-01 | t=0.0061s
    tv | MR=0.2 | seed=1 | MAE=7.7313e-02 | t=0.2331s
    trss | MR=0.2 | seed=1 | MAE=5.7092e-02 | t=0.0205s

Completed: 2026-04-15T00:56:39.636302+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.