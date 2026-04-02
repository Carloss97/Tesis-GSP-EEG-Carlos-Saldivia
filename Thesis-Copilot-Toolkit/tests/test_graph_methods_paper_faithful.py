import unittest

import numpy as np

from src.data.data_loader import load_synthetic_eeg
from src.graph_construction.graph_constructors import build_graph


class TestGraphMethodsPaperFaithful(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_synthetic_eeg(n_channels=22, n_times=200, random_state=42)
        cls.signals = data["signals"]
        cls.positions = data["positions"]

    def _assert_valid_adjacency(self, adjacency: np.ndarray):
        self.assertEqual(adjacency.shape[0], adjacency.shape[1])
        self.assertTrue(np.isfinite(adjacency).all())
        self.assertTrue(np.all(adjacency >= -1e-12))
        self.assertTrue(np.allclose(adjacency, adjacency.T, atol=1e-8))
        self.assertTrue(np.allclose(np.diag(adjacency), 0.0, atol=1e-10))

    def test_nnk_adjacency_properties(self):
        graph = build_graph("nnk", self.positions, signals=self.signals, k=6, backend="internal", reg=1e-6)
        adjacency = graph["adjacency"]
        if hasattr(adjacency, "toarray"):
            adjacency = adjacency.toarray()

        self._assert_valid_adjacency(adjacency)
        self.assertGreater(float(np.sum(adjacency)), 0.0)

    def test_aew_adjacency_properties(self):
        graph = build_graph("aew", self.positions, signals=self.signals, k=5, sigma_dist=1.0, sigma_corr=0.5)
        adjacency = graph["adjacency"]
        if hasattr(adjacency, "toarray"):
            adjacency = adjacency.toarray()

        self._assert_valid_adjacency(adjacency)
        self.assertGreater(float(np.sum(adjacency)), 0.0)

    def test_aew_responds_to_signal_structure(self):
        graph_a = build_graph("aew", self.positions, signals=self.signals, k=5, sigma_dist=1.0, sigma_corr=0.5)
        shuffled = self.signals.copy()
        rng = np.random.default_rng(123)
        rng.shuffle(shuffled, axis=1)
        graph_b = build_graph("aew", self.positions, signals=shuffled, k=5, sigma_dist=1.0, sigma_corr=0.5)

        a = graph_a["adjacency"]
        b = graph_b["adjacency"]
        if hasattr(a, "toarray"):
            a = a.toarray()
        if hasattr(b, "toarray"):
            b = b.toarray()

        self.assertGreater(np.linalg.norm(a - b), 1e-9)


if __name__ == "__main__":
    unittest.main()
