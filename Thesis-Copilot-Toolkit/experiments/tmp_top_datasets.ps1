param(
    [string]$graph,
    [string]$method
)
$csvPath = Join-Path (Resolve-Path (Join-Path $PSScriptRoot '..\results')).Path 'it05_all_datasets_raw.csv'
$csv = Import-Csv $csvPath
$rows = $csv | Where-Object { $_.graph -eq $graph -and $_.method -eq $method }
$processed = $rows | ForEach-Object {
    $m = $null
    if ($_.mae -and $_.mae -ne '') { $m = [double]::Parse($_.mae, [System.Globalization.CultureInfo]::InvariantCulture) }
    [pscustomobject]@{dataset=$_.dataset; mae=$m}
}
$processed | Sort-Object mae | Select-Object -First 10 | Format-Table -AutoSize
