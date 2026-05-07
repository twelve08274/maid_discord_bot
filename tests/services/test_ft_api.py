import unittest
from urllib.parse import parse_qs, urlparse

from ...src.config import FtOAuthConfig
from ...src.services.ft_api import (
    FT_AUTHORIZE_URL,
    create_authorization_url,
)


class FtApiTests(unittest.TestCase):
    def test_create_authorization_url_contains_expected_query(self) -> None:
        config = FtOAuthConfig(
            client_id="client-id",
            client_secret="client-secret",
            redirect_uri="http://localhost:8000/oauth/42/callback",
            scopes="public profile",
        )

        url = create_authorization_url("state-value", config=config)

        parsed = urlparse(url)
        self.assertEqual(
            f"{parsed.scheme}://{parsed.netloc}{parsed.path}",
            FT_AUTHORIZE_URL,
        )
        query = parse_qs(parsed.query)
        self.assertEqual(query["client_id"], ["client-id"])
        self.assertEqual(query["redirect_uri"], [config.redirect_uri])
        self.assertEqual(query["response_type"], ["code"])
        self.assertEqual(query["scope"], ["public profile"])
        self.assertEqual(query["state"], ["state-value"])


if __name__ == "__main__":
    unittest.main()
