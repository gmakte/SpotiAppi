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
        [0.95, 0.95],
        gap="small"
    )

    # ---------------------------------
    # LEFT SIDE
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
margin-top:-6px;
margin-bottom:0px;
width:100%;
">

<div style="
display:flex;
justify-content:center;
align-items:center;
gap:24px;
padding:12px 22px;
border-radius:20px;
background:rgba(255,255,255,0.02);
border:1px solid rgba(255,255,255,0.04);
">

<!-- ITEM -->

<div style="
width:110px;
display:flex;
justify-content:center;
align-items:center;
gap:10px;
">

<div style="
width:15px;
height:15px;
border-radius:50%;
background:#4f6dff;
flex-shrink:0;
"></div>

<span style="
color:white;
font-size:17px;
line-height:1;
">
Ashanti
</span>

</div>

<!-- ITEM -->

<div style="
width:110px;
display:flex;
justify-content:center;
align-items:center;
gap:10px;
">

<div style="
width:15px;
height:15px;
border-radius:50%;
background:#FF8FD8;
flex-shrink:0;
"></div>

<span style="
color:white;
font-size:17px;
line-height:1;
">
Gabi
</span>

</div>

<!-- ITEM -->

<div style="
width:110px;
display:flex;
justify-content:center;
align-items:center;
gap:10px;
">

<div style="
width:15px;
height:15px;
border-radius:50%;
background:#FF8A3D;
flex-shrink:0;
"></div>

<span style="
color:white;
font-size:17px;
line-height:1;
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
    # RIGHT SIDE
    # ---------------------------------

    with col2:

        share_data = sorted(

            clock_data[
                "listening_share"
            ],

            key=lambda x:
                x["share"],

            reverse=True
        )

        USER_COLORS = {

            "Ashanti": "#4f6dff",
            "Gabi": "#FF8FD8",
            "Maribel": "#FF8A3D"
        }

        # ---------------------------------
        # INSIGHTS
        # ---------------------------------

        SILLY_INSIGHTS = {

            "Ashanti":
                "certified midnight overthinker.",

            "Gabi":
                "runs purely on dramatic energy.",

            "Maribel":
                "treats mornings like a movie montage."
        }

        html = """

<div style="
padding:22px;
margin-top:-34px;
margin-left:-36px;
border-radius:24px;
background:rgba(255,255,255,0.02);
border:1px solid rgba(255,255,255,0.06);
max-width:720px;
">

<div style="
font-size:24px;
font-weight:700;
color:white;
margin-bottom:26px;
line-height:1;
">
Listening personality overview
</div>

"""

        # ---------------------------------
        # USER BLOCKS
        # ---------------------------------

        for person in share_data:

            color = USER_COLORS[
                person["user"]
            ]

            silly_text = SILLY_INSIGHTS[
                person["user"]
            ]

            html += f"""

<div style="
margin-bottom:28px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:flex-start;
gap:16px;
">

<!-- LEFT -->

<div style="
flex:1;
min-width:0;
">

<!-- NAME -->

<div style="
display:flex;
align-items:center;
gap:10px;
margin-bottom:8px;
">

<div style="
width:16px;
height:16px;
border-radius:50%;
background:{color};
flex-shrink:0;
"></div>

<div style="
font-size:18px;
font-weight:700;
color:{color};
line-height:1;
">
{person["user"]}
</div>

<div style="
font-size:18px;
font-weight:700;
color:{color};
line-height:1;
">
{person["share"]}%
</div>

</div>

<!-- MINUTES -->

<div style="
font-size:13px;
color:rgba(255,255,255,0.55);
margin-left:26px;
margin-bottom:12px;
">
{person["minutes"]:,} min total listening
</div>

<!-- BAR -->

<div style="
height:10px;
width:70%;
border-radius:999px;
background:rgba(255,255,255,0.05);
overflow:hidden;
margin-left:26px;
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

<!-- RIGHT CARD -->

<div style="
width:120px;
min-width:120px;
padding:10px 12px;
border-radius:14px;
background:rgba(255,255,255,0.025);
border:1px solid rgba(255,255,255,0.04);
text-align:right;
">

<div style="
font-size:10px;
letter-spacing:1px;
text-transform:uppercase;
color:rgba(255,255,255,0.35);
margin-bottom:8px;
">
Peak window
</div>

<div style="
font-size:14px;
font-weight:700;
color:white;
margin-bottom:12px;
line-height:1.2;
">
{person["peak_hour"]}:00 — {person["peak_end_hour"]}:00
</div>

<div style="
font-size:13px;
font-weight:500;
color:{color};
line-height:1.45;
">
{silly_text}
</div>

</div>

</div>

</div>

"""

        html += "</div>"

        st.markdown(
            html,
            unsafe_allow_html=True
        )