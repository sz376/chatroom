from os.path import join, dirname
from dotenv import load_dotenv
import os
import requests
import json

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)
openweatherkey = os.environ["OPEN_WEATHER_KEY"]


def temperature(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={openweatherkey}&units=metric"
    data = requests.get(url).json()
    temp = data["main"]["temp"]
    return temp
