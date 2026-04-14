$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$resultsDir = (Resolve-Path (Join-Path $root '..\results')).Path

# Input files (it05 + it20)
$f1 = Join-Path $resultsDir 'it05_all_datasets_raw.csv'
$f2 = Join-Path $resultsDir 'it20_synthetic_alpha_high_missing_raw.csv'
$files = @($f1, $f2) | Where-Object { Test-Path $_ }

if ($files.Count -eq 0) { Write-Error "No input CSVs found in $resultsDir"; exit 1 }

$all = @()
foreach ($f in $files) { $all += Import-Csv $f }
$all = $all | ForEach-Object { $_ | Add-Member -NotePropertyName combo -NotePropertyValue ($_.graph + '|' + $_.method) -PassThru }

function ToDoubleInvariant([string]$s) {
    if ([string]::IsNullOrWhiteSpace($s)) { return $null }
    try { return [double]::Parse($s, [System.Globalization.CultureInfo]::InvariantCulture) } catch { return $null }
}

function MedianValue([double[]]$arr) {
    if (-not $arr -or $arr.Count -eq 0) { return $null }
    $sorted = $arr | Sort-Object
    $n = $sorted.Count
    $mid = [int]([math]::Floor($n / 2))
    if ($n % 2 -eq 1) {
        return $sorted[$mid]
    } else {
        $a = $sorted[$mid - 1]
        $b = $sorted[$mid]
        return (($a + $b) / 2)
    }
}

