import pandas as pd

# Load data
me = pd.read_csv("data/full_Gabi.csv")
friend = pd.read_csv("data/full_Ashanti.csv")

# Add user label
me["user"] = "Gabi"
friend["user"] = "Ashanti"

# Combine
df = pd.concat([me, friend], ignore_index=True)

# --- CLEANING ---
df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
df = df.dropna(subset=["ts"])

df["date"] = df["ts"].dt.date
df["week"] = df["ts"].dt.to_period("W").astype(str)
df["month"] = df["ts"].dt.to_period("M").astype(str)

df["minutes"] = df["ms_played"] / 60000

# Keep only real music rows (remove podcasts/ads/empty tracks)
df = df.dropna(subset=["master_metadata_track_name"])

# Save cleaned file
df.to_csv("data/cleaned.csv", index=False)

print("Cleaned data saved to data/cleaned.csv")