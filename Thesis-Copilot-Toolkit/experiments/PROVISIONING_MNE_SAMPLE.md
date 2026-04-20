# Provisioning the MNE "sample" dataset

Purpose
-------
This document explains how to provision the MNE `sample` dataset locally for
the experiments in this repository and how to integrate the provisioning step
in CI workflows.

Why
---
- The `sample` dataset is used by several iterations (e.g., `it17`) and is
  ~1.6GB compressed. Tests and experiments expect it available locally.
- This repository intentionally does not commit large datasets; use this
  provisioning step in your environment or CI.

Usage (local)
-------------
Run the helper script (recommended inside the `eegrasp` environment):

Windows PowerShell
```powershell
& "C:\Users\sarlo\anaconda3\envs\eegrasp\python.exe" "Thesis-Copilot-Toolkit\scripts\provision_mne_sample.py" --path "C:\path\to\repo\Thesis-Copilot-Toolkit\datasets\MNE-eegbci-data"
```

Linux / macOS
```bash
python3 Thesis-Copilot-Toolkit/scripts/provision_mne_sample.py --path /workdir/Thesis-Copilot-Toolkit/datasets/MNE-eegbci-data
```

Notes
-----
- The helper uses `mne.datasets.sample.data_path(...)` and will download the
  dataset automatically if missing. The download is ~1.6GB and will be
  extracted under the provided path.
- Do NOT commit the dataset. The `.gitignore` already excludes `datasets/`.

CI integration (GitHub Actions example)
-------------------------------------
Add a step that runs the provisioner before the test/experiment steps. Example:

```yaml
- name: Provision MNE sample dataset
  run: |
    python -m pip install --upgrade pip mne
    python Thesis-Copilot-Toolkit/scripts/provision_mne_sample.py --path "${{ runner.workspace }}/Thesis-Copilot-Toolkit/datasets/MNE-eegbci-data"
  env:
    MNE_DATA: ${{ runner.workspace }}/Thesis-Copilot-Toolkit/datasets
```

Troubleshooting
---------------
- If `sample_audvis_raw.fif` is not found after the script runs, check
  network access to OSF and confirm that `mne` can download files.
- To force a fresh download, re-run the script with `--force-update`.
- Manual download: see https://mne.tools/stable/overview/datasets_index.html#mne-sample-dataset

Follow-ups
---------
- Consider adding a CI cache for the dataset if your CI provider supports it.
- Decide whether to include a provisioning step in repository setup docs.
