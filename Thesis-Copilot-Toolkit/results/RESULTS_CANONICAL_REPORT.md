# Reporte Canónico Final — Experimento Unificado EEG-GSP

> Generado automáticamente por `run_canonical_experiment.py`
> Fecha: 2026-04-04 01:01
> Protocolo: Validación Anidada (inner=60% ajuste, outer=40% reporte)

## Resumen Ejecutivo

- **Corridas válidas (outer fold):** 2816
- **Datasets sintéticos:** 3 (synthetic_alpha, synthetic_beta, synthetic_broad)
- **Datasets reales incluidos:** 1 (physionet_eegmmidb — sujetos [1, 2, 3, 4, 5])
- **BCI Competition IV 2a:** NO DISPONIBLE — declarado formalmente como PROXY/EXCLUIDO de afirmaciones fuertes
- **Métodos de interpolación:** 22
- **Métodos de grafo:** 7
- **Niveles de pérdida:** ['10%', '20%', '30%', '40%']
- **Unidades de señal PhysioNet:** Voltios (EEG en V desde MNE; MAE ~1e-6 V es normal)

**Mejor método global** (menor MAE — outer fold): `mean` (familia: instant, MAE=1.2442e-01 ± 9.6541e-02)

## Declaración Explícita: BCI Competition IV 2a

> ⚠️ **BCI Competition IV 2a — PROXY / NO DISPONIBLE**
>
> BCI Competition IV Dataset 2a (.gdf) requires manual download from https://www.bbci.de/competition/iv/. Files not found in BCI_IV_2A_PATH. This dataset is formally declared as PROXY/NOT AVAILABLE for this run. Any results referencing bci_competition_iv_2a in this context are excluded from strong empirical claims.
>
> **Decisión formal:** Este dataset se excluye de todas las afirmaciones empíricas fuertes
> de este experimento. Los resultados sobre physionet_eegmmidb son los únicos resultados
> con datos EEG reales validados en esta corrida.

## 1. Ranking Global por MAE (outer fold)

|   rank | method                  | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |   n_runs |
|-------:|:------------------------|:---------|-------------:|-------------:|-------------:|-------------:|---------:|
|      1 | mean                    | instant  |   1.2442e-01 |   9.6541e-02 |   2.7079e-01 |   5.1083e-01 |      128 |
|      2 | tv                      | tv_time  |   1.2543e-01 |   9.6942e-02 |   2.7472e-01 |   4.4100e-01 |      128 |
|      3 | gsmooth                 | instant  |   1.2623e-01 |   9.7650e-02 |   2.7567e-01 |   5.4106e-01 |      128 |
|      4 | idw                     | instant  |   1.2714e-01 |   9.8841e-02 |   2.7861e-01 |   4.8330e-01 |      128 |
|      5 | directed_tv             | tv_time  |   1.3086e-01 |   9.6816e-02 |   2.9245e-01 |  -4.0621e-01 |      128 |
|      6 | trss                    | tv_time  |   1.3190e-01 |   1.0170e-01 |   2.9204e-01 |   1.8225e-01 |      128 |
|      7 | gsp                     | instant  |   1.3622e-01 |   1.0600e-01 |   3.0479e-01 |  -8.9835e-02 |      128 |
|      8 | wavelet_temporal        | tv_time  |   1.3805e-01 |   9.9843e-02 |   2.7205e-01 |   1.7992e+01 |      128 |
|      9 | linear                  | instant  |   1.4709e-01 |   1.1407e-01 |   3.3724e-01 |  -6.6319e-01 |      128 |
|     10 | nearest                 | instant  |   1.5996e-01 |   1.2444e-01 |   3.7233e-01 |  -1.5858e+00 |      128 |
|     11 | rbfi_tps                | instant  |   1.6243e-01 |   1.2774e-01 |   3.7476e-01 |  -1.6435e+00 |      128 |
|     12 | rbfi_mq                 | instant  |   1.7145e-01 |   1.3425e-01 |   3.9814e-01 |  -2.3225e+00 |      128 |
|     13 | spherical_spline        | instant  |   1.7981e-01 |   1.5130e-01 |   4.1529e-01 |  -2.5489e+00 |      128 |
|     14 | tikhonov                | instant  |   2.1372e-01 |   1.7160e-01 |   3.3095e-01 |   1.2867e+01 |      128 |
|     15 | spline_surface          | instant  |   2.1662e-01 |   1.5773e-01 |   5.8398e-01 |  -4.6491e+00 |      128 |
|     16 | heat_diffusion_temporal | tv_time  |   2.4936e-01 |   4.5831e-01 |   5.0489e-01 |  -1.2921e+00 |      128 |
|     17 | graph_time_tikhonov     | tv_time  |   3.0810e-01 |   2.0185e-01 |   3.8371e-01 |   5.2626e+00 |      128 |
|     18 | puy                     | instant  |   3.1298e-01 |   2.1485e-01 |   4.1099e-01 |   6.6263e+00 |      128 |
|     19 | temporal_laplacian      | tv_time  |   3.4479e-01 |   2.1214e-01 |   4.0323e-01 |   3.2700e+00 |      128 |
|     20 | bgsrp                   | instant  |   3.8062e-01 |   2.2511e-01 |   4.7451e-01 |   2.8177e+00 |      128 |
|     21 | sobolev                 | instant  |   4.1056e-01 |   2.4528e-01 |   4.6581e-01 |   1.9487e+00 |      128 |
|     22 | spline_temporal         | tv_time  | nan          | nan          | nan          | nan          |        0 |

