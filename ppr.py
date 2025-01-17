import pandas as pd

SOURCE_FILE = "football_data/Game_Logs_Quarterback.csv"
MIN_ATTEMPTS = (
    14  # From 1978–present, the minimum number of passing attempts per team game is 14.
)
df = pd.read_csv(SOURCE_FILE)
print(df)
