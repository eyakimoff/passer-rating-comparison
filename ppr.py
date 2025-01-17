import pandas as pd

SOURCE_FILE = "football_data/Game_Logs_Quarterback.csv"
MIN_ATTEMPTS = (
    14  # From 1978–present, the minimum number of passing attempts per team game is 14.
)
df = pd.read_csv(SOURCE_FILE)

# For converting numeric string to integers/floats
numeric_columns = [
    "passes completed",
    "passes attempted",
    "completion percentage",
    "passing yards",
    "passing yards per attempt",
    "td passes",
    "ints",
    "sacks",
    "sacked yards lost",
    "passer rating",
    "rushing attempts",
    "rushing yards",
    "yards per carry",
    "rushing tds",
    "fumbles",
    "fumbles lost",
]

df[numeric_columns] = df[numeric_columns].apply(
    pd.to_numeric, errors="coerce"
)  # TODO: fix this

df_cleaned = (
    df.drop("Position", axis=1)
    .rename(columns=str.lower)  # Rename columns to lowercase
    .replace("--", pd.NA)  # Replace '--' with NaN
    .dropna(subset=["passes attempted"])  # Drop where no passes attempted
    .loc[lambda x: x["passes attempted"] >= 14]  # Drop where QB attempted >= 14 passes
    .reset_index(drop=True)  # Reset index after cleaning
)
print(df_cleaned["passes attempted"])

"""


    ATT = Number of passing attempts
    CMP = Number of completions
    YDS = Passing yards
    TD = Touchdown passes
    INT = Interceptions
"""
