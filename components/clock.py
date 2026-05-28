import streamlit as st
import json

from charts.radial_clock import (create_clock_chart)
from services.mood_service import compute_hourly_mood_map
from assets.palette import (USER_COLORS,MOOD_COLORS)
from assets.text import SILLY_INSIGHTS
from charts.proportional_chart import (create_proportional_chart)

def render_clock():

    with open("data/clock_insights.json") as f:
        clock_data = json.load(f)

    # =====================================================
    # TITLE
    # =====================================================

    st.html("""
        <div class="clock-section-header">

            <div class="taste-evolution-title-inline"
            style="margin-bottom:5px;">

                <span class="taste-evolution-title">
                    24h Listening Clock
                </span>

                <div class="taste-evolution-info-floating">
                    <span class="taste-evolution-info-icon">i</span>

                    <div class="taste-evolution-tooltip">
                        Hours are normalized by each person’s total listening, highlighting who most owns each moment of the day.
                    </div>
                </div>

            </div>

        </div>
    """)


    fig = create_clock_chart(clock_data)

    # =====================================================
    # GLOBAL SPACING
    # =====================================================

    st.markdown(
        """
    <style>

    .clock-info-icon {
        position: relative;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 18px;
        height: 18px;
        border-radius: 999px;
        border:1px solid {UI_COLORS["border_soft"]};
        color:{UI_COLORS["text_primary"]};;
        font-size: 12px;
        font-weight: 700;
        line-height: 1;
        cursor: help;
        flex-shrink: 0;
    }

    .clock-info-tooltip {
        position: absolute;
        left: 50%;
        top: 26px;
        transform: translateX(-50%);
        width: 250px;
        padding: 8px 10px;
        border-radius: 10px;
        background:{UI_COLORS["tooltip"]};
        border:1px solid {UI_COLORS["border_soft"]};
        color: rgba(255,255,255,0.92);
        font-size: 12px;
        font-weight: 500;
        line-height: 1.35;
        box-shadow: 0 12px 28px rgba(0,0,0,0.28);
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
        z-index: 50;
    }

    .clock-info-icon:hover .clock-info-tooltip {
        opacity: 1;
        visibility: visible;
    }

    /* remove extra top padding on columns and overall page */
    div[data-testid="column"] {
        padding-top: 0rem !important;
    }

    /* reduce global top padding so title/selector sit closer to the chart */
    .block-container {
        padding-top: 0.45rem !important;
    }

    /* remove extra top margin Streamlit may add before plotly charts */
    div[data-testid="stPlotlyChart"] {
        margin-top: 0rem !important;
        padding-top: 0rem !important;
    }

    </style>
    """,
        unsafe_allow_html=True
    )

    left_col, right_col = st.columns(
        [0.78, 1.22],
        gap="small"
    )

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left_col:

        fig.update_layout(

            height=520,
            width=520,

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
            key=lambda x: x["user"]
        )

        st.markdown(
            """
        <div class="section-title">
        Peak windows
        </div>
        """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            '<div class="peak-windows-row">',
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
            font-size:24px;
            font-weight:800;
            color:{color};
            text-align:center;
            margin-bottom:4px;
            letter-spacing:0.2px;
            ">
            {person["user"]}
            </div>        

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
            <div style="height:8px;"></div>
            {silly}
            </div>

            </div>
            """)
                
        # =====================================================
        # PROPORTIONAL VIEW
        # =====================================================

        st.markdown(
            """
        <div style="height:16px;"></div>
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


        with open("data/normalized_clock_share.json") as f:
            normalized_map = json.load(f)

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
    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )