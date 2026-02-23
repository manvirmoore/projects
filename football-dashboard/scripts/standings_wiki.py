import requests
import csv
from bs4 import BeautifulSoup
import time

# Establish the years and competitions we want
years = [2020,2021,2022,2023,2024] # Not including current league table
comps = [
    "Premier_League",
    "La_Liga",
    "Serie_A",
    "Ligue_1",
    "Bundesliga"
]

# Create a string for each season which will work in the Wikipedia url
seasons = []

for x in years:
    s = f"{x}–{x-2000+1}"
    seasons.append([s,x+1])

# Create a list of combinations of leagues and seasons to use in the scraping 
urls = []

for s, y in seasons:
    for c in comps:
        url = f"https://en.wikipedia.org/wiki/{s}_{c}"
        urls.append([url,c,s,y])

# Establish the header for resposible scraping
headers = {
    "User-Agent": "MyWikiScript/1.0 (manvir.moore@yahoo.co.uk)"
}

# Create and populate the data
data = [["Pos",	"Team","Pld","W","D","L","GF","GA","GD","Pts","Qualification or relegation", "League", "Season", "Season_end"]] # header row

for url in urls:
    res = requests.get(url[0], headers=headers)
    res.raise_for_status() # checks for request errors
    soup = BeautifulSoup(res.text, "html.parser")
    headline = soup.find(id="League_table") # Finds the league table section of the page
    table = headline.find_next("table", class_="wikitable") # finds the table itself
    rows = table.find_all("tr") # reads the rows of the table
    
    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
        # Skip header row
        if cols[0] == "Pos": continue 
        # Add the league and year to the row. Add an entry when there is no comment to keep columns aligned.
        if len(cols) == 10: cols.extend([' ', url[1], url[2], url[3]])
        else: cols.extend([url[1], url[2], url[3]]) 
        # Add the row to the data list
        data.append(cols) 
    
    print(f"Got {url[1]} {url[2]}") # prints which section has been completed
    time.sleep(5) # waits 5 seconds before starting again, to avoid any 403 errors from scraping too quickly

# Get rid of champion / relegated / other suffixes
for row in data:
    row[1] = row[1].replace("(C)", "")
    row[1] = row[1].replace("(R)", "")
    row[1] = row[1].replace("(O)", "")
    row[1] = row[1].replace("[b]", "")
    row[1] = row[1].replace("[c]", "")

with open("football-dashboard/data/standings.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Done")