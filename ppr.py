import pandas as pd
import streamlit as st

SOURCE_FILE = "football_data/Game_Logs_Quarterback.csv"
MIN_ATTEMPTS = (
    14  # From 1978–present, the minimum number of passing attempts per team game is 14.
)
df = pd.read_csv(SOURCE_FILE)


df_cleaned = (
    df.drop("Position", axis=1)
    .replace("--", pd.NA)  # Replace '--' with NaN
    .dropna(subset=["Passes Attempted"])  # Drop where no passes attempted
    .apply(pd.to_numeric, errors="ignore")  # TODO: fix this, not convert year
    .loc[lambda x: x["Passes Attempted"] >= 14]  # Drop where QB attempted >= 14 passes
    .reset_index(drop=True)  # Reset index after cleaning
)

# adding 'Perfect' Passer Rating
df_cleaned["improved passer rating"] = (
    (df_cleaned["Completion Percentage"] - 0.3) * 5
    + (df_cleaned["Passing Yards Per Attempt"] - 3) * 0.25
    + (df_cleaned["TD Passes"] / df_cleaned["Passes Attempted"]) * 20
    + 2.375  # TODO: maybe remove?
    - (df_cleaned["Ints"] / df_cleaned["Passes Attempted"])
)
print(df_cleaned)

st.dataframe(df_cleaned)


# to toggle if the viewer wants to include preaseason games
def preseason_toggle(df):
    df.loc[lambda x: x["Season"] == "Regular Season"]
