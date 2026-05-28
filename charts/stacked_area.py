import plotly.graph_objects as go
import streamlit as st

from assets.palette import GENRE_COLORS
GENRE_ORDER = list(GENRE_COLORS.keys())

def render_genre_evolution_chart(monthly, selected_genre):

    fig = go.Figure()

    for genre in GENRE_ORDER:

        # skip missing genres safely
        if genre not in monthly.columns:
            continue

        is_active = (
            selected_genre == "All"
            or genre == selected_genre
        )

        fig.add_trace(
            go.Scatter(
                x=monthly.index,
                y=monthly[genre],

                mode="lines",

                name=genre,

                showlegend=False,

                stackgroup="one",

                line=dict(
                    width=1,
                    color="rgba(255,255,255,0.22)"
                ),

                line_shape="spline",
                line_smoothing=1.1,

                fillcolor=GENRE_COLORS[genre],

                opacity=1 if is_active else 0.08,

                hoverinfo=(
                    "skip"
                    if not is_active
                    else None
                ),

                hovertemplate=(
                    None
                    if not is_active
                    else
                    "<b>%{fullData.name}</b><br>"
                    "%{x|%b %Y}<br>"
                    "%{y:.1%}<extra></extra>"
                )
            )
        )

    fig.update_layout(

        showlegend = False,
        height=220,

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        hovermode="closest",

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        xaxis=dict(
            title="",

            showgrid=False,

            tickformat="%b %Y",

            tickfont=dict(size=11),

            color="rgba(255,255,255,0.7)"
        ),

        yaxis=dict(

            range=[0, 1],

            showticklabels=False,

            showgrid=False,

            zeroline=False,

            title="",

            showline=False
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )