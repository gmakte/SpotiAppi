#APP with no pages
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio
# from utils.data_loader import load_data


# # ----------------------------
# #THEME SETUP
# # ----------------------------
# pio.templates.default = "plotly_dark"

# SPOTIFY_GREEN = "#0F6E30"
# SPOTIFY_GREEN_LIGHT = "#83f0a9"
# BG = "#0B0B0B"

# st.set_page_config(page_title="Spotify Dashboard", layout="wide")

# st.title("Spotify Listenings")
# st.caption("Comparing friends tastes and music obsetions")

# # ----------------------------
# #LOAD DATA
# # ----------------------------
# #df = pd.read_csv("data/cleaned.csv")
# df = load_data()

# df["ts"] = pd.to_datetime(df["ts"], errors="coerce")

# # ----------------------------
# #SIDEBAR FILTERS
# # ----------------------------
# st.sidebar.title("Filters")

# users = df["user"].unique()
# selected_users = st.sidebar.multiselect("Select user", users, default=users)

# df = df[df["user"].isin(selected_users)]

# # ----------------------------
# #METRICS
# # ----------------------------
# df["minutes"] = df["ms_played"] / 60000

# col1, col2, col3 = st.columns(3)

# col1.metric("Total Listening (hrs)", round(df["minutes"].sum() / 60, 1))
# col2.metric("Total Tracks", df.shape[0])
# col3.metric("Unique Artists", df["master_metadata_album_artist_name"].nunique())

# st.markdown("---")

# # ----------------------------
# #DAILY TREND
# # ----------------------------
# daily = df.groupby([df["ts"].dt.date, "user"])["minutes"].sum().reset_index()
# daily.columns = ["date", "user", "minutes"]

# fig1 = px.line(
#     daily,
#     x="date",
#     y="minutes",
#     color="user",
#     color_discrete_sequence=[SPOTIFY_GREEN, SPOTIFY_GREEN_LIGHT],
#     title="Daily Listening Time"
# )

# fig1.update_layout(
#     paper_bgcolor=BG,
#     plot_bgcolor=BG,
#     font_color="white"
# )

# st.plotly_chart(fig1, use_container_width=True)

# # ----------------------------
# #TOP ARTISTS
# # ----------------------------
# top_artists = (
#     df.groupby(["master_metadata_album_artist_name", "user"])["minutes"]
#     .sum()
#     .reset_index()
#     .sort_values("minutes", ascending=False)
#     .head(15)
# )

# fig2 = px.bar(
#     top_artists,
#     x="minutes",
#     y="master_metadata_album_artist_name",
#     color="user",
#     orientation="h",
#     color_discrete_sequence=[SPOTIFY_GREEN, SPOTIFY_GREEN_LIGHT],
#     title="Top Artists"
# )

# fig2.update_layout(
#     paper_bgcolor=BG,
#     plot_bgcolor=BG,
#     font_color="white"
# )

# st.plotly_chart(fig2, use_container_width=True)

# # ----------------------------
# #SKIP RATE
# # ----------------------------
# if "skipped" in df.columns:
#     skip_rate = df.groupby("user")["skipped"].mean().reset_index()

#     fig3 = px.bar(
#         skip_rate,
#         x="user",
#         y="skipped",
#         color="user",
#         color_discrete_sequence=[SPOTIFY_GREEN, SPOTIFY_GREEN_LIGHT],
#         title="⏭ Skip Rate"
#     )

#     fig3.update_layout(
#         paper_bgcolor=BG,
#         plot_bgcolor=BG,
#         font_color="white"
#     )

#     st.plotly_chart(fig3, use_container_width=True)

import streamlit as st

st.set_page_config(layout="wide")

st.title("Spotify Dashboard")

st.markdown("## Spotify data analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Trends")
    st.write("Daily, weekly, monthly listening")
    if st.button("Open Trends"):
        st.switch_page("pages/trends.py")

with col2:
    st.markdown("### Artists")
    st.write("Top artists and ranking")
    if st.button("Open Artists"):
        st.switch_page("pages/artists.py")

with col3:
    st.markdown("### Comparison")
    st.write("Friend stats")
    if st.button("Open Compare"):
        st.switch_page("pages/comparison.py")