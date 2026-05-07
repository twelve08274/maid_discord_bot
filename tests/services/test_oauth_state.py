import time
import unittest

from ...src.services.oauth_state import (
    OAuthStateError,
    create_oauth_state,
    parse_oauth_state,
)


class OAuthStateTests(unittest.TestCase):
    def test_create_and_parse_state(self) -> None:
        state = create_oauth_state(12345, secret="test-secret")

        parsed = parse_oauth_state(state, secret="test-secret")

        self.assertEqual(parsed.discord_user_id, 12345)
        self.assertLessEqual(parsed.issued_at, int(time.time()))
        self.assertTrue(parsed.nonce)

    def test_rejects_tampered_signature(self) -> None:
        state = create_oauth_state(12345, secret="test-secret")
        payload, signature = state.split(".", 1)
        tampered_state = f"{payload}x.{signature}"

        with self.assertRaises(OAuthStateError):
            parse_oauth_state(tampered_state, secret="test-secret")

    def test_rejects_expired_state(self) -> None:
        state = create_oauth_state(12345, secret="test-secret")

        with self.assertRaises(OAuthStateError):
            parse_oauth_state(state, secret="test-secret", max_age_seconds=-1)


if __name__ == "__main__":
    unittest.main()
