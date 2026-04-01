# Tesis: Reconstrucción de EEG usando GSP e Interpolación

## Hipótesis
El uso de técnicas de interpolación basadas en grafos (GSP) permite reconstruir señales de EEG de manera más precisa que los métodos clásicos.

## Objetivos
1. Implementar y comparar distintos métodos de construcción de grafos para EEG.
2. Implementar y comparar métodos de interpolación (GSP y clásicos).
3. Evaluar el desempeño usando métricas objetivas (MAE, DTW, etc.).
4. Redactar paper científico y tesis extendida.

## Pipeline general
1. Input: Señal EEG y localización de electrodos
2. Construcción de grafo (varios métodos)
3. Interpolación de electrodos faltantes (varios métodos)
4. Evaluación cuantitativa (métricas)
5. Comparación y análisis de resultados
6. Redacción de resultados y discusión

## Estructura de carpetas
- /experiments: scripts y notebooks de experimentos
- /src: implementación modular de métodos
- /results: resultados, logs, figuras
- /paper: borrador del paper
- /thesis: borrador de la tesis
- /backlog.md: lista de tareas y métodos

## Checklist de validación y documentación mínima

- [ ] Todos los métodos principales tienen docstring y ejemplo de uso en el código.
- [ ] Existen scripts de ejemplo en /experiments para cada etapa del pipeline.
- [ ] Se puede ejecutar un pipeline completo (de datos a resultados) con un solo script.
- [ ] Las métricas y resultados generados son reproducibles (semillas fijas donde aplica).
- [ ] Hay instrucciones claras para instalar dependencias y ejecutar experimentos.
- [ ] Se han probado casos con datos sintéticos y reales.
- [ ] Los resultados clave (tablas/figuras) están guardados en /results y referenciados en el paper/tesis.
- [ ] Se han validado los métodos ante entradas erróneas (NaN, shapes inesperados, etc.).

### Sugerencia para pruebas automáticas

Se recomienda agregar un archivo `tests/test_pipeline.py` con pruebas mínimas:

```python
import numpy as np
from src.data import data_loader
from src.graph_construction import graph_constructors
from src.interpolation import interpolators
from src.evaluation import evaluation

def test_dummy_mean():
	x = np.array([[1., np.nan, 3.], [np.nan, 5., 6.]])
	A = np.eye(3)
	y = interpolators.interpolate('dummy_mean', x, A)['signals_reconstructed']
	assert not np.isnan(y).any()

def test_eval_1d():
	y = np.array([1., 2., 3.])
	p = np.array([1., 2., 2.])
	res = evaluation.evaluate_signals(y, p, ['mae', 'rmse', 'dtw', 'snr'])
	assert all(k in res for k in ['mae', 'rmse', 'dtw', 'snr'])
```

Esto ayuda a detectar errores futuros y mejora la reproducibilidad.