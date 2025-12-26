import requests

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching weather data.", response.status_code, response.text)
        return None
    
    return response.json()

def print_weather(data):
    if not data:
        print("No data to show.")
        return None
    
    city = data["name"]
    country = data["sys"]["country"]
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\nWeather in {city}, {country}:")
    print(f"  Condition: {weather}")
    print(f"  Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"  Humidity: {humidity}%")
    print(f"  Wind: {wind} m/s")

def main():
    api_key = "3364a2a3f1e563b6d721f160faa75468"  # <-- Replace with your API key from https://openweathermap.org/api
    city = "Dubai"

    weather_data = get_weather(city, api_key)
    print_weather(weather_data)

if __name__ == "__main__":
    main()