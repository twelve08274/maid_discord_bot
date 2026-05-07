import discord
from discord.ext import commands

from ..config import (
    ConfigError,
    get_openweather_api_key,
    get_weather_default_location,
)
from ..database.connection import get_connection
from ..database.repositories.users import (
    add_affection,
    get_user_by_discord_id,
)
from ..database.schema import initialize_database
from ..services.weather import (
    WeatherApiKeyUnauthorizedError,
    WeatherLocationNotFoundError,
    WeatherReport,
    WeatherServiceError,
    fetch_current_weather,
)


def build_weather_embed(report: WeatherReport) -> discord.Embed:
    embed = discord.Embed(
        title=f"Weather in {report.location_name}",
        description=report.comment,
        color=0x70B7FF,
    )
    embed.add_field(name="Weather", value=report.weather, inline=True)
    embed.add_field(
        name="Temperature",
        value=f"{report.temperature_celsius:.1f} C",
        inline=True,
    )
    embed.add_field(
        name="Feels like",
        value=f"{report.feels_like_celsius:.1f} C",
        inline=True,
    )
    embed.add_field(
        name="Humidity",
        value=f"{report.humidity_percent}%",
        inline=True,
    )
    embed.add_field(
        name="Wind",
        value=f"{report.wind_speed_mps:.1f} m/s",
        inline=True,
    )
    embed.set_footer(text="Affection +1")
    return embed


def register_weather_command(bot: commands.Bot) -> None:
    @bot.tree.command(
        name="weather",
        description="Check today's weather.",
    )
    async def weather(interaction: discord.Interaction) -> None:
        with get_connection() as connection:
            initialize_database(connection)
            user = get_user_by_discord_id(connection, interaction.user.id)
            if user is None:
                await interaction.response.send_message(
                    "Please use /register first.",
                    ephemeral=True,
                )
                return

        try:
            api_key = get_openweather_api_key()
            location = get_weather_default_location()
        except ConfigError as error:
            message = "Weather API key is not configured."
            if "WEATHER_DEFAULT_LOCATION" in str(error):
                message = "Weather default location is not configured."
            await interaction.response.send_message(message, ephemeral=True)
            return

        await interaction.response.defer()

        try:
            report = await fetch_current_weather(api_key, location)
        except WeatherApiKeyUnauthorizedError:
            await interaction.followup.send(
                "Weather API key is invalid. Please check the configuration."
            )
            return
        except WeatherLocationNotFoundError:
            await interaction.followup.send(
                "Weather was not found for the configured location."
            )
            return
        except WeatherServiceError:
            await interaction.followup.send(
                "Could not fetch weather right now. Please try again later."
            )
            return

        with get_connection() as connection:
            initialize_database(connection)
            user = get_user_by_discord_id(connection, interaction.user.id)
            if user is None:
                await interaction.followup.send("Please use /register first.")
                return
            add_affection(connection, int(user["id"]), 1)

        await interaction.followup.send(embed=build_weather_embed(report))
