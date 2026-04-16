# Integration Log: scr_00055
Started: 2026-04-16T14:41:09.487338+00:00
Description: Screening scr_00055 ds=iris_graph_signal graph=gaussian miss=1ch mode=base

## Dataset: iris_graph_signal | rows=14
  Graph: gaussian__sigma0.6 built OK
    mean | MR=1ch | seed=0 | MAE=1.2881e-01 | t=0.0014s
    nearest | MR=1ch | seed=0 | MAE=1.6484e-01 | t=0.0014s
    tikhonov | MR=1ch | seed=0 | MAE=1.4209e-01 | t=0.0044s
    tv | MR=1ch | seed=0 | MAE=1.0936e-01 | t=0.2002s
    trss | MR=1ch | seed=0 | MAE=1.0897e-01 | t=0.0036s
    graph_time_tikhonov | MR=1ch | seed=0 | MAE=2.1049e-01 | t=0.0040s
    temporal_laplacian | MR=1ch | seed=0 | MAE=3.8607e-01 | t=6.2932s
    mean | MR=1ch | seed=1 | MAE=1.3930e-01 | t=0.0017s
    nearest | MR=1ch | seed=1 | MAE=1.5346e-01 | t=0.0010s
    tikhonov | MR=1ch | seed=1 | MAE=1.5325e-01 | t=0.0027s
    tv | MR=1ch | seed=1 | MAE=1.2181e-01 | t=0.0585s
    trss | MR=1ch | seed=1 | MAE=1.1909e-01 | t=0.0027s

Completed: 2026-04-16T14:41:09.488255+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.