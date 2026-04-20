#!/usr/bin/env python3
"""
Provision helper for the MNE 'sample' dataset used by the experiments.

This script downloads the MNE sample dataset into a project-local folder
and verifies the presence of `sample_audvis_raw.fif`. It is idempotent and
prints a small CI snippet that can be used in GitHub Actions or similar.

Usage examples:
  python provision_mne_sample.py --path /abs/path/to/Thesis-Copilot-Toolkit/datasets/MNE-eegbci-data
  python provision_mne_sample.py --force-update

Notes:
 - Do NOT commit the downloaded dataset to git. The repository's .gitignore
   already excludes heavy datasets.
 - The script uses `mne.datasets.sample.data_path(...)` under the hood.
"""
from __future__ import annotations

import argparse
import os
import sys
import textwrap
from pathlib import Path

try:
    import mne
except Exception:  # pragma: no cover - runtime environment
    print("ERROR: mne is required. Activate the 'eegrasp' env or install mne.", file=sys.stderr)
    raise


def find_sample_file(root: Path) -> Path | None:
    for p in root.rglob("sample_audvis_raw.fif"):
        return p
    return None


def ci_snippet(path: str) -> str:
    snippet = textwrap.dedent(f"""
    # CI snippet: provision MNE sample dataset
    - name: Provision MNE sample dataset
      run: |
        python -m pip install --upgrade pip mne
        python {Path(__file__).as_posix()} --path "{path}"
      env:
        MNE_DATA: ${{{{ runner.workspace }}}}/Thesis-Copilot-Toolkit/datasets
    """)
    return snippet


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Provision the MNE sample dataset for experiments")
    repo_default = Path(__file__).resolve().parents[1] / "datasets" / "MNE-eegbci-data"
    p.add_argument("--path", default=str(repo_default), help=f"Target base path (default: {repo_default})")
    p.add_argument("--force-update", action="store_true", help="Force update/download even when present")
    p.add_argument("--update-config", action="store_true", help="Set MNE config path to the chosen path")
    p.add_argument("--ci-snippet", action="store_true", help="Print a CI snippet for provisioning")
    args = p.parse_args(argv)

    target = Path(args.path).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    print("Target base path:", target)

    try:
        print("Calling mne.datasets.sample.data_path(...) — this may download ~1.6GB")
        data_path = mne.datasets.sample.data_path(path=str(target), force_update=args.force_update, download=True, update_path=args.update_config)
        data_path = Path(data_path)
        print("mne data_path returned:", data_path)
    except Exception as exc:
        print("ERROR: failed to obtain MNE sample dataset:", exc, file=sys.stderr)
        return 2

    # Robust search for the file, because different mne versions may return
    # slightly different folder layouts (we've seen an extra nested 'MNE-sample-data').
    sample_file = find_sample_file(data_path) or find_sample_file(target)
    if sample_file:
        size_mb = sample_file.stat().st_size / 1024 / 1024
        print(f"Found sample file: {sample_file} ({size_mb:.1f} MB)")
        print("Provisioning OK. Do not commit this file to git; keep datasets in .gitignore.")
    else:
        print("ERROR: sample_audvis_raw.fif not found under:", data_path, file=sys.stderr)
        print("Search attempted under:", target, file=sys.stderr)
        print("If automatic download failed, follow manual instructions in the README.")
        return 3

    if args.ci_snippet:
        print("\nCI snippet to add in your workflow:\n")
        print(ci_snippet(str(target)))

    print("To persist the location for other code, set the environment variable: MNE_DATA=<path-to-datasets>")
    print("Example (Windows PowerShell):")
    print(f"  setx MNE_DATA \"{target}\"")
    print("Example (Linux/macOS):")
    print(f"  export MNE_DATA=\"{target}\"")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
