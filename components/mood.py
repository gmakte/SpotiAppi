import streamlit as st

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

    st.markdown("""

    <div class="mood-diagnosis-wrapper">

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:#4f6dff;">
    Ashanti
    </div>

    <div class="diagnosis-title">
    Melancholic Soul
    </div>

    </div>

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:#FF8A3D;">
    Maribel
    </div>

    <div class="diagnosis-title">
    Energetic Beast
    </div>

    </div>

    <div class="mood-diagnosis-card">

    <div class="diagnosis-name"
    style="color:#FF8FD8;">
    Gabi
    </div>

    <div class="diagnosis-title">
    Dreamy Queen
    </div>

    </div>

    </div>

    """, unsafe_allow_html=True)
