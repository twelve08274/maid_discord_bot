import os
import unittest
from unittest.mock import patch

from src.config import get_debug_mode


class ConfigTests(unittest.TestCase):
    def test_debug_mode_is_enabled_by_true(self) -> None:
        with patch.dict(os.environ, {"DEBUG": "true"}, clear=False):
            self.assertTrue(get_debug_mode())

    def test_debug_mode_is_disabled_by_default(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(get_debug_mode())


if __name__ == "__main__":
    unittest.main()
