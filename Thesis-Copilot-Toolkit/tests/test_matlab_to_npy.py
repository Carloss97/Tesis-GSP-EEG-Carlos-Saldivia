import importlib.util
import os
import sys

import numpy as np
import scipy.io


def load_converter_module(root_path: str):
    module_path = os.path.join(root_path, "tools", "matlab_to_npy.py")
    spec = importlib.util.spec_from_file_location("matlab_to_npy", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_mat_to_npy_roundtrip(tmp_path):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if root not in sys.path:
        sys.path.insert(0, root)

    mod = load_converter_module(root)

    # create a synthetic .mat with expected variables
    mat_path = tmp_path / "example.mat"
    F = np.arange(12).reshape(3, 4)
    G = np.eye(4)
    adjacency = np.zeros((4, 4))
    recon = np.ones((3, 4))
    scipy.io.savemat(str(mat_path), {"F": F, "G": G, "adjacency": adjacency, "recon": recon})

    outdir = tmp_path / "out"
    outdir.mkdir()

    saved = mod.convert_mat_file(str(mat_path), str(outdir), var_whitelist=["F", "G", "adjacency", "recon"], overwrite=True)
    assert len(saved) == 4

    # verify saved arrays
    F2 = np.load(str(outdir / "example_F.npy"))
    G2 = np.load(str(outdir / "example_G.npy"))
    A2 = np.load(str(outdir / "example_adjacency.npy"))
    R2 = np.load(str(outdir / "example_recon.npy"))

    assert np.array_equal(F, F2)
    assert np.array_equal(G, G2)
    assert np.array_equal(adjacency, A2)
    assert np.array_equal(recon, R2)
