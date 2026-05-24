# SpotiAppi - Spotify dashboard

## Quickstart

You need to create and activate environment for this to work. So bellow are the cmd codes to start :)

Create env and load libraries to it:

```bash
conda create -n spotify-dashboard python=3.11 -y
conda activate spotify-dashboard
pip install -r requirements.txt
```

## Add data to data folder
1. Add full_Ashanti.csv, full_Gabi.csv, full_Maribel.csv from Ashanti's repo
2. Run data_clean.py. It will create cleaned.csv file
3. That cleaned.csv file is later loaded into app by calling utils/data_loader.py
4. Add git ignore file:

```bash
data/
*.csv
__pycache__/*
```

## Visualizations are in pages
Example: pages/trends.py has trends page line chart which is called by app.py (main file)

## Main file
Main file that is rendering the whole app is app.py

To run the app, run this in cmd (remeber to activate your prepared env and be in repo folder):

```bash
streamlit run app.py
```

## Project layout schema

spotify-dashboard/
├── app.py
├── pages/
│   ├── artists.py
│   ├── comparison.py
│   ├── trends.py
├── utils/
│   └── data_loader.py
├── data/
│   └── cleaned.csv
