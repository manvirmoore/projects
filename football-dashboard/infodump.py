import pandas as pd

teams = pd.read_csv('football-dashboard/teams.csv')
matches = pd.read_csv('football-dashboard/2025_match_results.csv')
players = pd.read_csv('football-dashboard/2025_player_stats.csv')
standings = pd.read_csv('football-dashboard/big5_standings.csv')

position = pd.merge(standings, teams, how="left", left_on="team", right_on="api-football_name")
record = pd.merge(matches, teams, how="left", left_on="Team", right_on="worldfootballR_name")
common_players = pd.merge(players, teams, how="left", left_on="Squad", right_on="worldfootballR_name")

x = input("Enter the name of a team: ")

if x not in teams['full_name'].to_list():
    print("Try a different team or spelling.")
    quit()

x_position = position[position['full_name'] == x]
print(f"This is where {x} finished in the league over the past 3 seasons:")
print(x_position[['season', 'position']].to_string(index=False))

wins = record[(record['full_name'] == x) & (record['Result'] == "W")]
draws = record[(record['full_name'] == x) & (record['Result'] == "D")]
losses = record[(record['full_name'] == x) & (record['Result'] == "L")]

print(f"Last season {x} had {len(wins)} wins, {len(draws)} draws, and {len(losses)} losses.")

big_loss = record[record['full_name'] == x].sort_values(by='Diff', ascending=True).head(1)
print(f"The team's biggest loss was to {big_loss['Opp'].to_string(index=False)}, losing by {big_loss['Diff'].to_string(index=False)} goals.")

big_win = record[record['full_name'] == x].sort_values(by='Diff', ascending=False).head(1)
print(f"The team's biggest win was to {big_win['Opp'].to_string(index=False)}, winning by {big_win['Diff'].to_string(index=False)} goals.")

x_common = common_players[common_players['full_name'] == x].sort_values(by='MP_Playing Time', ascending=False).head(11)
print("This was the most common starting XI last season:")
print(x_common[['Player', 'Pos', 'MP_Playing Time']].to_string(index=False))
