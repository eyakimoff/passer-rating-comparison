import pandas as pd
import streamlit as st

SOURCE_FILE = "football_data/cleaned_Game_Logs_Quarterback.csv"
MIN_ATTEMPTS = (
    14  # From 1978–present, the minimum number of passing attempts per team game is 14.
)
df = pd.read_csv(SOURCE_FILE)

numeric_columns = [
    "Games Started",
    "Passes Completed",
    "Passes Attempted",
    "Completion Percentage",
    "Passing Yards",
    "Passing Yards Per Attempt",
    "TD Passes",
    "Ints",
    "Sacks",
    "Sacked Yards Lost",
    "Passer Rating",
    "Rushing Attempts",
    "Rushing Yards",
    "Yards Per Carry",
    "Rushing TDs",
    "Fumbles",
    "Fumbles Lost",
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.loc[
    lambda x: x["Passes Attempted"]
    >= MIN_ATTEMPTS  # Drop where QB attempted less than 14 passes
]

# adding 'Perfect' Passer Rating
df["Improved Passer Rating"] = round(
    (
        (
            (df["Passes Completed"] / df["Passes Attempted"] - 0.3) * 5
            + (df["Passing Yards Per Attempt"] - 3) * 0.25
            + (df["TD Passes"] / df["Passes Attempted"]) * 20
            + (df["Ints"] / df["Passes Attempted"])
        )
        / 6
    )
    * 100,
    1,
)

st.dataframe(df)
