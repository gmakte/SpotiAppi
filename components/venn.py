import streamlit as st

from services.overlap_service import (
    compute_song_overlaps
)

from services.shared_artists import (
    compute_shared_artists
)

from charts.venn_chart import (
    create_venn_chart
)


def render_venn(df):

    st.markdown("### 2. Which song do we listen together?")

    # ---------------------------------
    # USER SELECTION
    # ---------------------------------

    users = sorted(df["user"].dropna().unique())

    selected_users = st.multiselect(
        "Compare users",
        users,
        default=users[:3],
        max_selections=3,
        key="venn_users"
    )

    if len(selected_users) < 2:
        st.warning("Select at least 2 users.")
        return

    # ---------------------------------
    # FILTER DATA
    # ---------------------------------

    filtered_df = df[
        df["user"].isin(selected_users)
    ]

    # ---------------------------------
    # BUILD DATA
    # ---------------------------------

    overlap_data = compute_song_overlaps(
        filtered_df
    )

    shared_artists = compute_shared_artists(
        filtered_df
    )

    fig = create_venn_chart(
        overlap_data
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

            st.markdown(
                f"""
<div style="
padding:14px;
margin-bottom:12px;
border-radius:14px;
background:#151515;
border:1px solid rgba(255,255,255,0.05);
">

<div style="
font-size:18px;
font-weight:600;
color:white;
">
{row['master_metadata_album_artist_name']}
</div>

<div style="
margin-top:6px;
font-size:15px;
color:#B86BFF;
">
{row['score']:.2f}% shared taste
</div>

</div>
""",
                unsafe_allow_html=True
            )