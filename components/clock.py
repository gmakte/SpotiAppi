import streamlit as st

from services.clock_analysis import compute_clock
from charts.radial_clock import (create_clock_chart)
from assets.palette import USER_COLORS


def render_clock(df):

    clock_data = compute_clock(df)

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown(
        """
    <div style="
        display:flex;
        align-items:center;
        gap:8px;
        margin-bottom:8px;
        padding-bottom:0;
    ">
        <div style="
            font-size:24px;
            line-height:1;
            font-weight:700;
            color:#ffffff;
        ">
            24h Listening Clock
        </div>
        <span class="clock-info-icon">
            i
            <span class="clock-info-tooltip">These are normalized dominant hours: each hour is weighted by a user's share of listening, so the ring shows who leads after normalization.</span>
        </span>
    </div>
    """,
        unsafe_allow_html=True
    )

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
        border: 1px solid rgba(255,255,255,0.45);
        color: rgba(255,255,255,0.9);
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
        background: rgba(14, 18, 28, 0.96);
        border: 1px solid rgba(255,255,255,0.12);
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
        [0.82, 0.68],
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

    with right_col:

        st.markdown(
            """
            <div style="
                display:flex;
                flex-direction:column;
                gap:10px;
                padding-top:22px;
            ">
            """,
            unsafe_allow_html=True
        )

        # Render a vertical timeline with circular badges (no moods or percentages)
        st.markdown(
            """
            <div style="position:relative;padding-left:36px;padding-top:8px;">
            """,
            unsafe_allow_html=True
        )

        for i, item in enumerate(clock_data.get("listening_share", [])):

            user = item.get("user", "")
            peak_hour = item.get("peak_hour")
            peak_end_hour = item.get("peak_end_hour")
            color = USER_COLORS.get(user, "#ffffff")

            # compute left offset and width as percentages for a 24-hour bar
            if peak_hour is None:
                left_pct = 0
                width_pct = 0
            else:
                start = int(peak_hour) % 24
                end = int(peak_end_hour) % 24
                span = (end - start) % 24
                if span == 0:
                    span = 24
                left_pct = (start / 24) * 100
                width_pct = (span / 24) * 100

            st.markdown(
                f"""
                <div style="position:relative; margin-bottom:18px; display:flex; gap:12px; align-items:center;">
                    <div style="width:140px;">
                        <div style="font-size:14px; font-weight:700; color:#ffffff;">{user}</div>
                        <div style="font-size:13px; color:rgba(255,255,255,0.9); font-weight:700;">{peak_hour}:00 - {peak_end_hour}:00</div>
                    </div>
                    <div style="flex:1; height:18px; background:rgba(255,255,255,0.06); border-radius:10px; position:relative; overflow:hidden;">
                        <div style="position:absolute; left:{left_pct}%; top:0; height:100%; width:{width_pct}%; background:{color}; border-radius:8px; box-shadow:inset 0 -6px 18px rgba(0,0,0,0.24);"></div>
                        <div style="position:absolute; left:0; top:50%; transform:translateY(-50%); width:100%; display:flex; justify-content:space-between; padding:0 6px; font-size:10px; color:rgba(255,255,255,0.38);">
                            <div>{0}</div>
                            <div>24</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)