import streamlit as st

from services.clock_analysis import (
    compute_clock
)

from charts.radial_clock import (
    create_clock_chart
)


def render_clock(df):

    # ---------------------------------
    # TITLE
    # ---------------------------------

    st.title(
        "When do we listen?"
    )

    st.caption(
        "Normalized by total listening activity per user."
    )

    # ---------------------------------
    # DATA
    # ---------------------------------

    clock_data = compute_clock(df)

    fig = create_clock_chart(
        clock_data
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    col1, col2 = st.columns(
        [1.3, 1],
        gap="large"
    )

    # ---------------------------------
    # CLOCK
    # ---------------------------------

    with col1:

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        # ---------------------------------
        # LEGEND
        # ---------------------------------

        st.markdown(
        """
    <div style="
    display:flex;
    justify-content:center;
    margin-top:-10px;
    width:100%;
    ">

    <div style="
    display:flex;
    align-items:center;
    justify-content:center;
    gap:40px;
    padding:10px 22px;
    border-radius:16px;
    background:rgba(255,255,255,0.02);
    width:fit-content;
    ">

    <div style="
    display:flex;
    align-items:center;
    gap:8px;
    ">

    <div style="
    width:14px;
    height:14px;
    border-radius:50%;
    background:#4f6dff;
    "></div>

    <span style="
    color:white;
    font-size:16px;
    ">
    Ashanti
    </span>

    </div>

    <div style="
    display:flex;
    align-items:center;
    gap:8px;
    ">

    <div style="
    width:14px;
    height:14px;
    border-radius:50%;
    background:#FF8FD8;
    "></div>

    <span style="
    color:white;
    font-size:16px;
    ">
    Gabi
    </span>

    </div>

    <div style="
    display:flex;
    align-items:center;
    gap:8px;
    ">

    <div style="
    width:14px;
    height:14px;
    border-radius:50%;
    background:#FF8A3D;
    "></div>

    <span style="
    color:white;
    font-size:16px;
    ">
    Maribel
    </span>

    </div>

    </div>

    </div>
    """,
        unsafe_allow_html=True
    )

    # ---------------------------------
    # RIGHT PANEL
    # ---------------------------------

    with col2:

        st.markdown(
            "### Placeholder"
        )

        st.markdown(
            """
<div style="
height:420px;
border-radius:18px;
background:#111111;
border:1px solid rgba(255,255,255,0.06);
">
</div>
""",
            unsafe_allow_html=True
        )