## 2. Ranking por Dataset (outer fold)

### physionet_eegmmidb [REAL]

|   rank | method                  | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:------------------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal         | tv_time  | nan          | nan          | nan          | nan          |
|      1 | tv                      | tv_time  |   7.2649e-06 |   4.1334e-06 |   1.8102e-05 |   2.4210e+00 |
|      2 | mean                    | instant  |   7.2930e-06 |   4.1281e-06 |   1.8213e-05 |   2.3589e+00 |
|      3 | idw                     | instant  |   7.2962e-06 |   4.4271e-06 |   1.8207e-05 |   2.9799e+00 |
|      4 | gsmooth                 | instant  |   7.3196e-06 |   4.5211e-06 |   1.7822e-05 |   2.9866e+00 |
|      5 | linear                  | instant  |   7.4680e-06 |   5.3012e-06 |   1.9595e-05 |   3.2206e+00 |
|      6 | trss                    | tv_time  |   7.5096e-06 |   4.7756e-06 |   1.8319e-05 |   3.0092e+00 |
|      7 | heat_diffusion_temporal | tv_time  |   7.6670e-06 |   4.5741e-06 |   1.9762e-05 |   1.9296e+00 |
|      8 | gsp                     | instant  |   7.7244e-06 |   5.1100e-06 |   1.8831e-05 |   2.8901e+00 |
|      9 | nearest                 | instant  |   7.9533e-06 |   4.4845e-06 |   2.2744e-05 |   2.0708e+00 |
|     10 | directed_tv             | tv_time  |   8.5846e-06 |   4.9629e-06 |   2.2863e-05 |   7.0974e-01 |
|     11 | rbfi_tps                | instant  |   9.3600e-06 |   6.9169e-06 |   2.3432e-05 |   1.8543e+00 |
|     12 | wavelet_temporal        | tv_time  |   9.3951e-06 |   5.1210e-06 |   2.4514e-05 |   2.4395e+01 |
|     13 | rbfi_mq                 | instant  |   1.0605e-05 |   7.6603e-06 |   2.6426e-05 |   6.6638e-01 |
|     14 | tikhonov                | instant  |   1.2387e-05 |   5.1131e-06 |   2.1370e-05 |   1.4675e+01 |

