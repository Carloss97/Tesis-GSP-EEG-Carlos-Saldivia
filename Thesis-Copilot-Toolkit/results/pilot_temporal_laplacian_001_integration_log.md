# Integration Log: pilot_temporal_laplacian_001
Started: 2026-04-18T03:36:41.466787+00:00
Description: Pilot: temporal_laplacian inclusion check

## Dataset: bci_iv2a_real_s1 | rows=12
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=8.5828e-02 | t=0.0024s
    nearest | MR=0.2 | seed=0 | MAE=7.9901e-02 | t=0.0125s
    tikhonov | MR=0.2 | seed=0 | MAE=1.6862e-01 | t=0.0074s
    trss | MR=0.2 | seed=0 | MAE=6.2563e-02 | t=0.0219s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.8750e-01 | t=0.0117s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=4.7132e-01 | t=2.7821s
    mean | MR=0.2 | seed=1 | MAE=8.8933e-02 | t=0.0030s
    nearest | MR=0.2 | seed=1 | MAE=8.2138e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=1 | MAE=1.6858e-01 | t=0.0070s
    trss | MR=0.2 | seed=1 | MAE=6.4636e-02 | t=0.0413s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.8309e-01 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=4.6851e-01 | t=3.0567s

## Dataset: iris_graph_signal | rows=12
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=1.2881e-01 | t=0.0010s
    nearest | MR=0.2 | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=0.2 | seed=0 | MAE=2.6763e-01 | t=0.0028s
    trss | MR=0.2 | seed=0 | MAE=1.1223e-01 | t=0.0036s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=4.1809e-01 | t=0.0025s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=6.1214e-01 | t=0.0333s
    mean | MR=0.2 | seed=1 | MAE=1.3930e-01 | t=0.0009s
    nearest | MR=0.2 | seed=1 | MAE=1.5346e-01 | t=0.0010s
    tikhonov | MR=0.2 | seed=1 | MAE=2.7086e-01 | t=0.0030s
    trss | MR=0.2 | seed=1 | MAE=1.2000e-01 | t=0.0029s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=4.1540e-01 | t=0.0033s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=6.1330e-01 | t=0.2587s

## Dataset: iv100hz_mat | rows=12
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=2.1337e-02 | t=0.0026s
    nearest | MR=0.2 | seed=0 | MAE=3.2157e-02 | t=0.0055s
    tikhonov | MR=0.2 | seed=0 | MAE=4.4294e-02 | t=0.0057s
    trss | MR=0.2 | seed=0 | MAE=1.7424e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=6.9567e-02 | t=0.0080s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=8.2842e-02 | t=1.5467s
    mean | MR=0.2 | seed=1 | MAE=2.1439e-02 | t=0.0020s
    nearest | MR=0.2 | seed=1 | MAE=3.2220e-02 | t=0.0051s
    tikhonov | MR=0.2 | seed=1 | MAE=4.4724e-02 | t=0.0062s
    trss | MR=0.2 | seed=1 | MAE=1.8031e-02 | t=0.0206s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=6.9767e-02 | t=0.0081s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=8.2653e-02 | t=1.8673s

## Dataset: physionet_eegmmidb_real | rows=12
  Graph: knn__k3 built OK
    mean | MR=0.2 | seed=0 | MAE=9.8565e-02 | t=0.0035s
    nearest | MR=0.2 | seed=0 | MAE=1.0944e-01 | t=0.0063s
    tikhonov | MR=0.2 | seed=0 | MAE=1.1602e-01 | t=0.0093s
    trss | MR=0.2 | seed=0 | MAE=4.8933e-02 | t=0.0279s
    graph_time_tikhonov | MR=0.2 | seed=0 | MAE=2.1088e-01 | t=0.0113s
    temporal_laplacian | MR=0.2 | seed=0 | MAE=5.6397e-01 | t=3.0853s
    mean | MR=0.2 | seed=1 | MAE=9.9814e-02 | t=0.0021s
    nearest | MR=0.2 | seed=1 | MAE=1.1253e-01 | t=0.0050s
    tikhonov | MR=0.2 | seed=1 | MAE=1.1436e-01 | t=0.0078s
    trss | MR=0.2 | seed=1 | MAE=4.7936e-02 | t=0.0193s
    graph_time_tikhonov | MR=0.2 | seed=1 | MAE=2.1011e-01 | t=0.0082s
    temporal_laplacian | MR=0.2 | seed=1 | MAE=5.6722e-01 | t=2.7864s

Completed: 2026-04-18T03:36:41.470262+00:00
Total rows: 48
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.