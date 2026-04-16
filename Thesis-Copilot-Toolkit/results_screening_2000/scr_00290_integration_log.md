# Integration Log: scr_00290
Started: 2026-04-16T15:12:52.890368+00:00
Description: Screening scr_00290 ds=physionet_real graph=knng miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: knng built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0081s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0070s
    tikhonov | MR=3ch | seed=0 | MAE=6.1120e-06 | t=0.0106s
    tv | MR=3ch | seed=0 | MAE=3.0643e-06 | t=0.3758s
    trss | MR=3ch | seed=0 | MAE=1.5332e-06 | t=0.4323s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.2360e-05 | t=0.0083s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.0567e-05 | t=24.4505s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0033s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0054s
    tikhonov | MR=3ch | seed=1 | MAE=6.1253e-06 | t=0.0090s
    tv | MR=3ch | seed=1 | MAE=3.0728e-06 | t=0.7210s
    trss | MR=3ch | seed=1 | MAE=1.5045e-06 | t=0.5187s

Completed: 2026-04-16T15:12:52.891436+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.