### synthetic_alpha [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | mean             | instant  |   1.6334e-01 |   7.9787e-02 |   3.5094e-01 |   3.3292e-01 |
|      2 | tv               | tv_time  |   1.6763e-01 |   7.8373e-02 |   3.6292e-01 |   3.4563e-03 |
|      3 | gsmooth          | instant  |   1.7107e-01 |   8.1079e-02 |   3.6871e-01 |  -1.7791e-01 |
|      4 | idw              | instant  |   1.7152e-01 |   8.3050e-02 |   3.6912e-01 |  -1.1213e-01 |
|      5 | wavelet_temporal | tv_time  |   1.7852e-01 |   7.3204e-02 |   3.5739e-01 |   1.8708e+01 |
|      6 | directed_tv      | tv_time  |   1.8581e-01 |   6.6797e-02 |   4.1858e-01 |  -1.3602e+00 |
|      7 | trss             | tv_time  |   1.8738e-01 |   8.5359e-02 |   4.0986e-01 |  -1.1457e+00 |
|      8 | gsp              | instant  |   1.9770e-01 |   9.2878e-02 |   4.3674e-01 |  -1.6048e+00 |
|      9 | linear           | instant  |   2.0691e-01 |   1.0048e-01 |   4.6452e-01 |  -1.9668e+00 |
|     10 | nearest          | instant  |   2.1614e-01 |   1.0524e-01 |   4.9427e-01 |  -2.4241e+00 |
|     11 | rbfi_tps         | instant  |   2.3313e-01 |   1.1008e-01 |   5.3274e-01 |  -3.1681e+00 |
|     12 | rbfi_mq          | instant  |   2.3943e-01 |   1.1270e-01 |   5.5096e-01 |  -3.4469e+00 |
|     13 | spherical_spline | instant  |   2.9032e-01 |   1.3598e-01 |   6.8001e-01 |  -5.0394e+00 |
|     14 | tikhonov         | instant  |   2.9190e-01 |   1.2941e-01 |   4.5240e-01 |   1.1960e+01 |

### synthetic_beta [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | gsmooth          | instant  |   1.7110e-01 |   8.1584e-02 |   3.6739e-01 |  -1.9719e-01 |
|      2 | tv               | tv_time  |   1.7112e-01 |   8.2375e-02 |   3.6723e-01 |  -1.6669e-01 |
|      3 | mean             | instant  |   1.7161e-01 |   8.1698e-02 |   3.6622e-01 |  -2.1668e-01 |
|      4 | idw              | instant  |   1.7173e-01 |   8.1311e-02 |   3.6916e-01 |  -2.7979e-01 |
|      5 | directed_tv      | tv_time  |   1.7278e-01 |   7.6082e-02 |   3.7457e-01 |  -3.7907e-01 |
|      6 | trss             | tv_time  |   1.7452e-01 |   8.1539e-02 |   3.8106e-01 |  -4.5590e-01 |
|      7 | gsp              | instant  |   1.7747e-01 |   8.3358e-02 |   3.9082e-01 |  -6.4933e-01 |
|      8 | wavelet_temporal | tv_time  |   1.9180e-01 |   7.4714e-02 |   3.6797e-01 |   1.4211e+01 |
|      9 | linear           | instant  |   1.9617e-01 |   8.6532e-02 |   4.4919e-01 |  -2.0262e+00 |
|     10 | rbfi_tps         | instant  |   2.1430e-01 |   1.0112e-01 |   4.8820e-01 |  -2.6046e+00 |
|     11 | rbfi_mq          | instant  |   2.1704e-01 |   1.0001e-01 |   4.9700e-01 |  -2.7717e+00 |
|     12 | nearest          | instant  |   2.2134e-01 |   1.0373e-01 |   5.1092e-01 |  -3.1532e+00 |
|     13 | spherical_spline | instant  |   2.6615e-01 |   1.3239e-01 |   6.1514e-01 |  -4.3608e+00 |
|     14 | tikhonov         | instant  |   2.8521e-01 |   1.4756e-01 |   4.3483e-01 |   1.2347e+01 |

### synthetic_broad [SYNTHETIC]

