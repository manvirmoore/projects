library(worldfootballR)
library(tidyverse)

Prem_2025_teams <- fb_season_team_stats(
  country = "ENG",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  stat_type = "standard",
  time_pause = 10
)

Ligue1_2025_teams <- fb_league_stats(
  country = "FRA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "team"
)

LaLiga_2025_teams <- fb_league_stats(
  country = "ESP",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "team"
)

Bundesliga_2025_teams <- fb_league_stats(
  country = "GER",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "team"
)

SerieA_2025_teams <- fb_league_stats(
  country = "ITA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "team"
)

all_2025 <- rbind(Prem_2025_teams, Ligue1_2025_teams, Bundesliga_2025_teams, LaLiga_2025_teams, SerieA_2025_teams)

write.csv(all_2025, file = "2025_team_stats.csv")