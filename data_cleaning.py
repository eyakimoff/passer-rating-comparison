import pandas as pd

SOURCE_FILE = "football_data/Game_Logs_Quarterback.csv"

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

df_cleaned.to_csv("football_data/cleaned_Game_Logs_Quarterback.csv", index=False)
