# Integration Log: scr_00257
Started: 2026-04-16T14:57:19.096568+00:00
Description: Screening scr_00257 ds=bci_iv2a_real_s3 graph=gaussian miss=3ch mode=base

## Dataset: bci_iv2a_real_s3 | rows=14
  Graph: gaussian__sigma1.0 built OK
    mean | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.0038s
    nearest | MR=3ch | seed=0 | MAE=4.0021e-07 | t=0.0067s
    tikhonov | MR=3ch | seed=0 | MAE=2.5129e-06 | t=0.0141s
    tv | MR=3ch | seed=0 | MAE=4.5067e-07 | t=0.7019s
    trss | MR=3ch | seed=0 | MAE=3.3028e-07 | t=0.0195s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=3.2259e-06 | t=0.0105s
    temporal_laplacian | MR=3ch | seed=0 | MAE=6.4823e-06 | t=12.9889s
    mean | MR=3ch | seed=1 | MAE=4.4119e-07 | t=0.0031s
    nearest | MR=3ch | seed=1 | MAE=3.7573e-07 | t=0.0064s
    tikhonov | MR=3ch | seed=1 | MAE=2.5136e-06 | t=0.0372s
    tv | MR=3ch | seed=1 | MAE=4.4119e-07 | t=1.0230s
    trss | MR=3ch | seed=1 | MAE=3.2113e-07 | t=0.3464s

Completed: 2026-04-16T14:57:19.097425+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.