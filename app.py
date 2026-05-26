import streamlit as st

from utils.styles import load_css
from utils.data_loader import load_data
from components.hero import render_hero
from components.podium import render_podium
from services.listening_rankings import top_listeners
from components.venn import render_venn
from services.shared_artists import (compute_shared_artists)
from services.obsession_service import (compute_obsession_metrics)
from components.obsession import render_obsession
from components.users_card import (render_users_card)
from components.mood import (render_mood)
from components.clock import (render_clock)

st.set_page_config(
    page_title="Spotify Dashboard",
    layout="wide"
)

# LOAD CUSTOM CSS
load_css()

# LOAD DATA
df = load_data()

# ROW 1

col1, col2 = st.columns([1, 2])

with col1:
    render_hero(df)

with col2:
    render_users_card(df)

# ROW 2
col2, col3 = st.columns([1, 2])

with col2:
    render_podium(df)

with col3:
    render_venn(df)


render_obsession(df)

# ROW 3
render_mood(df)

# ROW 4
render_clock(df)

# ROW 5
with st.container(border=True):
    st.write("Taste evolution")