import os
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

from ...src.commands.register import (
    build_register_message,
    create_register_authorization_url,
)
from ...src.services.oauth_state import parse_oauth_state


class RegisterCommandTests(unittest.TestCase):
    def test_build_register_message_includes_url_and_expiry(self) -> None:
        message = build_register_message("https://example.com/oauth")

        self.assertIn("https://example.com/oauth", message)
        self.assertIn("The link expires in 10 minutes.", message)

    def test_create_register_authorization_url_uses_discord_user_state(
        self,
    ) -> None:
        env = {
            "FT_CLIENT_ID": "client-id",
            "FT_CLIENT_SECRET": "client-secret",
            "FT_REDIRECT_URI": "http://localhost:8000/oauth/42/callback",
            "FT_SCOPES": "public",
            "FT_STATE_SECRET": "state-secret",
        }

        with patch.dict(os.environ, env, clear=False):
            url = create_register_authorization_url(98765)

        query = parse_qs(urlparse(url).query)
        self.assertEqual(query["client_id"], ["client-id"])
        self.assertEqual(query["redirect_uri"], [env["FT_REDIRECT_URI"]])
        parsed_state = parse_oauth_state(
            query["state"][0],
            secret=env["FT_STATE_SECRET"],
        )
        self.assertEqual(parsed_state.discord_user_id, 98765)


if __name__ == "__main__":
    unittest.main()
