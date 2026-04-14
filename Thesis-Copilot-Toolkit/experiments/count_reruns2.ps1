$resultsPath = Join-Path (Get-Location) 'Thesis-Copilot-Toolkit\results'
$files = Get-ChildItem -Path $resultsPath -Filter 'rerun_*_raw.csv' -Recurse -File -ErrorAction SilentlyContinue
$ids = $files | ForEach-Object { if ($_.Name -match '^rerun_(\d+)_') { [int]$matches[1] } } | Sort-Object -Unique
$doneCount = $ids.Count
$expected = 0..208
$missing = $expected | Where-Object { $_ -notin $ids }
$missingCount = $missing.Count
Write-Output "DONE_COUNT:$doneCount"
Write-Output "MISSING_COUNT:$missingCount"
Write-Output ("DONE_SAMPLE:" + ($ids | Select-Object -Last 5 -join ','))
Write-Output ("MISSING_SAMPLE:" + (($missing | Select-Object -First 10) -join ','))
if (Test-Path '.\Thesis-Copilot-Toolkit\experiments\propose_and_try_mappings.progress.log') { Write-Output 'LAST_PROGRESS:'; Get-Content '.\Thesis-Copilot-Toolkit\experiments\propose_and_try_mappings.progress.log' -Tail 5 | ForEach-Object { Write-Output "  $_" } } else { Write-Output 'LAST_PROGRESS: (none)'}
if (Test-Path '.\Thesis-Copilot-Toolkit\experiments\propose_and_try_mappings.fullrun.log') { Write-Output 'LAST_FULL_LOG:'; Get-Content '.\Thesis-Copilot-Toolkit\experiments\propose_and_try_mappings.fullrun.log' -Tail 40 | ForEach-Object { Write-Output "  $_" } } else { Write-Output 'LAST_FULL_LOG: (none)'}
