import streamlit as st
from data_cleaning import get_dataframe
from streamlit_tags import st_tags, st_tags_sidebar

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
print(str(selected_player))