|   rank | method           | family   |     mae_mean |      mae_std |    rmse_mean |     snr_mean |
|-------:|:-----------------|:---------|-------------:|-------------:|-------------:|-------------:|
|      0 | spline_temporal  | tv_time  | nan          | nan          | nan          | nan          |
|      1 | mean             | instant  |   1.6274e-01 |   6.1539e-02 |   3.6599e-01 |  -4.3184e-01 |
|      2 | spherical_spline | instant  |   1.6274e-01 |   6.1539e-02 |   3.6599e-01 |  -4.3184e-01 |
|      3 | gsmooth          | instant  |   1.6276e-01 |   6.2113e-02 |   3.6656e-01 |  -4.4726e-01 |
|      4 | tv               | tv_time  |   1.6297e-01 |   6.2346e-02 |   3.6872e-01 |  -4.9376e-01 |
|      5 | directed_tv      | tv_time  |   1.6484e-01 |   6.5982e-02 |   3.7662e-01 |  -5.9531e-01 |
|      6 | idw              | instant  |   1.6531e-01 |   6.5120e-02 |   3.7613e-01 |  -6.5483e-01 |
|      7 | trss             | tv_time  |   1.6570e-01 |   6.5162e-02 |   3.7722e-01 |  -6.7865e-01 |
|      8 | gsp              | instant  |   1.6969e-01 |   6.7036e-02 |   3.9158e-01 |  -9.9534e-01 |
|      9 | wavelet_temporal | tv_time  |   1.8188e-01 |   5.9764e-02 |   3.6280e-01 |   1.4656e+01 |
|     10 | linear           | instant  |   1.8528e-01 |   7.5527e-02 |   4.3521e-01 |  -1.8803e+00 |
|     11 | rbfi_tps         | instant  |   2.0230e-01 |   8.7711e-02 |   4.7806e-01 |  -2.6556e+00 |
|     12 | spline_surface   | instant  |   2.0230e-01 |   8.7711e-02 |   4.7806e-01 |  -2.6556e+00 |
|     13 | nearest          | instant  |   2.0236e-01 |   7.8676e-02 |   4.8412e-01 |  -2.8368e+00 |
|     14 | rbfi_mq          | instant  |   2.2932e-01 |   1.0207e-01 |   5.4458e-01 |  -3.7377e+00 |

## 3. Top-5 por Dataset × Nivel de Pérdida × Familia

