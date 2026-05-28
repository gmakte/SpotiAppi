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
    st.markdown(
        "### How has our taste evolved?"
    )

    controls_col, legend_col = st.columns([1, 5])

    with controls_col:

        timeline_mode = st.pills(
            label="Timeline mode",
            options=["Full timeline", "Aligned"],
            selection_mode="single",
            default="Aligned"
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
                timeline_mode=timeline_mode
            )

            render_genre_evolution_chart(monthly)

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