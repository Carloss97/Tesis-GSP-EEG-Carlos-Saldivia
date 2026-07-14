import unittest

import numpy as np

from src.data.data_loader import load_bci_competition_iv_2a


class TestBCICompetitionIV2A(unittest.TestCase):
    def test_loader_uses_proxy_when_file_is_missing(self):
        data = load_bci_competition_iv_2a(subject=1)
        signals = data["signals"]
        positions = data["positions"]
        info = data["info"]

        self.assertEqual(signals.shape[1], 64)
        self.assertEqual(positions.shape[0], 64)
        self.assertTrue(np.isfinite(signals).all())
        self.assertTrue(info.get("proxy", False))
        self.assertEqual(info.get("dataset"), "bci_competition_iv_2a")


if __name__ == "__main__":
    unittest.main()