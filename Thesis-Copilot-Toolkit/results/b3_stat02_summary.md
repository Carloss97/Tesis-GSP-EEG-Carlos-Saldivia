# STAT-02 Significance Report

## Resultado
- Se ejecutaron pruebas de significancia sobre comparaciones clave de B2.
- Regla: alpha=0.05.

## Pruebas con menor p-value

| test_id | metric | group_a | group_b | p_value | decision |
|---|---|---|---|---:|---|
| STAT-02_mae_trss_vs_bgsrp_mwu | mae | trss | bgsrp | 6.111e-259 | reject_H0 |
| STAT-02_mae_trss_vs_tikhonov_mwu | mae | trss | tikhonov | 4.688e-210 | reject_H0 |
| STAT-02_mae_bgsrp_vs_gsp_mwu | mae | bgsrp | gsp | 1.589e-114 | reject_H0 |
| STAT-02_mae_family_wilcoxon | mae | tv_time | instant | 4.770e-44 | reject_H0 |
| STAT-02_dtw_family_wilcoxon | dtw | tv_time | instant | 2.403e-12 | reject_H0 |
| STAT-02_mae_trss_vs_gsp_mwu | mae | trss | gsp | 9.810e-01 | fail_to_reject_H0 |

## Interpretacion
- El contraste principal instant vs TV/Tiempo se evalua con Wilcoxon pareado en contextos compartidos.
- Las comparaciones entre metodos clave se evalúan con Mann-Whitney U.
- Las conclusiones deben interpretarse junto con el estado proxy de INS-13 (pendiente 1:1 MATLAB/GSPBox).

