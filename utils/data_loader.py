import pandas as pd

def load_data():
    df = pd.read_csv("data/cleaned.csv")

    df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
    df["date"] = df["ts"].dt.date
    df["minutes"] = df["ms_played"] / 60000

    return df