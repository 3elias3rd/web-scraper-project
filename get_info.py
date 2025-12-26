import requests
import os
from fastapi import HTTPException

API_KEY = os.getenv("OPENWEATHER_API_KEY", "3364a2a3f1e563b6d721f160faa75468")

async def fetch_weather(city: str):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch weather data: {response.text}")
    
    return response.json()

def format_weather_response(data:dict):
    return{
        "city": data["name"],
        "country": data["sys"]["country"],
        "condition": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

