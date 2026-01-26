library(worldfootballR)
library(tidyverse)

Prem_2025_players <- fb_league_stats(
  country = "ENG",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "player"
)

Ligue1_2025_players <- fb_league_stats(
  country = "FRA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "player"
)

LaLiga_2025_players <- fb_league_stats(
  country = "ESP",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "player"
)

Bundesliga_2025_players <- fb_league_stats(
  country = "GER",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "player"
)

SerieA_2025_players <- fb_league_stats(
  country = "ITA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st",
  non_dom_league_url = NA,
  stat_type = "standard",
  team_or_player = "player"
)

all_2025 <- rbind(Prem_2025_players, Ligue1_2025_players, Bundesliga_2025_players, LaLiga_2025_players, SerieA_2025_players)

write.csv(all_2025, file = "2025_player_stats.csv")