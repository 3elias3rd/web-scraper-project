import requests
import os
from fastapi import HTTPException

# Checks for environment variable named OPENWEATHER_API_KEY.
# If the environment variable doesn't exist use the default key. 
API_KEY = os.getenv("OPENWEATHER_API_KEY", "3364a2a3f1e563b6d721f160faa75468")

# Function weather data for a given city.
# Async allows function to run without blocking other tasks in FastApi server.
# Returns a dictionary with raw JSON response from weather map.
async def fetch_weather(city: str) -> dict: 
    url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Query parameters to be sent with the requests
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    # Send get request to weatherapi with preset parameters.
    response = requests.get(url, params=params)

    # Raise error if get request fails
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch weather data: {response.text}")
    
    #Return response as a Python dict
    return response.json()

# Function to transform raw API response into a simplified format for WeatherResponse model.
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

