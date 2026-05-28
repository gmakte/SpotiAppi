import streamlit as st

from assets.palette import USER_COLORS

from services.mood_service import (
    compute_mood_distribution
)

from charts.mood_chart import (
    create_mood_chart
)


def render_mood(df):

    mood_df = compute_mood_distribution(
        df
    )

    fig = create_mood_chart(
        mood_df
    )

    st.markdown(
        "### Mood Fingerprints"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(f"""

    <div class="mood-diagnosis-wrapper">

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:{USER_COLORS['Ashanti']};">
    Ashanti
    </div>

    <div class="diagnosis-title">
    Melancholic Soul
    </div>

    </div>

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:{USER_COLORS['Maribel']};">
    Maribel
    </div>

    <div class="diagnosis-title">
    Energetic Beast
    </div>

    </div>

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:{USER_COLORS['Gabi']};">
    Gabi
    </div>

    <div class="diagnosis-title">
    Dreamy Queen
    </div>

    </div>

    </div>

    """, unsafe_allow_html=True)
