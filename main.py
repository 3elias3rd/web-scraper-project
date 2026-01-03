from fastapi import FastAPI, Query
from typing import Optional

from weather import fetch_weather, format_weather_response, WeatherResponse
# ^ assume your provided code lives in weather.py

app = FastAPI(
    title="Weather API",
    description="Simple FastAPI wrapper around OpenWeatherMap",
    version="1.0.0"
)


@app.get("/weather", response_model=WeatherResponse)
async def get_weather(
    city: str = Query(..., min_length=1, description="City name, e.g. London")
):
    """
    Fetch current weather for a given city.
    """
    raw_data = await fetch_weather(city)
    formatted = format_weather_response(raw_data)
    return formatted
