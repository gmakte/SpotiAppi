import streamlit as st
import plotly.graph_objects as go

from services.clock_analysis import (compute_clock)
from charts.radial_clock import (create_clock_chart)
from services.mood_service import compute_hourly_mood_map


def render_clock(df):

    clock_data = compute_clock(df)

    fig = create_clock_chart(clock_data)

    USER_COLORS = {
        "Ashanti": "#4f6dff",
        "Gabi": "#FF8FD8",
        "Maribel": "#FF8A3D"
    }

    SILLY_INSIGHTS = {
        "Ashanti":
            "certified midnight overthinker.",

        "Gabi":
            "runs purely on dramatic energy.",

        "Maribel":
            "treats mornings like a movie montage."
    }

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

    st.markdown(
        """
<style>

.normalized-wrapper{
    position:relative;
    display:inline-block;
    margin-top:50px;
    margin-bottom:-8px;
}

.normalized-pill{
    padding:12px 22px;
    border-radius:18px;
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    font-size:15px;
    font-weight:700;
    color:#7CFF9E;
    cursor:help;
}

.normalized-tooltip{

    visibility:hidden;
    opacity:0;

    width:280px;

    background:#111;

    color:rgba(255,255,255,0.82);

    padding:10px 10px;

    border-radius:14px;

    border:1px solid rgba(255,255,255,0.08);

    position:absolute;

    z-index:999;

    top:120%;
    left:0;

    transition:0.2s;

    font-size:13px;
    line-height:1.5;
}

.normalized-wrapper:hover .normalized-tooltip{
    visibility:visible;
    opacity:1;
}

</style>

<div class="normalized-wrapper">

<div class="normalized-pill">
Normalized
</div>

<div class="normalized-tooltip">
Scaled by each person’s total listening time to reveal habit patterns.
</div>

</div>
""",
        unsafe_allow_html=True
    )

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
    <div style="
    font-size:28px;
    font-weight:800;
    color:white;
    margin-top:-120px;
    margin-bottom:8px;
    ">
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

            silly = SILLY_INSIGHTS[
                person["user"]
            ]

            with card_cols[idx]:

                st.markdown(
                    f"""
    <div style="
    padding-right:20px;
    ">

    <div style="
    display:flex;
    align-items:center;
    gap:12px;
    margin-bottom:2px;
    margin-top:-75px;
    ">

    <div style="
    width:18px;
    height:18px;
    border-radius:50%;
    background:{color};
    "></div>

    <div style="
    font-size:22px;
    font-weight:800;
    color:{color};
    ">
    {person["user"]} - {person["share"]}%
    </div>

    </div>

    <div style="
    font-size:15px;
    color:rgba(255,255,255,0.58);
    margin-bottom:14px;
    ">
    {person["minutes"]:,} total listening minutes
    </div>

    <div style="
    height:12px;
    width:100%;
    background:rgba(255,255,255,0.05);
    border-radius:999px;
    overflow:hidden;
    margin-bottom:28px;
    ">

    <div style="
    height:100%;
    width:{person["share"]}%;
    background:{color};
    border-radius:999px;
    ">
    </div>

    </div>
    </div>
    """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
    <div style="
    font-size:28px;
    font-weight:800;
    color:white;
    margin-top:0px;
    margin-bottom:8px;
    ">
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
            <div style="
            background:rgba(255,255,255,0.02);
            border:2px solid {color}40;
            box-shadow:0 0 50px {color}25;

            border-radius:26px;

            padding:12px 14px;

            min-height:150px;

            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;

            text-align:center;
            ">

            <div style="
            font-size:30px;
            font-weight:800;
            color:white;

            line-height:1.1;

            margin-bottom:5px;
            ">
            {person["peak_hour"]}:00 —
            {person["peak_end_hour"]}:00
            </div>

            <div style="
            font-size:17px;
            line-height:1.6;
            font-weight:600;

            color:{color};

            max-width:220px;
            ">
            {silly}
            </div>

            </div>
            """)

        # =====================================================
        # PROPORTIONAL VIEW
        # =====================================================

        st.markdown(
            """
<div style="
font-size:22px;
font-weight:800;
color:white;
margin-top:1px;
margin-bottom:4px;
">
Proportional view
</div>

<div style="
font-size:13px;
color:rgba(255,255,255,0.55);
margin-bottom:14px;
">
Normalized listening share per hour
</div>
""",
            unsafe_allow_html=True
        )

        hours = clock_data["hours"]

        users = [
            "Ashanti",
            "Gabi",
            "Maribel"
        ]

        normalized_map = {
            user: []
            for user in users
        }

        for hour in hours:

            hour_data = clock_data[
                "hourly_breakdown"
            ][hour]

            total = sum(
                hour_data.values()
            )

            for user in users:

                value = hour_data.get(
                    user,
                    0
                )

                normalized = (
                    value / total
                    if total > 0
                    else 0
                )

                normalized_map[user].append(
                    normalized
                )

        fig2 = go.Figure()

        for user in users:

            fig2.add_trace(

                go.Bar(

                    x=hours,

                    y=normalized_map[user],

                    marker_color=USER_COLORS[user],

                    hovertemplate=(

                        f"<b>{user}</b><br>"
                        "Hour: %{x}:00<br>"
                        "Normalized share: %{y:.0%}"
                        "<extra></extra>"
                    )
                )
            )

        fig2.update_layout(

            barmode="stack",

            height=150,

            margin=dict(
                l=0,
                r=0,
                t=0,
                b=0
            ),

            paper_bgcolor=
                "rgba(0,0,0,0)",

            plot_bgcolor=
                "rgba(0,0,0,0)",

            showlegend=False,

            bargap=0.08,

            xaxis=dict(

                tickmode="linear",

                tick0=0,

                dtick=1,

                color="rgba(255,255,255,0.75)",

                showgrid=False,

                zeroline=False
            ),

            yaxis=dict(

                visible=False,

                range=[0, 1],

                showgrid=False,

                zeroline=False
            )
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

        from assets.palette import MOOD_COLORS
        mood_map = compute_hourly_mood_map(df)

        st.html("""

        <div style="
            margin-top:10px;
        ">

            <div style="
                font-size:22px;
                font-weight:800;
                color:white;
                margin-bottom:4px;
            ">
                Mood map
            </div>

            <div style="
                color:rgba(255,255,255,0.5);
                font-size:15px;
                margin-bottom:-5px;
            ">
                Dominant mood across each hour of the day.
            </div>

        </div>

        """)

        # -----------------------------------
        # HOURS
        # -----------------------------------

        hours_header = """

        <div style="
            display:flex;
            gap:4px;
            margin-left:76px;
            margin-bottom:-10px;
        ">

        """

        for hour in range(24):

            hours_header += f"""

            <div style="
                width:28px;
                text-align:center;
                color:rgba(255,255,255,0.45);
                font-size:15px;
            ">
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

            <div style="
                display:flex;
                align-items:center;
                gap:4px;
            ">

                <div style="
                    width:72px;
                    color:white;
                    font-size:17px;
                    font-weight:700;
                ">
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
                    style="
                        width:28px;
                        height:28px;

                        border-radius:4px;

                        background:{color};

                        box-shadow:0 0 10px {color}22;
                    "
                ></div>

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