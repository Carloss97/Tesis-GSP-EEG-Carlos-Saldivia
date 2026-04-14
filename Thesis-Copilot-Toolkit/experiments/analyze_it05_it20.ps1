$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$resultsDir = Resolve-Path (Join-Path $root '..\results')
$it05 = Import-Csv (Join-Path $resultsDir 'it05_all_datasets_raw.csv')
$it20 = Import-Csv (Join-Path $resultsDir 'it20_synthetic_alpha_high_missing_raw.csv')

# add combo column
$it05 = $it05 | ForEach-Object { $_ | Add-Member -NotePropertyName combo -NotePropertyValue ($_.graph + '|' + $_.method) -PassThru }
$it20 = $it20 | ForEach-Object { $_ | Add-Member -NotePropertyName combo -NotePropertyValue ($_.graph + '|' + $_.method) -PassThru }

function ToDoubleSafe([string]$s) {
    if ([string]::IsNullOrWhiteSpace($s)) { return $null }
    try { return [double]::Parse($s) } catch { return $null }
}
# Use invariant culture to parse floats with dot as decimal separator
function ToDoubleInvariant([string]$s) {
    if ([string]::IsNullOrWhiteSpace($s)) { return $null }
    try { return [double]::Parse($s, [System.Globalization.CultureInfo]::InvariantCulture) } catch { return $null }
}

