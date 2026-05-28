import plotly.graph_objects as go
import base64
from assets.palette import USER_COLORS


def hex_to_rgba(hex_color, alpha=0.60):

    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return f"rgba({r},{g},{b},{alpha})"

def load_icon(path):

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f"data:image/png;base64,{encoded}"


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

    podium_icons = [
        load_icon("assets/icons/second.png"),
        load_icon("assets/icons/first.png"),
        load_icon("assets/icons/third.png")
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(

            x=users,
            y=hours,

            text=[
                f"{h:,.0f}h"
                for h in hours
            ],

            textposition="outside",

            textfont=dict(
                size=20,
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

    for i, (user, hour) in enumerate(zip(users, hours)):

        fig.add_layout_image(

            dict(
                source=podium_icons[i],

                x=user,
                y=hour + max(hours) * 0.15,

                xref="x",
                yref="y",

                sizex=0.60,
                sizey=max(hours) * 0.11,

                xanchor="center",
                yanchor="middle",

                layer="above"
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
            showticklabels=False,

            range=[
                0,
                max(hours) * 1.28
            ]
        ),

        font=dict(
            color="white"
        )
    )

    return fig