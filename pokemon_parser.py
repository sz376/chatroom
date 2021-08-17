from os.path import join, dirname
from dotenv import load_dotenv
import os
import requests
import re

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)


def pokefacts(pokename):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokename}"
    res = requests.get(url)
    data = res.json()
    for i in range(len(data["flavor_text_entries"])):
        if data["flavor_text_entries"][i]["language"]["name"] == "en":
            flavor_text = data["flavor_text_entries"][i]["flavor_text"]
            text = ""
            for char in flavor_text:
                if char == "\n" or char == "\x0c":
                    text += " "
                else:
                    text += char
    return text