| dataset            |   missing_ratio | family   |   rank | method                  |   mae_mean |
|:-------------------|----------------:|:---------|-------:|:------------------------|-----------:|
| physionet_eegmmidb |      1.0000e-01 | instant  |      1 | rbfi_tps                | 1.8864e-06 |
| physionet_eegmmidb |      1.0000e-01 | instant  |      2 | gsp                     | 1.8896e-06 |
| physionet_eegmmidb |      1.0000e-01 | instant  |      3 | idw                     | 1.9471e-06 |
| physionet_eegmmidb |      1.0000e-01 | instant  |      4 | gsmooth                 | 1.9850e-06 |
| physionet_eegmmidb |      1.0000e-01 | instant  |      5 | linear                  | 2.1284e-06 |
| physionet_eegmmidb |      1.0000e-01 | tv_time  |      1 | trss                    | 1.8930e-06 |
| physionet_eegmmidb |      1.0000e-01 | tv_time  |      2 | heat_diffusion_temporal | 2.0737e-06 |
| physionet_eegmmidb |      1.0000e-01 | tv_time  |      3 | directed_tv             | 2.2354e-06 |
| physionet_eegmmidb |      1.0000e-01 | tv_time  |      4 | tv                      | 2.3573e-06 |
| physionet_eegmmidb |      1.0000e-01 | tv_time  |      5 | wavelet_temporal        | 2.7774e-06 |
| physionet_eegmmidb |      2.0000e-01 | instant  |      1 | linear                  | 3.3158e-06 |
| physionet_eegmmidb |      2.0000e-01 | instant  |      2 | mean                    | 4.5685e-06 |
| physionet_eegmmidb |      2.0000e-01 | instant  |      3 | gsmooth                 | 4.5916e-06 |
| physionet_eegmmidb |      2.0000e-01 | instant  |      4 | gsp                     | 4.8417e-06 |
| physionet_eegmmidb |      2.0000e-01 | instant  |      5 | idw                     | 4.9154e-06 |
| physionet_eegmmidb |      2.0000e-01 | tv_time  |      1 | tv                      | 4.5309e-06 |
| physionet_eegmmidb |      2.0000e-01 | tv_time  |      2 | trss                    | 4.7523e-06 |
| physionet_eegmmidb |      2.0000e-01 | tv_time  |      3 | heat_diffusion_temporal | 4.9502e-06 |
| physionet_eegmmidb |      2.0000e-01 | tv_time  |      4 | directed_tv             | 5.9124e-06 |
| physionet_eegmmidb |      2.0000e-01 | tv_time  |      5 | wavelet_temporal        | 6.7230e-06 |
| physionet_eegmmidb |      3.0000e-01 | instant  |      1 | nearest                 | 8.5202e-06 |
| physionet_eegmmidb |      3.0000e-01 | instant  |      2 | idw                     | 8.7333e-06 |
| physionet_eegmmidb |      3.0000e-01 | instant  |      3 | rbfi_tps                | 8.7810e-06 |
| physionet_eegmmidb |      3.0000e-01 | instant  |      4 | gsmooth                 | 9.1475e-06 |
| physionet_eegmmidb |      3.0000e-01 | instant  |      5 | linear                  | 9.2060e-06 |
| physionet_eegmmidb |      3.0000e-01 | tv_time  |      1 | trss                    | 9.2793e-06 |
| physionet_eegmmidb |      3.0000e-01 | tv_time  |      2 | tv                      | 9.4362e-06 |
| physionet_eegmmidb |      3.0000e-01 | tv_time  |      3 | heat_diffusion_temporal | 9.9302e-06 |
| physionet_eegmmidb |      3.0000e-01 | tv_time  |      4 | directed_tv             | 1.1185e-05 |
| physionet_eegmmidb |      3.0000e-01 | tv_time  |      5 | wavelet_temporal        | 1.2104e-05 |
| physionet_eegmmidb |      4.0000e-01 | instant  |      1 | mean                    | 1.2743e-05 |
| physionet_eegmmidb |      4.0000e-01 | instant  |      2 | gsmooth                 | 1.3554e-05 |
| physionet_eegmmidb |      4.0000e-01 | instant  |      3 | idw                     | 1.3589e-05 |
| physionet_eegmmidb |      4.0000e-01 | instant  |      4 | nearest                 | 1.4855e-05 |
| physionet_eegmmidb |      4.0000e-01 | instant  |      5 | gsp                     | 1.4883e-05 |
| physionet_eegmmidb |      4.0000e-01 | tv_time  |      1 | tv                      | 1.2735e-05 |
| physionet_eegmmidb |      4.0000e-01 | tv_time  |      2 | heat_diffusion_temporal | 1.3714e-05 |
| physionet_eegmmidb |      4.0000e-01 | tv_time  |      3 | trss                    | 1.4114e-05 |
| physionet_eegmmidb |      4.0000e-01 | tv_time  |      4 | directed_tv             | 1.5005e-05 |
| physionet_eegmmidb |      4.0000e-01 | tv_time  |      5 | wavelet_temporal        | 1.5977e-05 |
| synthetic_alpha    |      1.0000e-01 | instant  |      1 | mean                    | 5.8948e-02 |
| synthetic_alpha    |      1.0000e-01 | instant  |      2 | idw                     | 6.2584e-02 |
| synthetic_alpha    |      1.0000e-01 | instant  |      3 | linear                  | 6.3427e-02 |
| synthetic_alpha    |      1.0000e-01 | instant  |      4 | nearest                 | 6.4277e-02 |
| synthetic_alpha    |      1.0000e-01 | instant  |      5 | gsmooth                 | 6.5647e-02 |
| synthetic_alpha    |      1.0000e-01 | tv_time  |      1 | tv                      | 6.4045e-02 |
| synthetic_alpha    |      1.0000e-01 | tv_time  |      2 | trss                    | 7.8153e-02 |
| synthetic_alpha    |      1.0000e-01 | tv_time  |      3 | wavelet_temporal        | 8.1802e-02 |
| synthetic_alpha    |      1.0000e-01 | tv_time  |      4 | directed_tv             | 9.6381e-02 |
| synthetic_alpha    |      1.0000e-01 | tv_time  |      5 | heat_diffusion_temporal | 1.3940e-01 |
| synthetic_alpha    |      2.0000e-01 | instant  |      1 | mean                    | 1.2085e-01 |
| synthetic_alpha    |      2.0000e-01 | instant  |      2 | gsmooth                 | 1.2861e-01 |
| synthetic_alpha    |      2.0000e-01 | instant  |      3 | idw                     | 1.2894e-01 |
| synthetic_alpha    |      2.0000e-01 | instant  |      4 | gsp                     | 1.5659e-01 |
| synthetic_alpha    |      2.0000e-01 | instant  |      5 | linear                  | 1.7712e-01 |
| synthetic_alpha    |      2.0000e-01 | tv_time  |      1 | tv                      | 1.2777e-01 |
| synthetic_alpha    |      2.0000e-01 | tv_time  |      2 | trss                    | 1.4811e-01 |
| synthetic_alpha    |      2.0000e-01 | tv_time  |      3 | wavelet_temporal        | 1.4820e-01 |
| synthetic_alpha    |      2.0000e-01 | tv_time  |      4 | directed_tv             | 1.7036e-01 |
| synthetic_alpha    |      2.0000e-01 | tv_time  |      5 | heat_diffusion_temporal | 2.7226e-01 |

