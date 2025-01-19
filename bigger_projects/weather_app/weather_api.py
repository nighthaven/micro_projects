import json
from typing import Final
from datetime import datetime
from models import Weather
import requests

API_KEY: Final[str] = "2decb748f1de082b5af9b0f373055ecd"
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city_name: str, mock: bool = True) -> dict:
    if mock:
        with open("dummy_data.json", "r") as file:
            return json.load(file)
    payload: dict = {"q": city_name, "appid": API_KEY, "units": "metric"}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()
    if not mock:
        with open("dummy_data.json", "w") as file:
            json.dump(data, file)

    return data

def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get("list")
    if not days:
        raise Exception(f"Problem with json: {weather}")
    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(
            date=datetime.fromtimestamp(day.get("dt")),
            details=(details := day.get("main")),
            temp=details.get("temp"),
            weather=(weather := day.get("weather")),
            description=weather[0].get("description"),
        )
        list_of_weather.append(w)
    return list_of_weather

"""
if __name__ == "__main__":
    # print(get_weather(city_name="Tokyo", mock=False)) # pour créer le fichier dummy_data
    current_weather: dict = get_weather("tokyo", mock=True)
    weather: list[Weather] = get_weather_details(current_weather)
    for w in weather:
        print(w)
"""