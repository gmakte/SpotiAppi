import streamlit as st

from utils.styles import load_css
from utils.data_loader import load_data
from components.hero import render_hero
from components.podium import render_podium
from services.listening_rankings import top_listeners
from components.venn import render_venn
from services.shared_artists import (compute_shared_artists)


st.set_page_config(
    page_title="Spotify Dashboard",
    layout="wide"
)

# LOAD CUSTOM CSS
load_css()

# LOAD DATA
df = load_data()

render_hero(df)

# ROW 1
col1, col2 = st.columns([1, 2])

with col1:
    with st.container(border=True):
        render_podium(df)

with col2:
    with st.container(border=True):
        render_venn(df)

# ROW 2
col3, col4 = st.columns([1.2, 1])

with col3:
    with st.container(border=True):
        st.write("Obsession chart")

with col4:
    with st.container(border=True):
        st.write("Mood fingerprints")

# ROW 3
col5, col6 = st.columns([1, 2])

with col5:
    with st.container(border=True):
        st.write("Listening clock")

with col6:
    with st.container(border=True):
        st.write("Taste evolution")