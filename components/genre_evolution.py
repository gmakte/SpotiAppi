import streamlit as st

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

def render_taste_evolution(df):
    st.html("""
    <div class="taste-evolution-title-inline">

        <span class="taste-evolution-title">
            How has our taste evolved?
        </span>

        <span class="taste-evolution-info-floating">
            ⓘ

            <div class="taste-evolution-tooltip">
                Streamgraphs show the relative share of genres listened to over time.<br><br>

                • Full timeline: full Spotify history<br>
                • Aligned: same comparison period for everyone<br><br>

                Use “Choose genre” to isolate one genre on a shared baseline.
            </div>

        </span>

    </div>
    """)

    controls_col, legend_col = st.columns([1.8, 4.2])

    with controls_col:

        pills_col, genre_col = st.columns([2, 1])

        with pills_col:

            timeline_mode = st.pills(
                label="Timeline mode",
                options=["Full timeline", "Aligned"],
                selection_mode="single",
                default="Aligned"
            )

        with genre_col:

            selected_genre = st.selectbox(
                "Choose genre",
                ["All"] + list(GENRE_COLORS.keys())
            )

    # shared legend
    legend_html = """
    <div class="taste-evolution-legend">
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

    with legend_col:
        st.html(legend_html)


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