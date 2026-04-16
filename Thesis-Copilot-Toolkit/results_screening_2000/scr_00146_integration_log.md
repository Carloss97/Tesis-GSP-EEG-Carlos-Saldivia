# Integration Log: scr_00146
Started: 2026-04-16T15:25:56.470059+00:00
Description: Screening scr_00146 ds=physionet_real graph=gaussian miss=2ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.0040s
    nearest | MR=2ch | seed=0 | MAE=2.3639e-06 | t=0.0058s
    tikhonov | MR=2ch | seed=0 | MAE=1.7194e-05 | t=0.0167s
    tv | MR=2ch | seed=0 | MAE=2.0892e-06 | t=0.4849s
    trss | MR=2ch | seed=0 | MAE=1.5091e-06 | t=0.1616s
    graph_time_tikhonov | MR=2ch | seed=0 | MAE=2.1962e-05 | t=0.0124s
    temporal_laplacian | MR=2ch | seed=0 | MAE=3.8773e-05 | t=25.4608s
    mean | MR=2ch | seed=1 | MAE=2.0496e-06 | t=0.0136s
    nearest | MR=2ch | seed=1 | MAE=2.3187e-06 | t=0.0060s
    tikhonov | MR=2ch | seed=1 | MAE=1.7210e-05 | t=0.0115s
    tv | MR=2ch | seed=1 | MAE=2.0495e-06 | t=0.5025s
    trss | MR=2ch | seed=1 | MAE=1.4817e-06 | t=0.0417s

Completed: 2026-04-16T15:25:56.472351+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.