import streamlit as st

from services.clock_analysis import (compute_clock,compute_normalized_share)
from charts.radial_clock import (create_clock_chart)
from services.mood_service import compute_hourly_mood_map
from assets.palette import (USER_COLORS,MOOD_COLORS)
from assets.text import SILLY_INSIGHTS
from charts.proportional_chart import (create_proportional_chart)


def render_clock(df):

    clock_data = compute_clock(df)

    fig = create_clock_chart(clock_data)

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown(
        """
    <h1 style="
    margin-bottom:-38px;
    padding-bottom:0;
    ">
    When do we listen?
    </h1>
    """,
        unsafe_allow_html=True
    )

    st.html(
        """
    <div class="clock-pill-wrapper">

        <div class="clock-pill">
        Normalized
        </div>

        <div class="clock-tooltip">
        Scaled by each person’s total listening time to reveal habit patterns.
        </div>

    </div>
    """)

    # =====================================================
    # GLOBAL SPACING
    # =====================================================

    st.markdown(
        """
    <style>

    div[data-testid="column"] {
        padding-top: 0rem !important;
    }

    .block-container {
        padding-top: 1.2rem !important;
    }

    </style>
    """,
        unsafe_allow_html=True
    )

    left_col, right_col = st.columns(
        [0.70, 1.30],
        gap="small"
    )

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left_col:

        fig.update_layout(

            height=430,
            width=430,

            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),

            polar=dict(

                radialaxis=dict(
                    visible=False,
                    range=[0, 0.87]
                ),

                angularaxis=dict(

                    tickmode="array",

                    tickvals=[
                        0,
                        45,
                        90,
                        135,
                        180,
                        225,
                        270,
                        315
                    ],

                    ticktext=[
                        "0",
                        "3",
                        "6",
                        "9",
                        "12",
                        "15",
                        "18",
                        "21"
                    ],

                    tickfont=dict(
                        size=14,
                        color="white"
                    ),

                    ticks="",

                    rotation=90,

                    direction="clockwise"
                )
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=False,
            config={
                "displayModeBar": False
            }
        )

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right_col:

        share_data = sorted(
            clock_data["listening_share"],
            key=lambda x: x["share"],
            reverse=True
        )

        st.markdown(
            """
        <div class="section-title"
        style="margin-top:-120px;">
        Listening personality overview
        </div>
        """,
            unsafe_allow_html=True
        )

        card_cols = st.columns(3)

        for idx, person in enumerate(share_data):

            color = USER_COLORS[
                person["user"]
            ]

            with card_cols[idx]:

                st.markdown(
                    f"""
    <div class="personality-card">

    <div class="personality-row"
    style="margin-top:-75px;">

    <div class="personality-dot"
    style="background:{color};">
    </div>

    <div class="personality-name"
    style="color:{color};">

    {person["user"]} - {person["share"]}%
    </div>

    </div>

    <div class="personality-minutes">
    {person["minutes"]:,} total listening minutes
    </div>

    <div class="personality-bar">

    <div class="personality-bar-fill"
    style="
    width:{person['share']}%;
    background:{color};
    ">
    </div>

    </div>
    </div>
    """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
        <div class="section-title">
        Peak windows
        </div>
        """,
            unsafe_allow_html=True
        )
        
        peak_cols = st.columns(3)
        
        for idx, person in enumerate(share_data):

            color = USER_COLORS[
                person["user"]
            ]

            silly = SILLY_INSIGHTS[
                person["user"]
            ]

            with peak_cols[idx]:

                st.html(
                    f"""
            <div class="peak-window-card"
            style="
            border:2px solid {color}40;
            box-shadow:0 0 50px {color}25;
            ">

            <div class="peak-window-time">

            {person["peak_hour"]}:00 —
            {person["peak_end_hour"]}:00
            </div>

            <div class="peak-window-text"
            style="color:{color};">

            {silly}
            </div>

            </div>
            """)

        # =====================================================
        # PROPORTIONAL VIEW
        # =====================================================

        st.markdown(
            """
        <div class="section-title">
        Proportional view
        </div>

        <div class="section-subtitle">
        Normalized listening share per hour
        </div>
        """,
            unsafe_allow_html=True
        )

        hours = clock_data["hours"]

        normalized_map = compute_normalized_share(clock_data)

        fig2 = create_proportional_chart(
            normalized_map,
            hours
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        # -----------------------------------
        # MOOD MAP
        # -----------------------------------

        mood_map = compute_hourly_mood_map(df)

        st.markdown(
            """
        <div class="section-title">
        Mood map
        </div>

        <div class="section-subtitle"
        style="margin-bottom:-5px;">
        Dominant mood across each hour of the day.
        </div>
        """,
            unsafe_allow_html=True
        )

        # -----------------------------------
        # HOURS
        # -----------------------------------

        hours_header = """

        <div class="mood-map-hours">

        """

        for hour in range(24):

            hours_header += f"""

            <div class="mood-map-hour">
                {hour}
            </div>

            """

        hours_header += "</div>"

        st.html(hours_header)

        # -----------------------------------
        # USER ROWS
        # -----------------------------------

        for person, moods in mood_map.items():

            row = f"""

            <div class="mood-map-row">
                <div class="mood-map-name">
                    {person}
                </div>

            """

            for mood in moods:

                mood_key = mood.lower()

                color = MOOD_COLORS.get(
                    mood_key,
                    "#444444"
                )

                row += f"""

                <div
                title="{mood}"
                class="mood-map-cell"
                style="
                    background:{color};
                    box-shadow:0 0 10px {color}22;
                "
                >
                </div>

                """

            row += "</div>"

            st.html(row,)

        st.html("""

        <div class="mood-legend">

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#4f6dff;"></div>

                <div class="mood-legend-text">
                Melancholic
                </div>
            </div>

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#9B2242;"></div>

                <div class="mood-legend-text">
                Dark
                </div>
            </div>

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#FF8FD8;"></div>

                <div class="mood-legend-text">
                Dreamy
                </div>
            </div>

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#6FAF98;"></div>

                <div class="mood-legend-text">
                Calm
                </div>
            </div>

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#FF8A3D;"></div>

                <div class="mood-legend-text">
                Energetic
                </div>
            </div>

            <div class="mood-legend-item">
                <div class="mood-legend-dot"
                style="background:#FFD166;"></div>

                <div class="mood-legend-text">
                Happy
                </div>
            </div>

        </div>

        """)