# Build aggregated metrics across both it05 + it20
$uniqueDatasetsCount = ($all | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count
$groups = $all | Group-Object -Property combo
$results = @()
foreach ($g in $groups) {
    $combo = $g.Name
    $parts = $combo -split '\|'
    $graph = $parts[0]
    $method = $parts[1]
    $maes = $g.Group | ForEach-Object { ToDoubleInvariant($_.mae) } | Where-Object { $_ -ne $null }
    $count = $maes.Count
    if ($count -gt 0) {
        $mean = ($maes | Measure-Object -Average).Average
        $median = MedianValue $maes
        $sumSq = ($maes | ForEach-Object { ($_ - $mean)*($_ - $mean) } | Measure-Object -Sum).Sum
        if ($count -gt 1) { $std = [math]::Sqrt($sumSq/($count-1)) } else { $std = 0 }
        $min = ($maes | Measure-Object -Minimum).Minimum
        $max = ($maes | Measure-Object -Maximum).Maximum
        $cv = if ($mean -ne 0) { $std / $mean } else { $null }
    } else {
        $mean = $null; $median = $null; $std = $null; $min = $null; $max = $null; $cv = $null
    }
    $datasets_count = ($g.Group | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count
    $real_count = ($g.Group | Where-Object { -not ($_.dataset -like 'synthetic*') } | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count
    $real_obs_count = ($g.Group | Where-Object { -not ($_.dataset -like 'synthetic*') } | ForEach-Object { ToDoubleInvariant($_.mae) } | Where-Object { $_ -ne $null }).Count

    $results += [pscustomobject]@{
        graph = $graph
        method = $method
        combo = $combo
        mean_mae = $mean
        median_mae = $median
        std_mae = $std
        min_mae = $min
        max_mae = $max
        cv_mae = $cv
        count = $count
        datasets_count = $datasets_count
        real_datasets_count = $real_count
        real_obs_count = $real_obs_count
        rank_metric_mean = if ($null -ne $mean) { $mean + 0.5 * ($std -as [double]) } else { $null }
        rank_metric_median = $median
        rank_metric_stability = if ($null -ne $mean) { $mean + $std } else { $null }
        rank_metric_cv = $cv
    }
}

$out_csv = Join-Path $root 'analysis_it05_it20_multicriteria_agg.csv'
$results | Sort-Object rank_metric_mean | Export-Csv -Path $out_csv -NoTypeInformation -Encoding UTF8

# classification helpers
$temporalTokens = @('temporal','tv','wavelet','time','trss','directed_tv','heat_diffusion','spline')
function IsTemporal($m) { $mm = $m.ToLower(); foreach ($t in $temporalTokens) { if ($mm -like "*$t*") { return $true } }; return $false }

$baselineMethods = @('mean','nearest','linear')
$min_datasets_for_generalist = [math]::Max(3, [int]([Math]::Round($uniqueDatasetsCount * 0.1)))

function TopDatasetsForCombo($combo, $topk=5) {
    $rows = $all | Where-Object { $_.combo -eq $combo }
    $list = @()
    foreach ($r in $rows) {
        $m = ToDoubleInvariant($r.mae)
        if ($null -ne $m) { $list += [pscustomobject]@{dataset=$r.dataset; mae=$m} }
    }
    $list = $list | Sort-Object mae | Select-Object -First $topk
    return $list
}

# Helper: select top candidates given a results table and a metric name
function SelectTop($table, $metric, $minDatasets) {
    $gen = $table | Where-Object { $_.datasets_count -ge $minDatasets -and ($null -ne $_.$metric) } | Sort-Object -Property $metric | Select-Object -First 3
    $temp = $table | Where-Object { IsTemporal($_.method) -and ($null -ne $_.$metric) -and $_.count -gt 0 } | Sort-Object -Property $metric | Select-Object -First 3
    $inst = $table | Where-Object { -not (IsTemporal($_.method)) -and ($null -ne $_.$metric) -and $_.count -gt 0 } | Sort-Object -Property $metric | Select-Object -First 3

    $baselines = @()
    foreach ($bm in $baselineMethods) {
        $rows = $table | Where-Object { $_.method -eq $bm -and ($null -ne $_.$metric) } | Sort-Object -Property $metric
        if ($rows.Count -gt 0) { $best = $rows[0]; $baselines += [pscustomobject]@{method=$bm; mean_mae=$best.mean_mae; best_graph=$best.graph} }
        else { $baselines += [pscustomobject]@{method=$bm; mean_mae=$null; best_graph=$null} }
    }

    return [pscustomobject]@{generalists=$gen; temporal=$temp; instant=$inst; baselines=$baselines}
}

# CRITERIA
$report = [ordered]@{}

# 1) Original mean-based ranking (mean + 0.5*std) on full results
$report.mean_based = SelectTop $results 'rank_metric_mean' $min_datasets_for_generalist

# 2) Real-only: recompute aggregations using only non-synthetic datasets
$allReal = $all | Where-Object { -not ($_.dataset -like 'synthetic*') }
$groupsReal = $allReal | Group-Object -Property combo
$resultsReal = @()
foreach ($g in $groupsReal) {
    $combo = $g.Name; $parts = $combo -split '\|'; $graph = $parts[0]; $method = $parts[1]
    $maes = $g.Group | ForEach-Object { ToDoubleInvariant($_.mae) } | Where-Object { $_ -ne $null }
    $count = $maes.Count
    if ($count -gt 0) {
        $mean = ($maes | Measure-Object -Average).Average
        $median = MedianValue $maes
        $sumSq = ($maes | ForEach-Object { ($_ - $mean)*($_ - $mean) } | Measure-Object -Sum).Sum
        if ($count -gt 1) { $std = [math]::Sqrt($sumSq/($count-1)) } else { $std = 0 }
        $min = ($maes | Measure-Object -Minimum).Minimum
        $max = ($maes | Measure-Object -Maximum).Maximum
        $cv = if ($mean -ne 0) { $std / $mean } else { $null }
    } else { $mean=$null; $median=$null; $std=$null; $min=$null; $max=$null; $cv=$null }
    $datasets_count = ($g.Group | Select-Object -ExpandProperty dataset | Select-Object -Unique).Count
    $resultsReal += [pscustomobject]@{
        graph=$graph; method=$method; combo=$combo; mean_mae=$mean; median_mae=$median; std_mae=$std; min_mae=$min; max_mae=$max; cv_mae=$cv; count=$count; datasets_count=$datasets_count; rank_metric_mean=if($mean -ne $null){$mean + 0.5*$std}else{$null}
    }
}
$report.real_only_mean = SelectTop $resultsReal 'rank_metric_mean' $min_datasets_for_generalist

# 3) Median-based ranking (robust against outliers) on full results
$report.median_based = SelectTop $results 'rank_metric_median' $min_datasets_for_generalist

# 4) Stability-first: prioritize low mean+std (robustness)
$report.stability_first = SelectTop $results 'rank_metric_stability' $min_datasets_for_generalist

# Write JSON and MD outputs
$out_json = Join-Path $root 'analysis_it05_it20_multicriteria_recommendations.json'
$out_md = Join-Path $root 'analysis_it05_it20_multicriteria.md'
$report | ConvertTo-Json -Depth 6 | Out-File -FilePath $out_json -Encoding UTF8

# write human-readable markdown
$sb = New-Object System.Text.StringBuilder
$sb.AppendLine('# Multicriteria analysis — IT05 + IT20') | Out-Null
$sb.AppendLine("Generated: $(Get-Date -Format s)") | Out-Null
$sb.AppendLine('') | Out-Null
$sb.AppendLine('## Criteria evaluated') | Out-Null
$sb.AppendLine('- mean_based: ranking by mean MAE (mean + 0.5*std) on all data') | Out-Null
$sb.AppendLine('- real_only_mean: same as mean_based but computed only on non-synthetic datasets') | Out-Null
$sb.AppendLine('- median_based: ranking by median MAE (robust)') | Out-Null
$sb.AppendLine('- stability_first: ranking by mean+std (penalize high variance)') | Out-Null
$sb.AppendLine('') | Out-Null

function DumpSection($name,$obj) {
    $sb.AppendLine("### $name") | Out-Null
    $sb.AppendLine('') | Out-Null
    $sb.AppendLine('**Top 3 generalists**') | Out-Null
    foreach ($r in $obj.generalists) {
        $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std_mae=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
        foreach ($d in (TopDatasetsForCombo $($r.combo))) { $sb.AppendLine("    - $($d.dataset): mae=$([math]::Round($d.mae,6))") | Out-Null }
    }
    $sb.AppendLine('') | Out-Null
    $sb.AppendLine('**Top 3 temporal**') | Out-Null
    foreach ($r in $obj.temporal) {
        $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std_mae=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
    }
    $sb.AppendLine('') | Out-Null
    $sb.AppendLine('**Top 3 instant**') | Out-Null
    foreach ($r in $obj.instant) {
        $sb.AppendLine("- $($r.graph) | $($r.method): mean_mae=$([math]::Round($r.mean_mae,4)) std_mae=$([math]::Round($r.std_mae,4)) datasets=$($r.datasets_count)") | Out-Null
    }
    $sb.AppendLine('') | Out-Null
    $sb.AppendLine('**Baselines**') | Out-Null
    foreach ($b in $obj.baselines) { $sb.AppendLine("- method=$($b.method): best_graph=$($b.best_graph) mean_mae=$([math]::Round($b.mean_mae,4))") | Out-Null }
    $sb.AppendLine('') | Out-Null
}

DumpSection 'Mean-based (full)' $report.mean_based
DumpSection 'Real-only mean' $report.real_only_mean
DumpSection 'Median-based (robust)' $report.median_based
DumpSection 'Stability-first' $report.stability_first

$sb.ToString() | Out-File -FilePath $out_md -Encoding UTF8

Write-Host "Wrote: $out_csv"
Write-Host "Wrote: $out_json"
Write-Host "Wrote: $out_md"

exit 0
