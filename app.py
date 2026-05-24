import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Spotify Dashboard", layout="wide")

# Load cleaned data
df = pd.read_csv("data/cleaned.csv")

df["ts"] = pd.to_datetime(df["ts"])

st.title("Spotify Listening Dashboard (Gabi vs Ashanti)")

# --- SIDEBAR FILTER ---
user_filter = st.sidebar.multiselect(
    "Select user",
    df["user"].unique(),
    default=df["user"].unique()
)

df = df[df["user"].isin(user_filter)]

# --- KPI METRICS ---
col1, col2, col3 = st.columns(3)

col1.metric("Total Listening (hrs)", round(df["minutes"].sum() / 60, 1))
col2.metric("Total Tracks", df.shape[0])
col3.metric("Unique Artists", df["master_metadata_album_artist_name"].nunique())

# --- DAILY TREND ---
daily = df.groupby([df["ts"].dt.date, "user"])["minutes"].sum().reset_index()
daily.columns = ["date", "user", "minutes"]

fig1 = px.line(
    daily,
    x="date",
    y="minutes",
    color="user",
    title="Daily Listening Time"
)

st.plotly_chart(fig1, use_container_width=True)

# --- TOP ARTISTS ---
top_artists = df.groupby(["master_metadata_album_artist_name", "user"])["minutes"].sum().reset_index()

top_artists = top_artists.sort_values("minutes", ascending=False).head(15)

fig2 = px.bar(
    top_artists,
    x="minutes",
    y="master_metadata_album_artist_name",
    color="user",
    orientation="h",
    title="Top Artists"
)

st.plotly_chart(fig2, use_container_width=True)

# --- SKIP RATE ---
if "skipped" in df.columns:
    skip = df.groupby("user")["skipped"].mean().reset_index()

    fig3 = px.bar(skip, x="user", y="skipped", title="Skip Rate")
    st.plotly_chart(fig3)