import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned.csv")

    df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
    df["date"] = df["ts"].dt.date
    df["minutes"] = df["ms_played"] / 60000

    return df