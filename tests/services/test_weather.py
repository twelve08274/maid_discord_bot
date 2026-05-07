import sys
import unittest
from pathlib import Path

import httpx


sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from maid_discord_bot.services.weather import (  # noqa: E402
    WeatherApiKeyUnauthorizedError,
    WeatherLocationNotFoundError,
    WeatherServiceError,
    build_weather_comment,
    fetch_current_weather,
    parse_openweather_response,
)


class WeatherServiceTests(unittest.IsolatedAsyncioTestCase):
    def test_parse_openweather_response_returns_display_fields(self) -> None:
        report = parse_openweather_response(
            {
                "name": "Tokyo",
                "weather": [{"main": "Clear", "description": "晴天"}],
                "main": {
                    "temp": 22.4,
                    "feels_like": 21.8,
                    "humidity": 55,
                },
                "wind": {"speed": 3.2},
            }
        )

        self.assertEqual(report.location_name, "Tokyo")
        self.assertEqual(report.weather, "晴天")
        self.assertEqual(report.temperature_celsius, 22.4)
        self.assertEqual(report.feels_like_celsius, 21.8)
        self.assertEqual(report.humidity_percent, 55)
        self.assertEqual(report.wind_speed_mps, 3.2)

    def test_parse_openweather_response_rejects_incomplete_payload(self) -> None:
        with self.assertRaises(WeatherServiceError):
            parse_openweather_response({"name": "Tokyo"})

    def test_build_weather_comment_for_rain(self) -> None:
        self.assertEqual(
            build_weather_comment("light rain", 20),
            "雨具を持ってお出かけください。",
        )

    def test_build_weather_comment_for_japanese_clear_weather(self) -> None:
        self.assertEqual(
            build_weather_comment("晴天", 20),
            "よい天気です。気持ちよく過ごせそうです。",
        )

    async def test_fetch_current_weather_uses_openweather_parameters(self) -> None:
        seen_params = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen_params.update(dict(request.url.params))
            return httpx.Response(
                200,
                json={
                    "name": "Tokyo",
                    "weather": [{"main": "Clouds", "description": "曇り"}],
                    "main": {
                        "temp": 18,
                        "feels_like": 17,
                        "humidity": 60,
                    },
                    "wind": {"speed": 2.5},
                },
            )

        transport = httpx.MockTransport(handler)
        async with httpx.AsyncClient(transport=transport) as client:
            report = await fetch_current_weather("secret", "Tokyo", client)

        self.assertEqual(report.location_name, "Tokyo")
        self.assertEqual(seen_params["q"], "Tokyo")
        self.assertEqual(seen_params["appid"], "secret")
        self.assertEqual(seen_params["units"], "metric")
        self.assertEqual(seen_params["lang"], "ja")

    async def test_fetch_current_weather_maps_404_to_location_not_found(
        self,
    ) -> None:
        transport = httpx.MockTransport(lambda request: httpx.Response(404))
        async with httpx.AsyncClient(transport=transport) as client:
            with self.assertRaises(WeatherLocationNotFoundError):
                await fetch_current_weather("secret", "Missing", client)

    async def test_fetch_current_weather_maps_401_to_api_key_error(self) -> None:
        transport = httpx.MockTransport(lambda request: httpx.Response(401))
        async with httpx.AsyncClient(transport=transport) as client:
            with self.assertRaises(WeatherApiKeyUnauthorizedError):
                await fetch_current_weather("secret", "Tokyo", client)


if __name__ == "__main__":
    unittest.main()
