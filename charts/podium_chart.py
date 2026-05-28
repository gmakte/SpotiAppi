import plotly.graph_objects as go


def create_podium_chart(rankings):

    # ---------------------------------
    # ORDER FOR VISUAL PODIUM
    # ---------------------------------

    rankings = rankings.iloc[[1, 0, 2]]

    users = rankings["user"]
    hours = rankings["hours"]

    colors = [
        "rgba(79,109,255,0.60)",
        "rgba(255,143,216,0.60)",
        "rgba(255,138,61,0.60)"
    ]

    border_colors = [
        "rgba(79,109,255,0.38)",
        "rgba(255,143,216,0.38)",
        "rgba(255,138,61,0.38)"
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

            width=0.55
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