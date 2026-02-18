library(worldfootballR)
library(tidyverse)

#Get the data for each leagues' 2024/25 matches and put it into 1 dataset

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

# Duplicate the data to get a complete record of each match for each team

matches_home <- select(.data = all_2025, c("Competition_Name", "Country", "Home", "Away", "HomeGoals", "AwayGoals")) %>%
  rename("Team" = Home, "Opp" = Away) %>%
  mutate(Venue = "H") %>%
  mutate(Result = case_when(
    HomeGoals > AwayGoals ~ "W",
    HomeGoals < AwayGoals ~ "L",
    TRUE ~ "D"
  )) %>%
  mutate(Diff = HomeGoals - AwayGoals)

matches_away <- select(.data = all_2025, c("Competition_Name", "Country", "Home", "Away", "HomeGoals", "AwayGoals")) %>%
  rename("Team" = Away, "Opp" = Home) %>%
  mutate(Venue = "A") %>%
  mutate(Result = case_when(
    HomeGoals > AwayGoals ~ "L",
    HomeGoals < AwayGoals ~ "W",
    TRUE ~ "D"
  )) %>%
  mutate(Diff = AwayGoals - HomeGoals)

#Put the data back together again

matches_clean <- rbind(matches_home, matches_away) %>% relocate(Venue, .before = HomeGoals)

write.csv(matches_clean, file = "data/2025_match_results.csv")