## 4. Mejor Método por Dataset × Nivel de Pérdida

| dataset            | data_source   |   missing_ratio | method                  | family   |   best_mae |   best_rmse |   best_snr |
|:-------------------|:--------------|----------------:|:------------------------|:---------|-----------:|------------:|-----------:|
| physionet_eegmmidb | real          |      1.0000e-01 | gsp                     | instant  | 1.6827e-06 |  7.7569e-06 | 3.0427e+00 |
| physionet_eegmmidb | real          |      2.0000e-01 | linear                  | instant  | 3.3158e-06 |  1.1367e-05 | 6.7948e+00 |
| physionet_eegmmidb | real          |      3.0000e-01 | trss                    | tv_time  | 8.2528e-06 |  1.9039e-05 | 5.4531e+00 |
| physionet_eegmmidb | real          |      4.0000e-01 | trss                    | tv_time  | 1.2274e-05 |  2.4223e-05 | 3.7545e+00 |
| synthetic_alpha    | synthetic     |      1.0000e-01 | mean                    | instant  | 5.8948e-02 |  2.0853e-01 | 9.4764e-01 |
| synthetic_alpha    | synthetic     |      2.0000e-01 | tv                      | tv_time  | 1.2012e-01 |  2.9983e-01 | 8.1435e-01 |
| synthetic_alpha    | synthetic     |      3.0000e-01 | directed_tv             | tv_time  | 1.9947e-01 |  3.9782e-01 | 5.1599e-03 |
| synthetic_alpha    | synthetic     |      4.0000e-01 | tv                      | tv_time  | 2.6030e-01 |  4.6011e-01 | 1.4142e-01 |
| synthetic_beta     | synthetic     |      1.0000e-01 | tv                      | tv_time  | 6.4535e-02 |  2.2818e-01 | 3.2316e-02 |
| synthetic_beta     | synthetic     |      2.0000e-01 | tv                      | tv_time  | 1.1561e-01 |  3.0882e-01 | 2.0733e+00 |
| synthetic_beta     | synthetic     |      3.0000e-01 | trss                    | tv_time  | 1.8885e-01 |  3.9229e-01 | 8.2275e-01 |
| synthetic_beta     | synthetic     |      4.0000e-01 | directed_tv             | tv_time  | 2.5551e-01 |  4.7932e-01 | 5.6148e-01 |
| synthetic_broad    | synthetic     |      1.0000e-01 | directed_tv             | tv_time  | 7.5694e-02 |  2.5876e-01 | 8.4077e-02 |
| synthetic_broad    | synthetic     |      2.0000e-01 | directed_tv             | tv_time  | 1.1815e-01 |  3.0736e-01 | 4.0528e-02 |
| synthetic_broad    | synthetic     |      3.0000e-01 | heat_diffusion_temporal | tv_time  | 1.9707e-01 |  3.9523e-01 | 3.5884e-03 |
| synthetic_broad    | synthetic     |      4.0000e-01 | heat_diffusion_temporal | tv_time  | 2.3516e-01 |  4.3308e-01 | 1.2652e-02 |

