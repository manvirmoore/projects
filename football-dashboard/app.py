import streamlit as st
import pandas as pd
import altair as alt

teams = pd.read_csv('data/teams.csv')

team = st.selectbox(
    label="Pick a team", 
    options=teams['full_name'].unique(), 
    index=76,
    width=300
)


matches = pd.read_csv('data/2025_match_results.csv')
players = pd.read_csv('data/2025_player_stats.csv')
standings = pd.read_csv('data/big5_standings.csv')

position = pd.merge(standings, teams, how="left", left_on="team", right_on="api-football_name")
record = pd.merge(matches, teams, how="left", left_on="Team", right_on="worldfootballR_name")
common_players = pd.merge(players, teams, how="left", left_on="Squad", right_on="worldfootballR_name")

wins = record[(record['full_name'] == team) & (record['Result'] == "W")]
draws = record[(record['full_name'] == team) & (record['Result'] == "D")]
losses = record[(record['full_name'] == team) & (record['Result'] == "L")]
big_loss = record[record['full_name'] == team].sort_values(by='Diff', ascending=True).head(1)
big_win = record[record['full_name'] == team].sort_values(by='Diff', ascending=False).head(1)
team_common = common_players[common_players['full_name'] == team].sort_values(by='MP_Playing Time', ascending=False).head(11)
team_common = team_common.rename(columns={"Pos":"Position", "MP_Playing Time":"Appearences"})

# Title
st.title(team, text_alignment="center")

# Historic league positions
st.altair_chart(
    alt.Chart(position[position['full_name'] == team])
    .mark_line(point=True)
    .encode(
        x=alt.X(
            "season:Q",
            scale=alt.Scale(domain=[2022, 2024]),
            axis=alt.Axis(tickMinStep=1, format=".0f"),
            title="Year",
        ),
        y=alt.Y(
            "position:Q",
            scale=alt.Scale(domain=[20, 1]),  # reversed so 1 is at top
            title="League Position",
        ),
        tooltip=["season", "position"],
    )
    .properties(width=600, height=400)
    .interactive()
)

# Wins / Draws / Losses record last season
with st.container(horizontal=True, gap="medium"):
    cols = st.columns(3, gap="medium", width=1200)

    with cols[0]:
        st.metric(
            label="Wins last season",
            value=f"{len(wins)}",
            # delta=None,
            width="content",
        )

    with cols[1]:
        st.metric(
            label="Draws last season",
            value=f"{len(draws)}",
            # delta=None,
            width="content",
        )

    with cols[2]:
        st.metric(
            label="Losses last season",
            value=f"{len(losses)}",
            # delta=None,
            width="content",
        )

# Biggest win
with st.container(horizontal=True, gap="medium"):
    cols = st.columns(2, gap="medium", width=1200)

    with cols[0]:
        st.metric(
            label="Biggest win",
            value=f"{big_win['Opp'].to_string(index=False)}",
            # delta=None,
            width="content",
        )

    with cols[1]:
        st.metric(
            label='Score',
            value=f"{big_win['HomeGoals'].to_string(index=False)}:{big_win['AwayGoals'].to_string(index=False)}",
            width="content"
        )

# Biggest loss
with st.container(horizontal=True, gap="medium"):
    cols = st.columns(2, gap="medium", width=1200)

    with cols[0]:
        st.metric(
            label="Biggest loss",
            value=f"{big_loss['Opp'].to_string(index=False)}",
            # delta=None,
            width="content",
        )

    with cols[1]:
        st.metric(
            label='Score',
            value=f"{big_loss['HomeGoals'].to_string(index=False)}:{big_loss['AwayGoals'].to_string(index=False)}",
            width="content"
        )

# Most common XI
st.caption("Most common XI last season:")
st.dataframe(
    data=team_common[['Player', 'Position', 'Appearences']],
    hide_index=True,
    height="content"
)