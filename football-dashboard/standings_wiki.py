import requests
import csv
from bs4 import BeautifulSoup
import time

years = [2020,2021,2022,2023,2024] # Not including current league table
comps = [
    "Premier_League",
    "La_Liga",
    "Serie_A",
    "Ligue_1",
    "Bundesliga"
]

seasons = []

for x in years:
    s = f"{x}–{x-2000+1}"
    seasons.append(s)

urls = []

for s in seasons:
    for c in comps:
        url = f"https://en.wikipedia.org/wiki/{s}_{c}"
        urls.append([url,c,s])

headers = {
    "User-Agent": "MyWikiScript/1.0 (manvir.moore@yahoo.co.uk)"
}

data = [["Pos",	"Team","Pld","W","D","L","GF","GA","GD","Pts","Qualification or relegation", "League", "Season"]]

for url in urls:
    res = requests.get(url[0], headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    headline = soup.find(id="League_table")
    table = headline.find_next("table", class_="wikitable")
    rows = table.find_all("tr")
    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
        if cols[0] == "Pos": continue # skips header row
        cols.extend([url[1], url[2]])
        data.append(cols)
    print(f"Got {url[1]} {url[2]}")
    time.sleep(5)

with open("new_standings.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Done")