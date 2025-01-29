import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import plotly.graph_objects as go
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.data_cleaning import get_dataframe

df = get_dataframe()

st.title("Individual Player Data")

try:
    selected_player = st_tags(
        label="Player Name",
        text="enter one player name",
        suggestions=df["Name"].tolist(),
        maxtags=1,
    )
    if selected_player and selected_player[0].lower() not in [
        name.lower() for name in df["Name"].tolist()
    ]:
        raise KeyError("Player not found in the list.")
except KeyError as e:
    st.error(f"Error: {e}")

if selected_player:
    filtered_df = df[df["Name"].astype(str).str.lower() == selected_player[0].lower()]
    filtered_df = filtered_df[filtered_df["Season"] == "Regular Season"]
    year = st.selectbox("Year:", filtered_df["Year"].astype(int).unique())
    filtered_df = filtered_df[filtered_df["Year"].astype(int) == year]
    filtered_df = filtered_df[filtered_df["Game Date"] > "1/1/" + str(year)]
    filtered_df.sort_values(by=["Game Date"], inplace=True)
    print(filtered_df)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=filtered_df["Week"],
            y=filtered_df["Passer Rating"],
            name="Traditional Passer Rating",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=filtered_df["Week"],
            y=filtered_df["Refined Passer Rating"],
            name="Refined Passer Rating",
        )
    )
    st.plotly_chart(fig)
