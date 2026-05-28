import streamlit as st
import pandas as pd

from charts.stacked_area import (
    render_genre_evolution_chart
)

from services.genre_evolution import (
    prepare_genre_evolution
)

from assets.palette import GENRE_COLORS, USER_COLORS

ARCHETYPES = {
    "Ashanti": "The Pop Icon",
    "Gabi": "The Eclectic",
    "Maribel": "The Shape-Shifter"
}

df = pd.read_csv('data/genre_evolution.csv')

def render_taste_evolution():
    st.html("""
    <div class="taste-evolution-title-inline">

        <span class="taste-evolution-title">
            Our taste evolution
        </span>

        <div class="taste-evolution-info-floating">
            <span class="taste-evolution-info-icon">i</span>

            <div class="taste-evolution-tooltip">
                Streamgraphs show the relative share of genres listened to over time.<br><br>

                • Full timeline: full Spotify history<br>
                • Aligned: same comparison period for everyone<br><br>

                Use “Choose genre” to isolate one genre on a shared baseline.
            </div>
        </div>

    </div>
    """)

    st.markdown("""
    <style>

    div[data-baseweb="select"] {
        max-width: 180px;
    }  
                

    .taste-evolution-legend-inline {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 18px;

        margin-top: 34px;
    }

    .taste-evolution-legend-item {
        display: flex;
        align-items: center;
        gap: 8px;

        white-space: nowrap;
    }

    .taste-evolution-legend-dot {
        width: 10px;
        height: 10px;
        border-radius: 999px;
    }

    </style>
    """, unsafe_allow_html=True)

    controls_col = st.container()

    with controls_col:

        controls_row = st.columns([0.1, 0.68, 0.55, 2.5])

        with controls_row[0]:
            st.empty()

        # LEFT — timeline pills
        with controls_row[1]:

            st.markdown("""
            <div style="padding-left: 600px;">
            """, unsafe_allow_html=True)

            timeline_mode = st.pills(
                label="Timeline mode",
                options=["Full timeline", "Aligned"],
                selection_mode="single",
                default="Aligned"
            )

            st.markdown("</div>", unsafe_allow_html=True)

        # CENTER — legend
        with controls_row[3]:

            st.markdown(
                '<div style="margin-top: 14px;"></div>',
                unsafe_allow_html=True
            )

            legend_html = """
            <div class="taste-evolution-legend-inline">
            """

            for genre, color in GENRE_COLORS.items():

                legend_html += f"""
                <div class="taste-evolution-legend-item">

                    <div
                        class="taste-evolution-legend-dot"
                        style="background:{color};"
                    ></div>

                    <span>{genre}</span>

                </div>
                """

            legend_html += "</div>"

            st.html(legend_html)

        # RIGHT — selectbox
        with controls_row[2]:

            st.markdown(
                '<div style="margin-top: 14px;"></div>',
                unsafe_allow_html=True
            )

            selected_genre = st.selectbox(
                "Choose genre",
                ["All"] + list(GENRE_COLORS.keys())
            )

    users = df["user"].unique()
    for user in users:

        chart_col, label_col = st.columns([8, 1.2], gap="small")

        with chart_col:

            monthly = prepare_genre_evolution(
                df=df,
                user=user,
                timeline_mode=timeline_mode,
                selected_genre=selected_genre
            )

            render_genre_evolution_chart(monthly, selected_genre)

        with label_col:
            st.html(
                f"""
                <div
                    class="taste-evolution-card"
                    style="
                        box-shadow:
                            0 0 8px {USER_COLORS[user]}40,
                            0 0 18px {USER_COLORS[user]}22;

                        border:1.5px solid {USER_COLORS[user]}25;
                    "
                >

                    <div
                        class="taste-evolution-name"
                        style="color:{USER_COLORS[user]};"
                    >
                        {user}
                    </div>

                    <div class="taste-evolution-archetype">
                        {ARCHETYPES[user]}
                    </div>

                </div>
                """
            )