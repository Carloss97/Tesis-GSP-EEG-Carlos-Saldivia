"""Utilities to convert MATLAB .mat outputs into NumPy `.npy` fixtures.

Usage:
    python matlab_to_npy.py --matdir path/to/mats --outdir tests/fixtures/eeg_nnk --vars F,G,adjacency

The converter saves each MATLAB variable as `<mat_basename>_<var>.npy`.
"""
from __future__ import annotations

import argparse
import glob
import os
from typing import Iterable, List, Optional

import numpy as np
from scipy.io import loadmat


def convert_mat_file(mat_path: str, out_dir: str, var_whitelist: Optional[Iterable[str]] = None, overwrite: bool = False) -> List[str]:
    os.makedirs(out_dir, exist_ok=True)
    data = loadmat(mat_path, squeeze_me=True, struct_as_record=False)
    base = os.path.splitext(os.path.basename(mat_path))[0]
    saved = []
    for k, v in data.items():
        if k.startswith("__"):
            continue
        if var_whitelist and k not in var_whitelist:
            continue
        arr = np.asarray(v)
        out_name = f"{base}_{k}.npy"
        out_path = os.path.join(out_dir, out_name)
        if not overwrite and os.path.exists(out_path):
            saved.append(out_path)
            continue
        np.save(out_path, arr)
        saved.append(out_path)
    return saved


def convert_mat_dir(mat_dir: str, out_dir: str, pattern: str = "*.mat", vars: Optional[Iterable[str]] = None, overwrite: bool = False) -> List[str]:
    mat_files = sorted(glob.glob(os.path.join(mat_dir, pattern)))
    all_saved = []
    for m in mat_files:
        saved = convert_mat_file(m, out_dir, var_whitelist=vars, overwrite=overwrite)
        all_saved.extend(saved)
    return all_saved


def _parse_vars(s: Optional[str]) -> Optional[List[str]]:
    if s is None:
        return None
    return [x.strip() for x in s.split(",") if x.strip()]


def main():
    parser = argparse.ArgumentParser(description="Convert MATLAB .mat files to NumPy .npy fixtures")
    parser.add_argument("--matdir", required=True, help="Directory containing .mat files")
    parser.add_argument("--outdir", required=True, help="Output directory for .npy files")
    parser.add_argument("--vars", help="Comma-separated list of variables to extract (default: all)")
    parser.add_argument("--pattern", default="*.mat", help="Glob pattern for mat files")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing .npy files")

    args = parser.parse_args()
    vars = _parse_vars(args.vars)
    saved = convert_mat_dir(args.matdir, args.outdir, pattern=args.pattern, vars=vars, overwrite=args.overwrite)
    print(f"Saved {len(saved)} numpy files to {args.outdir}")


if __name__ == "__main__":
    main()
