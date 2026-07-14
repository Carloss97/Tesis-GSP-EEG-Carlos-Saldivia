import os
import unittest

import numpy as np

from experiments.optimize_and_benchmark import (
    apply_scenario_mask,
    build_realistic_scenarios,
    run_benchmark,
)


class TestOptimizeBenchmarkB1(unittest.TestCase):
    def setUp(self):
        self._env_backup = dict(os.environ)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._env_backup)

    def test_scenarios_are_created_with_minimum_groups(self):
        angles = np.linspace(0.0, 2.0 * np.pi, 16, endpoint=False)
        positions = np.stack([np.cos(angles), np.sin(angles), np.zeros_like(angles)], axis=1)
        ch_names = [f"Ch{i + 1}" for i in range(16)]

        scenarios = build_realistic_scenarios(positions, ch_names)

        self.assertGreaterEqual(len(scenarios), 4)
        for scenario in scenarios:
            self.assertGreaterEqual(len(scenario["base_indices"]), 2)
            self.assertIn("region", scenario)
            self.assertIn("electrode_type", scenario)

    def test_apply_scenario_mask_respects_missing_ratio(self):
        signals = np.ones((20, 10), dtype=float)
        masked, selected = apply_scenario_mask(signals, base_indices=[0, 1, 2], missing_ratio=0.4, seed=42)

        self.assertEqual(len(selected), 4)
        self.assertTrue(np.isnan(masked[:, selected]).all())
        observed = [idx for idx in range(10) if idx not in selected]
        self.assertTrue(np.isfinite(masked[:, observed]).all())

    def test_run_benchmark_includes_dtw_and_protocol_config(self):
        os.environ["B1_GRAPH_NAMES"] = "knn"
        os.environ["B1_METHOD_NAMES"] = "linear"
        os.environ["B1_MAX_SCENARIOS"] = "1"

        df, config = run_benchmark(
            include_mne=False,
            max_time_samples=40,
            missing_levels=[0.1],
            random_seed=42,
        )

        self.assertFalse(df.empty)
        self.assertIn("dtw", df.columns)
        self.assertIn("missing_ratio", df.columns)
        self.assertIn("scenario", df.columns)
        self.assertIn("datasets", config)
        self.assertIn("synthetic", config["datasets"])
        self.assertEqual(config["missing_levels"], [0.1])


if __name__ == "__main__":
    unittest.main()
