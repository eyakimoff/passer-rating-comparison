import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define the data file path relative to the project root
SOURCE_FILE = PROJECT_ROOT / "data" / "Game_Logs_Quarterback.csv"
CLEANED_FILE = PROJECT_ROOT / "data" / "cleaned_Game_Logs_Quarterback.csv"
df = pd.read_csv(SOURCE_FILE)
MIN_ATTEMPTS = (
    14  # From 1978–present, the minimum number of passing attempts per team game is 14.
)

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

df_cleaned = (
    df.drop(["Position", "Player Id"], axis=1)  # remove redundant columns
    .replace("--", 0)  # Replace '--' with 0
    .loc[df["Season"].isin(["Regular Season", "Postseason"])]  # remove preseason games
)

for col in numeric_columns:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")

df_cleaned.loc[
    lambda x: x["Passes Attempted"] >= 14  # Drop where QB attempted less than 14 passes
]

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
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")

df_cleaned = df_cleaned.loc[
    lambda x: x["Passes Attempted"]
    >= MIN_ATTEMPTS  # Drop where QB attempted less than 14 passes
]

# adding 'Perfect' Passer Rating
df_cleaned["Refined Passer Rating"] = round(
    (
        (
            (df_cleaned["Passing Yards Per Attempt"] - 3) * 0.25
            + (df_cleaned["TD Passes"] / df_cleaned["Passes Attempted"]) * 20
            + (2.375 - (df_cleaned["Ints"] / df_cleaned["Passes Attempted"]))
        )
        / 6
    )
    * 100,
    1,
)

df_cleaned["Passer Rating Difference"] = round(
    df_cleaned["Refined Passer Rating"] - df_cleaned["Passer Rating"]
)


# Sort data based on refined passer rating
df_cleaned = df_cleaned.sort_values(by="Refined Passer Rating", ascending=False)

# concatenate game date columnt and year to get mm/dd/yyy
df_cleaned["Game Date"] = df_cleaned["Game Date"] + "/" + df["Year"].astype(str)

# TODO: may need to move this to other file
df_cleaned["Game Date"] = pd.to_datetime(df_cleaned["Game Date"])

# change name format from 'lastname, firstname' to 'fistname lastname'
df_cleaned["Name"] = df_cleaned["Name"].apply(
    lambda x: " ".join(reversed(x.split(", ")))
)

df_cleaned.to_csv(CLEANED_FILE, index=False)


def get_dataframe():
    return df_cleaned
