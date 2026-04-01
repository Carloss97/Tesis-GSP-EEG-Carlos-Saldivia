import unittest

import numpy as np

from src.data.data_loader import load_synthetic_eeg, simulate_missing_channels
from src.graph_construction.graph_constructors import build_graph
from src.interpolation_methods import interpolate_signals


class TestPaperFaithfulMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_synthetic_eeg(n_channels=16, n_times=180, random_state=42)
        cls.signals = data["signals"]
        cls.positions = data["positions"]
        graph = build_graph("knng", cls.positions, signals=cls.signals, k=5, sigma=1.0)
        cls.adjacency = graph["adjacency"]
        if hasattr(cls.adjacency, "toarray"):
            cls.adjacency = cls.adjacency.toarray()

    def test_bgsrp_runs_and_returns_finite(self):
        masked = simulate_missing_channels(self.signals, missing_ratio=0.2, random_state=7)
        rec = interpolate_signals("bgsrp", masked, adjacency=self.adjacency, bandwidth=6, gamma=0.1)
        x = rec["reconstructed"]
        self.assertEqual(x.shape, self.signals.shape)
        self.assertTrue(np.isfinite(x).all())

    def test_bgsrp_gamma_changes_solution(self):
        masked = simulate_missing_channels(self.signals, missing_ratio=0.2, random_state=13)
        x1 = interpolate_signals("bgsrp", masked, adjacency=self.adjacency, bandwidth=6, gamma=0.05)["reconstructed"]
        x2 = interpolate_signals("bgsrp", masked, adjacency=self.adjacency, bandwidth=6, gamma=0.5)["reconstructed"]
        self.assertGreater(np.linalg.norm(x1 - x2), 1e-9)

    def test_trss_preserves_observed_entries(self):
        masked = simulate_missing_channels(self.signals, missing_ratio=0.2, random_state=21)
        observed = ~np.isnan(masked)
        rec = interpolate_signals("trss", masked, adjacency=self.adjacency, alpha=0.8, beta=0.15, n_iter=80, lr=0.05)
        x = rec["reconstructed"]
        self.assertTrue(np.allclose(x[observed], masked[observed], atol=1e-8))

    def test_sobolev_temporal_alias_matches_trss(self):
        masked = simulate_missing_channels(self.signals, missing_ratio=0.2, random_state=42)
        params = {"alpha": 0.7, "beta": 0.2, "n_iter": 60, "lr": 0.04}
        x_trss = interpolate_signals("trss", masked, adjacency=self.adjacency, **params)["reconstructed"]
        x_sob = interpolate_signals("sobolev_temporal", masked, adjacency=self.adjacency, **params)["reconstructed"]
        self.assertTrue(np.allclose(x_trss, x_sob, atol=1e-10))


if __name__ == "__main__":
    unittest.main()
