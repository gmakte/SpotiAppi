import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(page_title="Top Artists", layout="wide")

st.title("Top Artists Dashboard")

# ----------------------------
# LOAD DATA (centralized)
# ----------------------------
df = load_data()

# ----------------------------
# FILTER
# ----------------------------
users = df["user"].unique()
selected_users = st.multiselect("Select user", users, default=users)

df = df[df["user"].isin(selected_users)]

# ----------------------------
# TOP ARTISTS
# ----------------------------
top_artists = (
    df.groupby(["master_metadata_album_artist_name", "user"])["minutes"]
    .sum()
    .reset_index()
    .sort_values("minutes", ascending=False)
    .head(20)
)

fig = px.bar(
    top_artists,
    x="minutes",
    y="master_metadata_album_artist_name",
    color="user",
    orientation="h",
    title="Top Artists"
)

fig.update_layout(
    plot_bgcolor="#0B0B0B",
    paper_bgcolor="#0B0B0B",
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)

if st.button("Go to Home"):
    st.switch_page("app.py")