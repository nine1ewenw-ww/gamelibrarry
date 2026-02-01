
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("RAWG_API_KEY")

BAZA_URL = "https://api.rawg.io/api/games"

params = {"key": API_KEY, "genres": 4, "page_size": 5}

try:
    response = requests.get(BAZA_URL, params=params)
    response.raise_for_status()
    games = response.json().get("results", [])
except requests.RequestException as err:
    print(f"ошибка cписка игр: {err}")
    exit()

for game in games:
    game_id = game.get("id")
    game_name = game.get("name")
    slug = game.get("slug")
    released = game.get("released")

    print(f"\n{game_name} ({released})")
    print(f"https://rawg.io/games/{slug}")

    ss_resp = requests.get(f"{BAZA_URL}/{game_id}/screenshots", params={"key": API_KEY})
    ss_resp.raise_for_status()
    screenshots = ss_resp.json().get("results", [])
    
    stores_resp = requests.get(f"{BAZA_URL}/{game_id}/stores", params={"key": API_KEY})
    stores_resp.raise_for_status()
    stores = stores_resp.json().get("results", [])
    print("Где купить:")
    for store in stores:
        url = store.get("url")
        print(url)
