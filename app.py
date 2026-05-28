import streamlit as st

from utils.styles import load_css
from utils.data_loader import load_data
from components.hero import render_hero
from components.users_card import render_users_card
from components.podium import render_podium
from components.venn import render_venn
from components.obsession import render_obsession
from components.mood import render_mood
from components.clock import render_clock
from components.genre_evolution import render_taste_evolution

st.set_page_config(
    page_title="Spotify Dashboard",
    layout="wide"
)

# LOAD CUSTOM CSS
load_css()

# LOAD DATA
#df = load_data()

# ROW 1
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    render_hero()

with col2:
    render_users_card()

st.markdown('</div>', unsafe_allow_html=True)



# ROW 2
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

col2, col3 = st.columns([1, 2])

with col2:
    render_podium()

with col3:
    render_venn()

st.markdown('</div>', unsafe_allow_html=True)


# ROW 3
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

render_obsession()

st.markdown('</div>', unsafe_allow_html=True)



# ROW 4
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

render_mood()

st.markdown('</div>', unsafe_allow_html=True)



# ROW 5
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

render_clock()

st.markdown('</div>', unsafe_allow_html=True)



# ROW 6
st.markdown('<div class="snap-section">', unsafe_allow_html=True)

render_taste_evolution()

st.markdown('</div>', unsafe_allow_html=True)
