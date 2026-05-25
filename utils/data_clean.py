from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")


def load_user_file(path: Path) -> pd.DataFrame:
	sep = "\t" if path.suffix.lower() == ".tsv" else ","
	frame = pd.read_csv(path, sep=sep)
	frame["user"] = path.stem.replace("full_", "")
	return frame


source_files = sorted(
	path for path in DATA_DIR.iterdir() if path.stem.startswith("full_") and path.suffix.lower() in {".csv", ".tsv"}
)

if not source_files:
	raise FileNotFoundError("No input files found in data/. Expected files named full_*.csv or full_*.tsv")

frames = [load_user_file(path) for path in source_files]

# Combine all user files into one dataset
df = pd.concat(frames, ignore_index=True)

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
df.to_csv(DATA_DIR / "cleaned.csv", index=False)

print(f"Cleaned data saved to {DATA_DIR / 'cleaned.csv'}")