$groups = $it05 | Group-Object -Property combo
$results = @()
foreach ($g in $groups) {
    $combo = $g.Name
    $parts = $combo -split '\|'
    $graph = $parts[0]
    $method = $parts[1]
    $maes = $g.Group | ForEach-Object { ToDoubleInvariant($_.mae) } | Where-Object { $_ -ne $null }
    $count = $maes.Count
    if ($count -eq 0) { $mean = $null; $std = $null } else {
        $mean = ($maes | Measure-Object -Average).Average
        $sumSq = ($maes | ForEach-Object { ($_ - $mean)*($_ - $mean) } | Measure-Object -Sum).Sum
        if ($count -gt 1) { $std = [math]::Sqrt($sumSq/($count-1)) } else { $std = 0 }
    }
    $datasets_count = ($g.Group | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count
    $results += [pscustomobject]@{
        graph = $graph
        method = $method
        combo = $combo
        mean_mae = $mean
        std_mae = $std
        count = $count
        datasets_count = $datasets_count
        rank_metric = if ($mean -ne $null) { $mean + 0.5 * ($std -as [double]) } else { $null }
    }
}

$out_csv = Join-Path $root 'analysis_it05_agg.csv'
$results | Sort-Object rank_metric | Export-Csv -Path $out_csv -NoTypeInformation

# classification
$temporalTokens = @('temporal','tv','wavelet','time','trss','directed_tv','heat_diffusion','graph_time')
function IsTemporal($m) { $mm = $m.ToLower(); foreach ($t in $temporalTokens) { if ($mm -like "*$t*") { return $true } }; return $false }

$baselineMethods = @('mean','nearest','linear')

$min_datasets_for_generalist = [math]::Max(3, [int]([Math]::Round(($it05 | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count * 0.1)))

$generalists = $results | Where-Object { $_.datasets_count -ge $min_datasets_for_generalist -and $_.mean_mae -ne $null } | Sort-Object rank_metric
$top3_generalists = $generalists | Select-Object -First 3

$temporal_candidates = $results | Where-Object { IsTemporal($_.method) -and $_.mean_mae -ne $null -and $_.count -gt 0 } | Sort-Object rank_metric
$top3_temporal = $temporal_candidates | Select-Object -First 3

$instant_candidates = $results | Where-Object { -not (IsTemporal($_.method)) -and $_.mean_mae -ne $null } | Sort-Object rank_metric
$top3_instant = $instant_candidates | Select-Object -First 3

# Baselines summary
$baselines = @()
foreach ($bm in $baselineMethods) {
    $rows = $results | Where-Object { $_.method -eq $bm -and $_.mean_mae -ne $null } | Sort-Object mean_mae
    if ($rows.Count -gt 0) {
        $best = $rows[0]
        $baselines += [pscustomobject]@{method=$bm; mean_mae=$best.mean_mae; best_graph=$best.graph}
    } else {
        $baselines += [pscustomobject]@{method=$bm; mean_mae=$null; best_graph=$null}
    }
}

# helper to get top datasets per combo (lowest mae)
function TopDatasetsForCombo($combo, $topk=5) {
    $rows = $it05 | Where-Object { $_.combo -eq $combo }
    $list = @()
    foreach ($r in $rows) {
        $m = ToDoubleInvariant($r.mae)
        if ($m -ne $null -and $m -lt 10) { $list += [pscustomobject]@{dataset=$r.dataset; mae=$m} }
    }
    $list = $list | Sort-Object mae | Select-Object -First $topk
    return $list
}

# build recommendations object
$recs = [ordered]@{}
$recs.generalists = @()
foreach ($r in $top3_generalists) {
    $recs.generalists += [pscustomobject]@{graph=$r.graph; method=$r.method; mean_mae=$r.mean_mae; std_mae=$r.std_mae; datasets_count=$r.datasets_count; top_datasets=(TopDatasetsForCombo $r.combo)}
}

$recs.temporal = @()
foreach ($r in $top3_temporal) {
    $recs.temporal += [pscustomobject]@{graph=$r.graph; method=$r.method; mean_mae=$r.mean_mae; std_mae=$r.std_mae; datasets_count=$r.datasets_count; top_datasets=(TopDatasetsForCombo $r.combo)}
}

$recs.instant = @()
foreach ($r in $top3_instant) {
    $recs.instant += [pscustomobject]@{graph=$r.graph; method=$r.method; mean_mae=$r.mean_mae; std_mae=$r.std_mae; datasets_count=$r.datasets_count; top_datasets=(TopDatasetsForCombo $r.combo)}
}

$recs.baselines = $baselines

# Write outputs
$out_json = Join-Path $root 'analysis_it05_it20_recommendations.json'
$out_report = Join-Path $root 'analysis_it05_it20_report.txt'
$recs | ConvertTo-Json -Depth 5 | Out-File -FilePath $out_json -Encoding utf8

# human readable
$sb = New-Object System.Text.StringBuilder
$sb.AppendLine('Analysis IT05 (aggregated) — Top candidates') | Out-Null
$sb.AppendLine('') | Out-Null
$sb.AppendLine('Top 3 generalists:') | Out-Null
foreach ($r in $recs.generalists) {
    $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
    foreach ($d in $r.top_datasets) { $sb.AppendLine("    - $($d.dataset): mae=$([math]::Round($d.mae,4))") | Out-Null }
}

$sb.AppendLine('') | Out-Null
$sb.AppendLine('Top 3 temporal:') | Out-Null
foreach ($r in $recs.temporal) {
    $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
    foreach ($d in $r.top_datasets) { $sb.AppendLine("    - $($d.dataset): mae=$([math]::Round($d.mae,4))") | Out-Null }
}

$sb.AppendLine('') | Out-Null
$sb.AppendLine('Top 3 instant:') | Out-Null
foreach ($r in $recs.instant) {
    $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
    foreach ($d in $r.top_datasets) { $sb.AppendLine("    - $($d.dataset): mae=$([math]::Round($d.mae,4))") | Out-Null }
}

$sb.AppendLine('') | Out-Null
$sb.AppendLine('Baselines (best graph per method):') | Out-Null
foreach ($b in $recs.baselines) { $sb.AppendLine("- method=$($b.method): best_graph=$($b.best_graph) mean_mae=$([math]::Round($b.mean_mae,4))") | Out-Null }

$sb.ToString() | Out-File -FilePath $out_report -Encoding utf8

Write-Host "Wrote: $out_csv"
Write-Host "Wrote: $out_json"
Write-Host "Wrote: $out_report"