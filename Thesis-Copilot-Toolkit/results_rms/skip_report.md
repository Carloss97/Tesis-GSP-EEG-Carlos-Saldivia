# Informe parcial: iteraciones saltadas

Fecha: 2026-04-14

Resumen:

- Total de iteraciones saltadas (snapshot parcial): 50
- Archivo origen de la lista: `rerun_selected_skipped.json`
- Estado del run: en ejecución (background). Este informe refleja el estado actual; lo actualizaré cuando finalice la ejecución.

Iteraciones saltadas (actual):

- rerun_0_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_1_bci_competition_iv_2a_proxy_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_2_bci_competition_iv_2a_proxy_knn__k3_directed_tv — no available datasets to run.
- rerun_3_mne_sample_knn__k3_directed_tv — no available datasets to run.
- rerun_4_mne_sample_knn__k3_directed_tv — no available datasets to run.
- rerun_5_mne_sample_knn__k3_directed_tv — no available datasets to run.
- rerun_6_synthetic_alpha_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_7_synthetic_alpha_kalofolias_directed_tv — no available datasets to run.
- rerun_8_synthetic_alpha_knn__k5_directed_tv — no available datasets to run.
- rerun_9_synthetic_alpha_knng__k4_sigma1_directed_tv — no available datasets to run.
- rerun_10_synthetic_alpha_vknng__alpha1_k4_k_max8_k_min2_directed_tv — no available datasets to run.
- rerun_11_synthetic_beta_aew__k4_sigma_corr0_5_sigma_dist1_directed_tv — no available datasets to run.
- rerun_12_synthetic_beta_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_13_synthetic_beta_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_14_synthetic_beta_kalofolias_directed_tv — no available datasets to run.
- rerun_15_synthetic_beta_kalofolias_directed_tv — no available datasets to run.
- rerun_16_synthetic_beta_knn__k5_directed_tv — no available datasets to run.
- rerun_17_synthetic_beta_vknng__alpha1_k4_k_max8_k_min2_directed_tv — no available datasets to run.
- rerun_18_synthetic_broad_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_19_synthetic_broad_gaussian__sigma1_directed_tv — no available datasets to run.
- rerun_20_synthetic_broad_kalofolias_directed_tv — no available datasets to run.
- rerun_21_synthetic_broad_kalofolias_directed_tv — no available datasets to run.
- rerun_22_synthetic_broad_knn__k5_directed_tv — no available datasets to run.
- rerun_23_synthetic_broad_knn__k5_directed_tv — no available datasets to run.
- rerun_24_synthetic_broad_knn__k5_directed_tv — no available datasets to run.
- rerun_25_synthetic_broad_knng__k4_sigma1_directed_tv — no available datasets to run.
- rerun_26_synthetic_broad_vknng__alpha1_k4_k_max8_k_min2_directed_tv — no available datasets to run.
- rerun_27_synthetic_16ch_kalofolias_graph_time_tikhonov — no available datasets to run.
- rerun_28_synthetic_beta_knng__k4_sigma1_gsmooth — no available datasets to run.
- rerun_29_synthetic_beta_nnk__k4_gsmooth — no available datasets to run.
- rerun_30_synthetic_beta_vknng__alpha1_k4_k_max8_k_min2_gsmooth — no available datasets to run.
- rerun_31_physionet_eegmmidb_knng__k4_sigma1_gsp — no available datasets to run.
- rerun_32_physionet_eegmmidb_vknng__alpha1_k4_k_max8_k_min2_gsp — no available datasets to run.
- rerun_33_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_34_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_35_bci_competition_iv_2a_proxy_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_36_mne_sample_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_37_mne_sample_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_38_mne_sample_kalofolias_heat_diffusion_temporal — no available datasets to run.
- rerun_39_mne_sample_knn__k3_heat_diffusion_temporal — no available datasets to run.
- rerun_40_synthetic_beta_gaussian__sigma1_heat_diffusion_temporal — no available datasets to run.
- rerun_41_synthetic_beta_knn__k3_heat_diffusion_temporal — no available datasets to run.
- rerun_42_synthetic_beta_knn__k3_heat_diffusion_temporal — no available datasets to run.
- rerun_43_synthetic_beta_knn__k3_heat_diffusion_temporal — no available datasets to run.
- rerun_44_synthetic_beta_knng__k4_sigma1_heat_diffusion_temporal — no available datasets to run.
- rerun_45_synthetic_beta_knng__k4_sigma1_heat_diffusion_temporal — no available datasets to run.
- rerun_46_synthetic_beta_knng__k4_sigma1_heat_diffusion_temporal — no available datasets to run.
- rerun_47_synthetic_beta_nnk__k4_heat_diffusion_temporal — no available datasets to run.
- rerun_48_synthetic_beta_nnk__k4_heat_diffusion_temporal — no available datasets to run.
- rerun_49_synthetic_broad_aew__k4_sigma_corr0_5_sigma_dist1_heat_diffusion_temporal — no available datasets to run.

Notas y acciones sugeridas:

1. Causa más frecuente: el motor de disponibilidad no encuentra los datasets solicitados por clave (por ejemplo, `mne_sample_proxy` vs `mne_sample`) o la entrada no cumple los criterios de disponibilidad.
2. Re-ejecutar una iteración concreta:

```powershell
$env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; & 'Thesis-Copilot-Toolkit\.venv\Scripts\python.exe' 'Thesis-Copilot-Toolkit\experiments\run_reruns_selected_rms.py' --tags rerun_31_physionet_eegmmidb_knng__k4_sigma1_gsp
```

3. Re-ejecutar todas las saltadas (PowerShell helper):

```powershell
$skipped = Get-Content .\Thesis-Copilot-Toolkit\results_rms\rerun_selected_skipped.json | ConvertFrom-Json
$tags = $skipped | ForEach-Object { $_.iteration } -join ' '
$env:NORMALIZE_DATASETS='1'; $env:NORM_METHOD='rms'; & 'Thesis-Copilot-Toolkit\\.venv\\Scripts\\python.exe' 'Thesis-Copilot-Toolkit\\experiments\\run_reruns_selected_rms.py' --tags $tags
```

4. Si la causa es `mne_sample_proxy` vs `mne_sample`, ya reemplacé las claves en `experiments/run_reruns_selected.py` y añadí la variante `experiments/run_reruns_selected_real.py`. Asegúrate de que el loader expone `mne_sample` (ya probado) y re-ejecuta los tags afectados.

5. Actualizaré este `skip_report.md` cuando finalice la ejecución y tenga el listado final y causas consolidadas.
