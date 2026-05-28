import streamlit as st
import json
import pandas as pd

from assets.palette import UI_COLORS

from charts.venn_chart import (
    create_venn_chart
)


def render_venn():

    st.html("""
        <div class="clock-section-header">

            <div class="taste-evolution-title-inline">

                <span class="taste-evolution-title">
                    Common Interests in Artists
                </span>

                <div class="taste-evolution-info-floating">

                    <span class="taste-evolution-info-icon">
                        i
                    </span>

                    <div class="taste-evolution-tooltip">
                        Explore musical overlaps across listener groups.
                    </div>

                </div>

            </div>

        </div>
    """)

    # ---------------------------------
    # USER SELECTION
    # ---------------------------------

    with open("data/user_overlaps.json") as f:
        overlaps = json.load(f)

    with open("data/shared_artists.json") as f:
        shared_data = json.load(f)

    users = ["Ashanti", "Gabi", "Maribel"]

    selected_users = st.pills(

        "Compare listeners",

        options=users,

        selection_mode="multi",

        default=users[:2]
    )

    if len(selected_users) < 2:
        st.warning("Select at least 2 users.")
        return

    selected_users = sorted(selected_users)

    overlap_data = next(

        overlap
        for overlap in overlaps
        if sorted(overlap["users"]) == selected_users
    )

    fig = create_venn_chart(
        overlap_data
    )

    match = next(
        x for x in shared_data
        if sorted(x["users"]) == sorted(selected_users)
    )

    shared_artists = pd.DataFrame(
        match["shared_artists"]
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    col1, col2 = st.columns([2, 1])

    # ---------------------------------
    # VENN
    # ---------------------------------

    with col1:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------------------------
    # SHARED ARTISTS
    # ---------------------------------

    with col2:

        st.markdown("#### Shared favorites")

        for _, row in shared_artists.iterrows():

            st.html(
                f"""
                <div style="
                padding:14px;
                margin-bottom:12px;
                border-radius:14px;
                background:{UI_COLORS["card"]};
                border:1px solid {UI_COLORS["border"]};
                ">

                <div style="
                font-size:18px;
                font-weight:600;
                color:{UI_COLORS["text_primary"]};
                ">
                {row['artist']}
                </div>
                """)