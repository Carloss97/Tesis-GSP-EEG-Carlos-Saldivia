$scriptRoot = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$resultsDir = Join-Path -Path $scriptRoot -ChildPath '..\\results'
try { $resultsDir = (Resolve-Path $resultsDir -ErrorAction Stop).ProviderPath } catch { $resultsDir = Join-Path -Path (Get-Location) -ChildPath 'Thesis-Copilot-Toolkit\\results' }
$files = if (Test-Path $resultsDir) { Get-ChildItem -Path $resultsDir -Filter 'rerun_*_raw.csv' -Recurse -File -ErrorAction SilentlyContinue } else { @() }
$ids = @()
foreach($f in $files) {
    if ($f.Name -match '^rerun_(\d+)_.*_raw\\.csv') { $ids += [int]$matches[1] }
}
$ids = $ids | Sort-Object -Unique
$doneCount = $ids.Count
$expected = 0..208
$missing = $expected | Where-Object { $_ -notin $ids }
$missingCount = $missing.Count
$doneSamples = $ids | Select-Object -Last 5
Write-Output "DONE_COUNT:$doneCount"
Write-Output "MISSING_COUNT:$missingCount"
Write-Output ("DONE_SAMPLE:" + ($doneSamples -join ','))
$missingSample = ($missing | Select-Object -First 10) -join ','
Write-Output ("MISSING_SAMPLE:" + $missingSample)
$prog = Join-Path -Path $scriptRoot -ChildPath 'propose_and_try_mappings.progress.log'
$full = Join-Path -Path $scriptRoot -ChildPath 'propose_and_try_mappings.fullrun.log'
if (Test-Path $prog) { Write-Output "LAST_PROGRESS:"; Get-Content $prog -Tail 5 | ForEach-Object { Write-Output "  $_" } } else { Write-Output "LAST_PROGRESS: (none)" }
if (Test-Path $full) { Write-Output "LAST_FULL_LOG:"; Get-Content $full -Tail 40 | ForEach-Object { Write-Output "  $_" } } else { Write-Output "LAST_FULL_LOG: (none)" }
