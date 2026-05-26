import streamlit as st

from services.clock_analysis import (
    compute_clock
)

from charts.radial_clock import (
    create_clock_chart
)


def render_clock(df):

    st.markdown(
        "## When do we listen?"
    )

    # ---------------------------------
    # DATA
    # ---------------------------------

    clock_data = compute_clock(df)

    fig = create_clock_chart(
        clock_data
    )

    # ---------------------------------
    # CLOCK
    # ---------------------------------

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------------------------
    # LEGEND
    # ---------------------------------

    st.markdown(
        """
<div style="
display:flex;
justify-content:center;
align-items:center;
gap:70px;
margin-top:-10px;
margin-bottom:20px;
width:100%;
">

<div style="
display:flex;
align-items:center;
gap:10px;
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
gap:10px;
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
gap:10px;
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
""",
        unsafe_allow_html=True
    )