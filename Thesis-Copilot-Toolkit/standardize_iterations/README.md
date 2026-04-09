# Estandarización de Iteraciones (it1-it130)

Este directorio contiene utilidades para recopilar y estandarizar los artefactos de las
iteraciones documentadas (it1–it130) en una estructura uniforme bajo
`Thesis-Copilot-Toolkit/standardized_results/`.

Archivos principales:

- `standardize_results.py`: Script Python que escanea el repositorio y copia artefactos a la carpeta estándar.
- `run_standardize.ps1`: Runner PowerShell simple para ejecutar el script (Windows).

Uso rápido (PowerShell):

```powershell
cd <workspace-root>
.\Thesis-Copilot-Toolkit\standardize_iterations\run_standardize.ps1 -SourceRoot . -TargetRoot Thesis-Copilot-Toolkit/standardized_results -Min 1 -Max 130
```

Modo dry-run (no copia, solo lista lo que hará):

```powershell
.\Thesis-Copilot-Toolkit\standardize_iterations\run_standardize.ps1 -DryRun
```

Salida esperada:

```
Thesis-Copilot-Toolkit/standardized_results/
├── it001_it01_xxx/
│   ├── raw.csv
│   ├── stats.csv
│   ├── figures/*.pdf
│   ├── tables/*.tex
│   └── metadata.json
└── index.json
```

Después de ejecutar, revise `Thesis-Copilot-Toolkit/standardized_results/index.json` para ver el estado
de cada iteración y los artefactos faltantes. Si faltan artefactos, el script generará
una lista en el campo `stored` de cada `metadata.json`.

Siguientes pasos sugeridos:

- Revisar iteraciones con artefactos faltantes y usar el motor `v9` para re-ejecutarlas.
- El script también puede adaptarse para ejecutar automáticamente los reruns (no implementado por defecto).
