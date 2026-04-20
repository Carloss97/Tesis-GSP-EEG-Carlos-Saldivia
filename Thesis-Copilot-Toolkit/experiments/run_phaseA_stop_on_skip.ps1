param(
    [string]$envName = "eegrasp",
    [string]$schedule = "Thesis-Copilot-Toolkit/experiments/schedules/it01-it50_schedule_phaseA_real_varied.json",
    [string]$runner = "Thesis-Copilot-Toolkit/experiments/run_schedule_pilot.py",
    [string]$logFile = "Thesis-Copilot-Toolkit/results/phaseA_run_log.txt"
)

$ErrorActionPreference = "Stop"

Write-Host "== Phase A pilot launcher: using conda env -> $envName =="

try {
    Write-Host "Activating conda environment: $envName"
    conda activate $envName
} catch {
    Write-Host "ERROR: 'conda activate' falló. Abra 'Anaconda Powershell Prompt' o inicialice conda para PowerShell." -ForegroundColor Yellow
    Write-Host "Alternativa: ejecute manualmente:" -ForegroundColor Yellow
    Write-Host "  conda activate $envName" -ForegroundColor Yellow
    Write-Host "  python $runner --schedule $schedule --stop-on-error" -ForegroundColor Yellow
    exit 1
}

Write-Host "Ejecutando Phase A pilot (se detendrá al primer skip). Salida también en: $logFile"

# Asegurar carpeta results
$resultsDir = Join-Path -Path "Thesis-Copilot-Toolkit" -ChildPath "results"
if (-not (Test-Path $resultsDir)) { New-Item -ItemType Directory -Path $resultsDir | Out-Null }

# Ejecutar y guardar log (también imprime en consola)
& python $runner --schedule $schedule --stop-on-error 2>&1 | Tee-Object -FilePath $logFile

$ec = $LASTEXITCODE
if ($ec -eq 0) {
    Write-Host "Phase A pilot finalizó sin skips (exit code 0)." -ForegroundColor Green
} else {
    Write-Host "Phase A pilot terminó con código $ec. Revisa 'Thesis-Copilot-Toolkit/results/pilot_skipped_iterations.json' y $logFile" -ForegroundColor Red
}

exit $ec