## 5. Sensibilidad al Método de Grafo (Top-20)

| graph_method   | method                  |   mae_mean |
|:---------------|:------------------------|-----------:|
| aew            | heat_diffusion_temporal | 1.2310e-01 |
| aew            | trss                    | 1.2341e-01 |
| kalofolias     | directed_tv             | 1.2353e-01 |
| gaussian       | heat_diffusion_temporal | 1.2393e-01 |
| aew            | gsmooth                 | 1.2430e-01 |
| aew            | mean                    | 1.2442e-01 |
| kalofolias     | mean                    | 1.2442e-01 |
| gaussian       | mean                    | 1.2442e-01 |
| knng           | mean                    | 1.2442e-01 |
| nnk            | mean                    | 1.2442e-01 |
| knn            | mean                    | 1.2442e-01 |
| vknng          | mean                    | 1.2442e-01 |
| kalofolias     | tv                      | 1.2444e-01 |
| gaussian       | directed_tv             | 1.2448e-01 |
| gaussian       | tv                      | 1.2453e-01 |
| nnk            | heat_diffusion_temporal | 1.2456e-01 |
| gaussian       | gsmooth                 | 1.2472e-01 |
| knng           | heat_diffusion_temporal | 1.2476e-01 |
| vknng          | tv                      | 1.2488e-01 |
| knng           | tv                      | 1.2525e-01 |

## 6. Comparación de Familias por Tipo de Dato

| data_source   | family   |   mae_mean |    mae_std |   rmse_mean |   snr_mean |   n_runs |
|:--------------|:---------|-----------:|-----------:|------------:|-----------:|---------:|
| real          | tv_time  | 1.2681e-05 | 8.8192e-06 |  2.4927e-05 | 6.0405e+00 |      224 |
| real          | instant  | 1.2915e-05 | 9.1863e-06 |  2.6876e-05 | 3.3567e+00 |      448 |
| synthetic     | tv_time  | 2.7209e-01 | 2.3475e-01 |  4.6153e-01 | 2.8341e+00 |      672 |
| synthetic     | instant  | 2.7326e-01 | 1.5611e-01 |  5.0417e-01 | 5.1793e-02 |     1344 |

## 7. Figuras Generadas

- **canonical_mae_ranking_bar.png**: Ranking global de métodos por MAE (outer fold)
- **canonical_dataset_comparison.png**: Comparación métodos top por dataset
- **canonical_heatmap_mae.png**: Heatmap MAE: grafo × método
- **canonical_mae_vs_missing.png**: MAE vs. nivel de pérdida
- **canonical_family_boxplot.png**: Boxplot familias por tipo de dato

## 8. Notas Metodológicas

- Selección de parámetros: inner-fold temporal (60% primeras muestras) con búsqueda exhaustiva en grilla; evaluación final en outer-fold (40% últimas muestras).
- Datasets sintéticos (alpha/beta/broad): señales EEG simuladas con frecuencias en bandas características y geometría esférica/circular. Son la base robusta del análisis.
- Dataset real: physionet_eegmmidb (sujetos [1, 2, 3, 4, 5], run motor imagery). Cargado desde archivos EDF locales (22 canales subseleccionados, 160 Hz). Señales en Voltios; MAE del orden de 1e-6 V es esperado y correcto para EEG en V.
- BCI Competition IV 2a: archivos .gdf no disponibles. Declarado formalmente como proxy/excluido. No se hacen afirmaciones empíricas sobre este dataset.
- Métrica primaria: MAE. RMSE y SNR como métricas secundarias. DTW omitido en corrida completa para eficiencia (ver resultados previos en unified_final_raw.csv).
- Los grafos se construyen sobre el conjunto completo de señales para topología estable.
