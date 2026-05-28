import plotly.graph_objects as go

from assets.palette import USER_COLORS


def create_proportional_chart(
    normalized_map,
    hours
):

    fig = go.Figure()

    for user, values in normalized_map.items():

        fig.add_trace(

            go.Bar(

                x=hours,

                y=values,

                marker_color=USER_COLORS[user],

                hovertemplate=(

                    f"<b>{user}</b><br>"
                    "Hour: %{x}:00<br>"
                    "Normalized share: %{y:.0%}"
                    "<extra></extra>"
                )
            )
        )

    fig.update_layout(

        barmode="stack",

        height=150,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        paper_bgcolor=
            "rgba(0,0,0,0)",

        plot_bgcolor=
            "rgba(0,0,0,0)",

        showlegend=False,

        bargap=0.08,

        xaxis=dict(

            tickmode="linear",

            tick0=0,

            dtick=1,

            color="rgba(255,255,255,0.75)",

            showgrid=False,

            zeroline=False
        ),

        yaxis=dict(

            visible=False,

            range=[0, 1],

            showgrid=False,

            zeroline=False
        )
    )

    return fig