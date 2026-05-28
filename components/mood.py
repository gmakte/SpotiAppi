import streamlit as st

from assets.palette import USER_COLORS

from services.mood_service import (
    compute_mood_distribution
)

from charts.mood_chart import (
    create_mood_chart
)


def render_mood(df):

    mood_df = compute_mood_distribution(df)

    fig = create_mood_chart(mood_df)

    mood_titles = {

        "Ashanti": "Melancholic Soul",
        "Gabi": "Dreamy Queen",
        "Maribel": "Energetic Beast"
    }

    st.html("""
    <div class="taste-evolution-title-inline">

        <span class="taste-evolution-title">
            Emotional Grid
        </span>

        <div class="taste-evolution-info-floating">
            <span class="taste-evolution-info-icon">i</span>

            <div class="taste-evolution-tooltip">
                Each percentage shows how much of a person’s listening belongs to a given mood category.
            </div>
        </div>

    </div>
    """)

    bottom_left, bottom_right = st.columns(
        [5.2, 1.2]
    )

    # =====================================================
    # LEFT → HEATMAP
    # =====================================================

    with bottom_left:

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

    # =====================================================
    # RIGHT → GLOWING CARDS
    # =====================================================

    with bottom_right:

        card_offsets = [140, 135, 135]

        for idx, (user, title) in enumerate(mood_titles.items()):

            color = USER_COLORS[user]

            st.html(
                f"""
            <div style="
            background:#111111;
            border-radius:24px;
            border:1.5px solid {color}40;
            box-shadow:
            0 0 18px {color}20,
            0 0 42px {color}12;
            width:220px;
            height:100px;

            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;

            text-align:center;

            margin-bottom:14px;

            transform:translateY({card_offsets[idx]}px);
            ">

            <div style="
            font-size:22px;
            font-weight:800;
            line-height:1;
            margin-bottom:14px;
            color:{color};
            ">
            {user}
            </div>

            <div style="
            font-size:15px;
            font-weight:600;
            line-height:1.35;
            color:white;
            max-width:160px;
            ">
            {title}
            </div>

            </div>
            """
            )