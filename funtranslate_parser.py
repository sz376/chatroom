from os.path import join, dirname
from dotenv import load_dotenv
import os
import requests

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)


def funtranslate(text):
    url = f"https://api.funtranslations.com/translate/yoda.json?text={text}"
    res = requests.get(url)
    data = res.json()
    return data["contents"]["translated"]
