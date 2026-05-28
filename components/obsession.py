import streamlit as st
import pandas as pd


from charts.obsession_chart import (
    create_obsession_chart
)

from assets.palette import (
    USER_COLORS,
    UI_COLORS
)

def render_obsession():

    metrics = pd.read_csv("data/obsession_metrics.csv")

    fig = create_obsession_chart(metrics)

    st.html("""
    <div class="taste-evolution-title-inline">

        <span class="taste-evolution-title">
            Obsessive behavior analysis
        </span>

        <div class="taste-evolution-info-floating">
            <span class="taste-evolution-info-icon">i</span>

            <div class="taste-evolution-tooltip">
                <strong>Replay intensity</strong>: average number of plays per unique song for a listener.<br><br> 
                <strong>Skip rate</strong>: proportion of skipped streams out of total streams for a listener.
            </div>
        </div>

    </div>
    """)

    # tooltip CSS for obsession info
    st.markdown(
        """
    <style>
    .obsession-info-icon {
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
        margin-left:4px;
    }

    .obsession-info-tooltip {
        position: absolute;
        left: 50%;
        top: 26px;
        transform: translateX(-50%);
        width: 300px;
        padding: 10px 12px;
        border-radius: 10px;
        background: rgba(14, 18, 28, 0.96);
        border: 1px solid rgba(255,255,255,0.12);
        color: rgba(255,255,255,0.92);
        font-size: 13px;
        font-weight: 500;
        line-height: 1.35;
        box-shadow: 0 12px 28px rgba(0,0,0,0.28);
        opacity: 0;
        visibility: hidden;
        pointer-events: none;
        z-index: 50;
    }

    .obsession-info-icon:hover .obsession-info-tooltip {
        opacity: 1;
        visibility: visible;
    }
    </style>
    """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([2.8, 1])

    # ---------------------------------
    # CHART
    # ---------------------------------

    with col1:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------
    # RIGHT SIDE CARDS
    # ---------------------------------

    with col2:

        personality_map = {

            "Ashanti": {
                "label": "Comfort Zone",
                "quote": "Never leaves her comfort zone, even if the song is bad"
            },

            "Gabi": {
                "label": "Commitment Issues",
                "quote": "Always looking for the next best thing, can't commit to a song"
            },

            "Maribel": {
                "label": "Short Attention Span",
                "quote": "Clearly a victim of the modern streaming era, skips songs like swiping on Tinder"
            }
        }

        for i, row in metrics.iterrows():

            archetype = personality_map[
                row["user"]
            ]["label"]

            subtitle = personality_map[
                row["user"]
            ]["quote"]

            # ---------------------------------
            # CARD
            # ---------------------------------

            st.markdown(
                f"""
<div style="
padding:18px;
margin-bottom:18px;
border-radius:18px;
background:{UI_COLORS["card"]};
border:1px solid {UI_COLORS["border"]};
">

<div style="
font-size:26px;
font-weight:700;
color:{USER_COLORS[row['user']]};
margin-bottom:10px;
">
{row['user']}
</div>

<div style="
font-size:18px;
font-weight:600;
color:{UI_COLORS["text_primary"]};
margin-bottom:4px;
">
{archetype}
</div>

<div style="
font-size:14px;
font-style:italic;
color:{UI_COLORS["text_secondary"]};
margin-bottom:10px;
line-height:1.4;
">
“{subtitle}”
</div>

</div>
""",
                unsafe_allow_html=True
            )