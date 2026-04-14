$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$aggPath = Join-Path $root 'analysis_it05_it20_multicriteria_agg.csv'
if (-not (Test-Path $aggPath)) { Write-Error "Aggregation CSV not found: $aggPath"; exit 1 }

function ParseFloat($s) {
    if ($null -eq $s -or $s -eq '') { return $null }
    $t = $s -replace '"',''
    $t = $t -replace '\s+',''
    $t = $t -replace '\\u00A0',''
    $t = $t -replace ',', '.'
    try { return [double]::Parse($t, [System.Globalization.CultureInfo]::InvariantCulture) } catch { return $null }
}

function ToInt($s) {
    if ($null -eq $s -or $s -eq '') { return 0 }
    $t = $s -replace '"',''
    try { return [int]::Parse($t) } catch { return 0 }
}

$rows = Import-Csv $aggPath | ForEach-Object {
    [pscustomobject]@{
        combo = $_.combo
        graph = $_.graph
        method = $_.method
        mean_mae = ParseFloat($_.mean_mae)
        median_mae = ParseFloat($_.median_mae)
        std_mae = ParseFloat($_.std_mae)
        datasets_count = ToInt($_.datasets_count)
        real_datasets_count = ToInt($_.real_datasets_count)
        real_obs_count = ToInt($_.real_obs_count)
        count = ToInt($_.count)
    }
}

# Per-graph summary
$perGraph = $rows | Group-Object graph | ForEach-Object {
    $g = $_.Name
    $list = $_.Group
    $mean_mean = ($list | Where-Object { $_.mean_mae -ne $null } | Measure-Object mean_mae -Average).Average
    $median_median = ($list | Where-Object { $_.median_mae -ne $null } | Measure-Object median_mae -Average).Average
    $mean_std = ($list | Where-Object { $_.std_mae -ne $null } | Measure-Object std_mae -Average).Average
    $countCombos = $list.Count
    $best_combo = $list | Where-Object { $_.mean_mae -ne $null } | Sort-Object mean_mae | Select-Object -First 1
    [pscustomobject]@{
        graph = $g
        combos = $countCombos
        mean_of_mean_mae = $mean_mean
        mean_of_median_mae = $median_median
        mean_of_std_mae = $mean_std
        best_combo = $best_combo.combo
        best_combo_mean = $best_combo.mean_mae
    }
}

# Per-method summary
$perMethod = $rows | Group-Object method | ForEach-Object {
    $m = $_.Name
    $list = $_.Group
    $mean_mean = ($list | Where-Object { $_.mean_mae -ne $null } | Measure-Object mean_mae -Average).Average
    $median_median = ($list | Where-Object { $_.median_mae -ne $null } | Measure-Object median_mae -Average).Average
    $mean_std = ($list | Where-Object { $_.std_mae -ne $null } | Measure-Object std_mae -Average).Average
    $countCombos = $list.Count
    $best_combo = $list | Where-Object { $_.mean_mae -ne $null } | Sort-Object mean_mae | Select-Object -First 1
    [pscustomobject]@{
        method = $m
        combos = $countCombos
        mean_of_mean_mae = $mean_mean
        mean_of_median_mae = $median_median
        mean_of_std_mae = $mean_std
        best_combo = $best_combo.combo
        best_combo_mean = $best_combo.mean_mae
    }
}

# Top combos overall
$top_by_mean = $rows | Where-Object { $_.mean_mae -ne $null } | Sort-Object mean_mae | Select-Object -First 10
$top_by_median = $rows | Where-Object { $_.median_mae -ne $null } | Sort-Object median_mae | Select-Object -First 10

