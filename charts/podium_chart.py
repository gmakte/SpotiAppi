import plotly.graph_objects as go
from assets.palette import USER_COLORS


def hex_to_rgba(hex_color, alpha=0.60):

    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return f"rgba({r},{g},{b},{alpha})"


def create_podium_chart(rankings):

    # ---------------------------------
    # ORDER FOR VISUAL PODIUM
    # ---------------------------------

    rankings = rankings.iloc[[1, 0, 2]]

    users = rankings["user"]
    hours = rankings["hours"]

    colors = [
        hex_to_rgba(
            USER_COLORS[user],
            0.60
        )

        for user in users
    ]

    border_colors = [
        hex_to_rgba(
            USER_COLORS[user],
            0.38
        )

        for user in users
    ]

    medals = [
        "🥈",
        "🥇",
        "🥉"
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(

            x=users,
            y=hours,

            text=[
                f"{m}<br>{h:,.0f}h"
                for m, h in zip(
                    medals,
                    hours
                )
            ],

            textposition="outside",

            textfont=dict(
                size=22,
                color="white"
            ),

            marker=dict(
                color=colors,
                line=dict(
                    color=border_colors,
                    width=3
                )
            ),

            width=0.55,

            hovertemplate=(
                "<b>%{x}</b><br>"
                "%{y:,.0f} listening hours"
                "<extra></extra>"
            )
        )
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    fig.update_layout(

        height=500,

        paper_bgcolor=
        "rgba(0,0,0,0)",

        plot_bgcolor=
        "rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        showlegend=False,

        xaxis=dict(
            showgrid=False,
            zeroline=False,

            tickfont=dict(
                size=18,
                color="white"
            )
        ),

        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),

        font=dict(
            color="white"
        )
    )

    return fig