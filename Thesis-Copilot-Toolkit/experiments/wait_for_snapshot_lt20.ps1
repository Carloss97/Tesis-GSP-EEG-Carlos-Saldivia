$root = 'C:\Users\sarlo\OneDrive\Escritorio\Proyectos\Tesis-GSP-EEG-Carlos-Saldivia\Thesis-Copilot-Toolkit\results'
$pattern = 'reruns_lt20_*'
$initial = (Get-ChildItem $root -Directory | Where-Object { $_.Name -like $pattern }).Count
Write-Output "Waiting for new snapshot (initial count=$initial)."
while ((Get-ChildItem $root -Directory | Where-Object { $_.Name -like $pattern }).Count -le $initial) { Start-Sleep -Seconds 10 }
Write-Output 'SNAPSHOT_DETECTED'
Get-ChildItem $root -Directory | Where-Object { $_.Name -like $pattern } | Select-Object -ExpandProperty Name | Sort-Object | ForEach-Object { Write-Output "FOUND: $_" }