# Differences: compute z-score between top N and rest for mean_mae
$mean_vals = $rows | Where-Object { $_.mean_mae -ne $null } | Select-Object -ExpandProperty mean_mae
$global_mean = ($mean_vals | Measure-Object -Average).Average
# compute standard deviation manually (sample std)
$global_std = $null
if ($mean_vals.Count -gt 1) {
    $sum = 0.0
    foreach ($v in $mean_vals) { $sum += ([double]$v - $global_mean) * ([double]$v - $global_mean) }
    $variance = $sum / ($mean_vals.Count - 1)
    $global_std = [math]::Sqrt($variance)
} else {
    $global_std = 0.0
}

$top10 = $top_by_mean
$top10_stats = $top10 | ForEach-Object {
    $z = if ($global_std -ne 0) { ($_.mean_mae - $global_mean)/$global_std } else { $null }
    [pscustomobject]@{ combo=$_.combo; mean_mae=$_.mean_mae; median_mae=$_.median_mae; z_score=$z; graph=$_.graph; method=$_.method }
}

# Export reports
$outdir = Join-Path $root 'selections_analysis'
if (-not (Test-Path $outdir)) { New-Item -ItemType Directory -Path $outdir | Out-Null }
$perGraph | Export-Csv -Path (Join-Path $outdir 'per_graph_summary.csv') -NoTypeInformation -Encoding UTF8
$perMethod | Export-Csv -Path (Join-Path $outdir 'per_method_summary.csv') -NoTypeInformation -Encoding UTF8
$top_by_mean | Export-Csv -Path (Join-Path $outdir 'top_by_mean.csv') -NoTypeInformation -Encoding UTF8
$top_by_median | Export-Csv -Path (Join-Path $outdir 'top_by_median.csv') -NoTypeInformation -Encoding UTF8
$top10_stats | Export-Csv -Path (Join-Path $outdir 'top10_stats.csv') -NoTypeInformation -Encoding UTF8

# Export JSON and a human-readable MD summary
$report = [ordered]@{
    per_graph = $perGraph
    per_method = $perMethod
    top_by_mean = $top_by_mean
    top_by_median = $top_by_median
    top10_stats = $top10_stats
    global_mean = $global_mean
    global_std = $global_std
}
$report | ConvertTo-Json -Depth 6 | Out-File -FilePath (Join-Path $outdir 'selections_analysis.json') -Encoding UTF8

$md = New-Object System.Text.StringBuilder
$md.AppendLine('# Selections analysis — per-graph, per-method, top combos') | Out-Null
$md.AppendLine('') | Out-Null
$md.AppendLine('## Global stats') | Out-Null
$md.AppendLine("- Global mean MAE: $([math]::Round($global_mean,6))") | Out-Null
$md.AppendLine("- Global std MAE: $([math]::Round($global_std,6))") | Out-Null
$md.AppendLine('') | Out-Null
$md.AppendLine('## Top 10 by mean MAE') | Out-Null
foreach ($t in $top_by_mean) { $md.AppendLine("- $($t.combo): mean=$([math]::Round($t.mean_mae,6)) median=$([math]::Round($t.median_mae,6)) graph=$($t.graph) method=$($t.method)") | Out-Null }
$md.AppendLine('') | Out-Null
$md.AppendLine('## Top 10 by median MAE') | Out-Null
foreach ($t in $top_by_median) { $md.AppendLine("- $($t.combo): median=$([math]::Round($t.median_mae,6)) mean=$([math]::Round($t.mean_mae,6)) graph=$($t.graph) method=$($t.method)") | Out-Null }
$md.AppendLine('') | Out-Null
$md.AppendLine('## Per-graph best combos (summary)') | Out-Null
foreach ($g in $perGraph) { $md.AppendLine("- $($g.graph): best_combo=$($g.best_combo) mean=$([math]::Round($g.best_combo_mean,6)) combos=$($g.combos)") | Out-Null }

$mdPath = Join-Path $outdir 'selections_analysis.md'
$md.ToString() | Out-File -FilePath $mdPath -Encoding UTF8

Write-Host "Wrote analysis to $outdir"

exit 0
