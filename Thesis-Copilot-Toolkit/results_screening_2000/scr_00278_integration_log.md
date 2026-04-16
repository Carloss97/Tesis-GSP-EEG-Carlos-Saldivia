# Integration Log: scr_00278
Started: 2026-04-16T15:07:02.520840+00:00
Description: Screening scr_00278 ds=physionet_real graph=kalofolias miss=3ch mode=base

## Dataset: physionet_eegmmidb_real | rows=14
  Graph: kalofolias built OK
    mean | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.0028s
    nearest | MR=3ch | seed=0 | MAE=3.5155e-06 | t=0.0035s
    tikhonov | MR=3ch | seed=0 | MAE=1.1595e-05 | t=0.0063s
    tv | MR=3ch | seed=0 | MAE=3.0917e-06 | t=0.2964s
    trss | MR=3ch | seed=0 | MAE=2.2855e-06 | t=0.2235s
    graph_time_tikhonov | MR=3ch | seed=0 | MAE=1.9228e-05 | t=0.0255s
    temporal_laplacian | MR=3ch | seed=0 | MAE=3.3910e-05 | t=23.5408s
    mean | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.0030s
    nearest | MR=3ch | seed=1 | MAE=3.5329e-06 | t=0.0427s
    tikhonov | MR=3ch | seed=1 | MAE=1.1605e-05 | t=0.0087s
    tv | MR=3ch | seed=1 | MAE=3.0988e-06 | t=0.5566s
    trss | MR=3ch | seed=1 | MAE=2.2965e-06 | t=0.2849s

Completed: 2026-04-16T15:07:02.521732+00:00
Total rows: 14
INS-13 disclaimer: Results validated in Python proxy only. Do NOT claim 1:1 MATLAB/GSPBox equivalence.