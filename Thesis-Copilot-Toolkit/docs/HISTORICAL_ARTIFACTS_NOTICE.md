# Aviso sobre artefactos históricos

Fecha: 2026-04-18

Este repositorio contiene artefactos (resultados, CSV, informes y planificaciones) generados a lo largo de múltiples iteraciones experimentales. Algunos de esos artefactos contienen referencias a métodos o datasets que han sido retirados de la ejecución operativa por decisión de revisión científica o por motivos operativos.

Métodos / datasets señalados como HISTÓRICOS (no ejecutar por defecto):

- `heat_diffusion_temporal`
- `wavelet_temporal`
- `directed_tv` (excluido temporalmente en la fase actual)
- `iv100hz_mat` (dataset MAT 100Hz; excluido de ejecuciones automáticas)

Política de uso:

- Estos artefactos permanecen en el repositorio por trazabilidad (reproducibilidad, análisis retrospectivo y documentación). No deben eliminarse.
- No se programarán reruns automáticos que incluyan los métodos/datasets listados arriba salvo que:
  1. Un investigador documente explícitamente la razón técnica/científica en la solicitud de rerun.
  2. Se añada una nota en el commit/merge request justificando la re-ejecución.

Cómo tratarlos en código y planificación:

- Los scripts de planificación y orquestación (p.ej. `experiments/run_future_work_*.py`, `experiments/propose_mapping_run_summary.json`) han sido parcheados para filtrar estas entradas por defecto.
- Si necesita ejecutar alguno de estos métodos por motivos de investigación, use una rama experimental y documente la motivación en el PR.

Contacto:

- Para soporte operativo o preguntas sobre esta decisión, abra un issue o contacte al responsable del experimento.

