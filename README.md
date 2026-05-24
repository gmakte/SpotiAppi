# SpotiAppi - Spotify dashboard

## Quickstart

You need to create and activate environment for this to work. So bellow are the cmd codes to start :)

Create env and load libraries to it:

```bash
conda create -n spotify-dashboard python=3.11 -y
conda activate spotify-dashboard
pip install -r requirements.txt
```

## Run viz

Start the dashboard with Streamlit:

```bash
streamlit run app.py
```

## Project layout

- `app.py`: main Streamlit app (use to make visualizations)
- `requirements.txt`: Python dependencies
- `data/`: CSV data used by the app (e.g., `cleaned.csv`, `full_*.csv`)

Example data files in this repo (data folder is ignored):

- `data/cleaned.csv` (used to clean our datasets)
- `data/full_Ashanti.csv`
- `data/full_Gabi.csv`

