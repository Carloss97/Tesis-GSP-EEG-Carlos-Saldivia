$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$aggPath = Join-Path $root 'analysis_it05_it20_multicriteria_agg.csv'
$raw1 = Join-Path (Resolve-Path (Join-Path $root '..\results')).Path 'it05_all_datasets_raw.csv'
$raw2 = Join-Path (Resolve-Path (Join-Path $root '..\results')).Path 'it20_synthetic_alpha_high_missing_raw.csv'

if (-not (Test-Path $aggPath)) { Write-Error "Aggregation CSV not found: $aggPath"; exit 1 }

$agg = Import-Csv $aggPath

# load raw rows from available files
$rawAll = @()
if (Test-Path $raw1) { $rawAll += Import-Csv $raw1 }
if (Test-Path $raw2) { $rawAll += Import-Csv $raw2 }

function ParseFloat($s) {
    if ($null -eq $s -or $s -eq '') { return $null }
    $t = $s -replace '"',''
    $t = $t -replace '\s+',''
    $t = $t -replace '\\u00A0',''
    # normalize decimal comma to dot
    $t = $t -replace ',', '.'
    try { return [double]::Parse($t, [System.Globalization.CultureInfo]::InvariantCulture) } catch { return $null }
}

# compute numeric fields in agg
$rows = $agg | ForEach-Object {
    $mean = ParseFloat($_.mean_mae)
    $median = ParseFloat($_.median_mae)
    $std = ParseFloat($_.std_mae)
    $datasets_count = 0
    try { $datasets_count = [int]::Parse($_.datasets_count) } catch { $datasets_count = 0 }
    $real_obs_count = 0
    try { $real_obs_count = [int]::Parse($_.real_obs_count) } catch { $real_obs_count = 0 }
    [pscustomobject]@{
        graph = $_.graph
        method = $_.method
        combo = $_.combo
        mean_mae = $mean
        median_mae = $median
        std_mae = $std
        datasets_count = $datasets_count
        real_obs_count = $real_obs_count
    }
}

# FILTERS
$th_med = 0.05
$min_datasets = 3
$th_mean = 0.05
$min_real_obs = 3

$filter1 = $rows | Where-Object { ($null -ne $_.median_mae) -and ($_.median_mae -lt $th_med) -and ($_.datasets_count -ge $min_datasets) }
$filter2 = $rows | Where-Object { ($null -ne $_.mean_mae) -and ($_.mean_mae -lt $th_mean) -and ($_.real_obs_count -ge $min_real_obs) }

# helper to get top datasets for combo
function TopDatasets($combo, $k=5) {
    if ($rawAll.Count -eq 0) { return @() }
    $parts = $combo -split '\|'
    $g = $parts[0]; $m = $parts[1]
    $rows = $rawAll | Where-Object { $_.graph -eq $g -and $_.method -eq $m }
    $out = $rows | ForEach-Object {
        $mae = ParseFloat($_.mae)
        [pscustomobject]@{dataset=$_.dataset; mae=$mae; seed=$_.seed}
    } | Where-Object { $null -ne $_.mae } | Sort-Object mae | Select-Object -First $k
    return $out
}

# Export CSVs
$out1_csv = Join-Path $root 'filtered_threshold_median.csv'
$out2_csv = Join-Path $root 'filtered_mean_realobs.csv'

$filter1 | Select-Object combo,graph,method,median_mae,datasets_count | Export-Csv -Path $out1_csv -NoTypeInformation -Encoding UTF8
$filter2 | Select-Object combo,graph,method,mean_mae,real_obs_count | Export-Csv -Path $out2_csv -NoTypeInformation -Encoding UTF8

# Export JSON combined
$out_json = Join-Path $root 'filtered_selections.json'
$export = [ordered]@{ threshold_median = @(); mean_realobs = @() }
foreach ($r in $filter1) {
    $export.threshold_median += [pscustomobject]@{combo=$r.combo; graph=$r.graph; method=$r.method; median_mae=$r.median_mae; datasets_count=$r.datasets_count; top_datasets=(TopDatasets $r.combo)}
}
foreach ($r in $filter2) {
    $export.mean_realobs += [pscustomobject]@{combo=$r.combo; graph=$r.graph; method=$r.method; mean_mae=$r.mean_mae; real_obs_count=$r.real_obs_count; top_datasets=(TopDatasets $r.combo)}
}
$export | ConvertTo-Json -Depth 5 | Out-File -FilePath $out_json -Encoding UTF8

# Export compact markdown
$out_md = Join-Path $root 'filtered_selections_compact.md'
$sb = New-Object System.Text.StringBuilder
$sb.AppendLine('# Filtered selections (compact)') | Out-Null
$sb.AppendLine('') | Out-Null
$sb.AppendLine("## Filter A - median_mae < $th_med AND datasets_count >= $min_datasets") | Out-Null
if ($filter1.Count -eq 0) { $sb.AppendLine('No combos matched.') | Out-Null } else {
    foreach ($r in $filter1) {
        $sb.AppendLine("- $($r.combo): median=$([math]::Round($r.median_mae,6)) datasets=$($r.datasets_count)") | Out-Null
        $tops = TopDatasets $r.combo
        foreach ($t in $tops) { $sb.AppendLine("    - $($t.dataset): mae=$([math]::Round($t.mae,6)) (seed=$($t.seed))") | Out-Null }
    }
}
$sb.AppendLine('') | Out-Null
$sb.AppendLine("## Filter B - mean_mae < $th_mean AND real_obs_count >= $min_real_obs") | Out-Null
if ($filter2.Count -eq 0) { $sb.AppendLine('No combos matched.') | Out-Null } else {
    foreach ($r in $filter2) {
        $sb.AppendLine("- $($r.combo): mean=$([math]::Round($r.mean_mae,6)) real_obs=$($r.real_obs_count)") | Out-Null
        $tops = TopDatasets $r.combo
        foreach ($t in $tops) { $sb.AppendLine("    - $($t.dataset): mae=$([math]::Round($t.mae,6)) (seed=$($t.seed))") | Out-Null }
    }
}
$sb.ToString() | Out-File -FilePath $out_md -Encoding UTF8

Write-Host "Wrote: $out1_csv"
Write-Host "Wrote: $out2_csv"
Write-Host "Wrote: $out_json"
Write-Host "Wrote: $out_md"

exit 0
