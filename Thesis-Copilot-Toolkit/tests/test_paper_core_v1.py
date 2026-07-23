from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from experiments.run_paper_core_v1 import (  # noqa: E402
    apply_channel_mask,
    assert_no_duplicate_rows,
    count_expected_cases,
    evaluate_hidden_channels,
    hierarchical_bootstrap_ci,
    make_bad_indices,
    mask_digest,
    select_bci_eeg_names,
)


class PaperCoreV1Tests(unittest.TestCase):
    def setUp(self) -> None:
        config_path = ROOT / "paper" / "bspc" / "evidence" / "paper_core_v1" / "config.json"
        self.config = json.loads(config_path.read_text(encoding="utf-8"))
        self.signals = np.arange(20 * 10, dtype=float).reshape(20, 10)
        theta = np.linspace(0.0, 2.0 * np.pi, 10, endpoint=False)
        self.positions = np.column_stack([np.cos(theta), np.sin(theta), np.ones(10)])

    def test_expected_case_count_is_760(self) -> None:
        counts = count_expected_cases(self.config)
        self.assertEqual(counts["recording_units"], 19)
        self.assertEqual(counts["paired_cases"], 760)
        self.assertEqual(counts["method_evaluations"], 1520)

    def test_mask_is_deterministic_and_method_independent(self) -> None:
        first = make_bad_indices(self.positions, severity=0.3, mode="nearby", seed=4)
        second = make_bad_indices(self.positions, severity=0.3, mode="nearby", seed=4)
        self.assertTrue(np.array_equal(first, second))
        self.assertEqual(mask_digest(first), mask_digest(second))
        self.assertEqual(mask_digest(first), hashlib.sha256(first.astype("<i8").tobytes()).hexdigest())

    def test_bci_eog_channels_are_excluded_explicitly(self) -> None:
        names = [f"EEG-{i}" for i in range(22)] + ["EOG-left", "EOG-central", "EOG-right"]
        selected = select_bci_eeg_names(names, expected_count=22)
        self.assertEqual(selected, names[:22])
        self.assertFalse(any("EOG" in name.upper() for name in selected))

    def test_metrics_use_hidden_channels_only(self) -> None:
        t = np.linspace(0.0, 1.0, 160, endpoint=False)
        clean = np.column_stack([np.sin(2 * np.pi * (frequency + 1) * t) for frequency in range(4)])
        reconstructed = clean.copy()
        reconstructed[:, 0] = clean[:, 0] + 2.0
        reconstructed[:, 1:] = 1e6
        metrics = evaluate_hidden_channels(clean, reconstructed, np.array([0]), sfreq=160.0)
        self.assertAlmostEqual(metrics["mae"], 2.0)
        self.assertAlmostEqual(metrics["rmse"], 2.0)

    def test_masking_and_reconstruction_preserve_observed_channels(self) -> None:
        bad = np.array([1, 7])
        masked = apply_channel_mask(self.signals, bad)
        reconstructed = np.nan_to_num(masked, nan=-3.0)
        observed = np.ones(self.signals.shape[1], dtype=bool)
        observed[bad] = False
        self.assertTrue(np.isnan(masked[:, bad]).all())
        self.assertTrue(np.array_equal(reconstructed[:, observed], self.signals[:, observed]))

    def test_duplicate_rows_are_rejected(self) -> None:
        frame = pd.DataFrame({"row_id": ["a", "a"], "case_id": ["c", "c"], "method": ["mne", "mne"]})
        with self.assertRaises(ValueError):
            assert_no_duplicate_rows(frame)

    def test_hierarchical_bootstrap_is_deterministic_and_bounded(self) -> None:
        frame = pd.DataFrame({
            "dataset": ["a", "a", "a", "a", "b", "b", "b", "b"],
            "recording_id": ["a1", "a1", "a2", "a2", "b1", "b1", "b2", "b2"],
            "mae_relative_advantage": [-0.4, -0.2, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8],
        })
        first = hierarchical_bootstrap_ci(frame, "mae_relative_advantage", 250, 123, overall=True)
        second = hierarchical_bootstrap_ci(frame, "mae_relative_advantage", 250, 123, overall=True)
        self.assertEqual(first, second)
        self.assertGreaterEqual(first[0], frame["mae_relative_advantage"].min())
        self.assertLessEqual(first[1], frame["mae_relative_advantage"].max())


if __name__ == "__main__":
    unittest.main()
