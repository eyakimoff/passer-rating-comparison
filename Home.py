import pandas as pd
import streamlit as st
from data_cleaning import get_dataframe

df = get_dataframe()

st.title("Quarterback Refined Passer Rating Database")
st.subheader("Overview")
st.write(
    "Welcome to the homepage. Below is a table showing the refined passer rating leaderboards. You can toggle between a table which shows extensive game Details, and a simplified table with less game data. This showcases the difference between traditional passer rating formula and the refined version."
)

if "extensive" not in st.session_state:
    st.session_state.extensive = False

if st.button("Toggle Extensive Data"):
    st.session_state.extensive = not st.session_state.extensive

if st.session_state.extensive:
    st.dataframe(
        df[
            [
                "Name",
                "Year",
                "Season",
                "Week",
                "Opponent",
                "Outcome",
                "Passer Rating",
                "Refined Passer Rating",
                "Passer Rating Difference",
            ]
        ]
    )
else:
    st.dataframe(df)
