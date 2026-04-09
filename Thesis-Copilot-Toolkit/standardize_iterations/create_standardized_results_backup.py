#!/usr/bin/env python3
import tarfile
from pathlib import Path

root = Path('Thesis-Copilot-Toolkit') / 'standardized_results'
dest = Path('Thesis-Copilot-Toolkit') / 'standardize_iterations' / 'standardized_results_backup.tar.gz'

dest.parent.mkdir(parents=True, exist_ok=True)

with tarfile.open(dest, 'w:gz', format=tarfile.PAX_FORMAT) as tar:
    tar.add(str(root), arcname='standardized_results')

print(str(dest))
