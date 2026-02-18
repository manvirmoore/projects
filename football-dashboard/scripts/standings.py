import os
from dotenv import load_dotenv
import requests
import pandas as pd
import time

load_dotenv()
API_KEY = os.getenv('FOOTBALL_KEY')

base = "https://v3.football.api-sports.io/standings"

leagues = {
    39: "Premier League",
    140: "La Liga",
    135: "Serie A",
    78: "Bundesliga",
    61: "Ligue 1"
}

seasons = [2022, 2023, 2024]  # API uses year as season tag

all_rows = []
headers = {"x-apisports-key": API_KEY}

for league_id, league_name in leagues.items():
    for season in seasons:
        params = {"league": league_id, "season": season}
        r = requests.request("GET", base, headers=headers, params=params).json()
        for team in r["response"][0]["league"]["standings"][0]:
             all_rows.append({
                 "league": league_name,
                 "season": season,
                 "team": team["team"]["name"],
                 "position": team["rank"]
             })
        time.sleep(6)

df = pd.DataFrame(all_rows)

df.to_csv("football-dashboard/data/big5_standings.csv", index=False)
