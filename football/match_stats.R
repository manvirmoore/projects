library(worldfootballR)

x <- load_match_results(
  country="ENG",
  gender="M",
  season_end_year = 2025,
  tier = "1st"
)

Prem_2025_matches <- load_match_results(
  country = "ENG",
  gender = "M",
  season_end_year = 2025,
  tier = "1st"
)

Ligue1_2025_matches <- load_match_results(
  country = "FRA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st"
)

LaLiga_2025_matches <- load_match_results(
  country = "ESP",
  gender = "M",
  season_end_year = 2025,
  tier = "1st"
)

Bundesliga_2025_matches <- load_match_results(
  country = "GER",
  gender = "M",
  season_end_year = 2025,
  tier = "1st"
)

SerieA_2025_matches <- load_match_results(
  country = "ITA",
  gender = "M",
  season_end_year = 2025,
  tier = "1st"
)

all_2025 <- rbind(Prem_2025_matches, Ligue1_2025_matches, Bundesliga_2025_matches, LaLiga_2025_matches, SerieA_2025_matches)

write.csv(all_2025, file = "2025_match_results.csv")