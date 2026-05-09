import os
import unittest
from unittest.mock import patch

from src.config import (
    ConfigError,
    get_campus_now_cache_seconds,
    get_campus_now_campus_id,
    get_campus_now_pc_count,
    get_debug_mode,
)


class ConfigTests(unittest.TestCase):
    def test_debug_mode_is_enabled_by_true(self) -> None:
        with patch.dict(os.environ, {"DEBUG": "true"}, clear=False):
            self.assertTrue(get_debug_mode())

    def test_debug_mode_is_disabled_by_default(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(get_debug_mode())

    def test_campus_now_defaults(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(get_campus_now_campus_id(), "26")
            self.assertEqual(get_campus_now_pc_count(), 300)
            self.assertEqual(get_campus_now_cache_seconds(), 60)

    def test_campus_now_pc_count_must_be_positive(self) -> None:
        with patch.dict(os.environ, {"CAMPUS_NOW_PC_COUNT": "0"}, clear=True):
            with self.assertRaises(ConfigError):
                get_campus_now_pc_count()


if __name__ == "__main__":
    unittest.main()
