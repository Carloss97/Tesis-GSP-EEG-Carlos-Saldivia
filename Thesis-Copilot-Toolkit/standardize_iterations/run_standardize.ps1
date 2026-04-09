param(
    [string]$SourceRoot = ".",
    [string]$TargetRoot = "Thesis-Copilot-Toolkit/standardized_results",
    [int]$Min = 1,
    [int]$Max = 130,
    [switch]$DryRun
)

$python = "python"
$script = "Thesis-Copilot-Toolkit\standardize_iterations\standardize_results.py"
$args = @("--source-root", $SourceRoot, "--target-root", $TargetRoot, "--min", $Min, "--max", $Max)
if ($DryRun) { $args += "--dry-run" } else { $args += "--yes" }

Write-Host "Ejecutando estandarización: $python $script $($args -join ' ')"
& $python $script @args
