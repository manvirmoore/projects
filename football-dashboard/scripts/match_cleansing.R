library(tidyverse)

matches <- read.csv("data/2025_match_results.csv") 
glimpse(matches)
names(matches)

# Duplicate the data to get a complete record of each match for each team

matches_home <- select(.data = matches, c("Competition_Name", "Country", "Home", "Away", "HomeGoals", "AwayGoals")) %>%
  rename("Team" = Home, "Opp" = Away) %>%
  mutate(Venue = "H") %>%
  mutate(Result = case_when(
    HomeGoals > AwayGoals ~ "W",
    HomeGoals < AwayGoals ~ "L",
    TRUE ~ "D"
  )) %>%
  mutate(Diff = HomeGoals - AwayGoals)

matches_away <- select(.data = matches, c("Competition_Name", "Country", "Home", "Away", "HomeGoals", "AwayGoals")) %>%
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

