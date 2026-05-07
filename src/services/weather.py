from dataclasses import dataclass
from typing import Any

import httpx


OPENWEATHER_CURRENT_WEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)


class WeatherServiceError(RuntimeError):
    pass


class WeatherLocationNotFoundError(WeatherServiceError):
    pass


class WeatherApiKeyUnauthorizedError(WeatherServiceError):
    pass


@dataclass(frozen=True)
class WeatherReport:
    location_name: str
    weather: str
    temperature_celsius: float
    feels_like_celsius: float
    humidity_percent: int
    wind_speed_mps: float
    comment: str


def build_weather_comment(weather: str, temperature_celsius: float) -> str:
    text = weather.lower()
    if "rain" in text or "drizzle" in text:
        return "Bring an umbrella before heading out."
    if "snow" in text:
        return "Watch your step and stay warm."
    if "clear" in text:
        return "Clear skies today. Enjoy the nice weather."
    if temperature_celsius >= 30:
        return "It may get hot today. Remember to drink water."
    if temperature_celsius <= 5:
        return "It is cold today. Dress warmly."
    return "Looks like a steady day. Take it at your pace."


def parse_openweather_response(payload: dict[str, Any]) -> WeatherReport:
    weather_items = payload.get("weather")
    main = payload.get("main")
    wind = payload.get("wind", {})

    if not isinstance(weather_items, list) or not weather_items:
        raise WeatherServiceError("OpenWeatherMap response has no weather.")
    if not isinstance(main, dict):
        raise WeatherServiceError("OpenWeatherMap response has no main data.")
    if not isinstance(wind, dict):
        raise WeatherServiceError("OpenWeatherMap response has invalid wind data.")

    weather_item = weather_items[0]
    if not isinstance(weather_item, dict):
        raise WeatherServiceError("OpenWeatherMap weather item is invalid.")

    weather_main = str(weather_item.get("main") or "")
    weather = str(weather_item.get("description") or weather_main or "")
    if weather == "":
        raise WeatherServiceError("OpenWeatherMap weather description is empty.")

    try:
        temperature = float(main["temp"])
        feels_like = float(main["feels_like"])
        humidity = int(main["humidity"])
        wind_speed = float(wind.get("speed", 0))
    except (KeyError, TypeError, ValueError) as error:
        raise WeatherServiceError("OpenWeatherMap response is incomplete.") from error

    location_name = str(payload.get("name") or "")
    if location_name == "":
        raise WeatherServiceError("OpenWeatherMap location name is empty.")

    return WeatherReport(
        location_name=location_name,
        weather=weather,
        temperature_celsius=temperature,
        feels_like_celsius=feels_like,
        humidity_percent=humidity,
        wind_speed_mps=wind_speed,
        comment=build_weather_comment(f"{weather} {weather_main}", temperature),
    )


async def fetch_current_weather(
    api_key: str,
    location: str,
    client: httpx.AsyncClient | None = None,
) -> WeatherReport:
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",
        "lang": "en",
    }

    async def request(active_client: httpx.AsyncClient) -> WeatherReport:
        try:
            response = await active_client.get(
                OPENWEATHER_CURRENT_WEATHER_URL,
                params=params,
            )
        except httpx.HTTPError as error:
            raise WeatherServiceError("Failed to connect to OpenWeatherMap.") from error

        if response.status_code == 404:
            raise WeatherLocationNotFoundError(location)
        if response.status_code == 401:
            raise WeatherApiKeyUnauthorizedError(
                "OpenWeatherMap rejected the API key."
            )
        if response.status_code >= 400:
            raise WeatherServiceError(
                f"OpenWeatherMap returned {response.status_code}."
            )

        try:
            payload = response.json()
        except ValueError as error:
            raise WeatherServiceError("OpenWeatherMap response is not JSON.") from error

        if not isinstance(payload, dict):
            raise WeatherServiceError("OpenWeatherMap response is invalid.")
        return parse_openweather_response(payload)

    if client is not None:
        return await request(client)

    timeout = httpx.Timeout(10.0)
    async with httpx.AsyncClient(timeout=timeout) as active_client:
        return await request(active_client)
