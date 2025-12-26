from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    country: str
    condition: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    