import plotly.graph_objects as go


USER_COLORS = {

    "Ashanti": "#4f6dff",
    "Gabi": "#FF8FD8",
    "Maribel": "#FF8A3D"
}


def create_clock_chart(data):

    fig = go.Figure()

    # ---------------------------------
    # COLORS
    # ---------------------------------

    colors = []

    for user in data["dominant_users"]:

        if user is None:

            colors.append(
                "rgba(255,255,255,0.08)"
            )

        else:

            colors.append(
                USER_COLORS[user]
            )

    # ---------------------------------
    # CLOCK RING
    # ---------------------------------

    fig.add_trace(

        go.Barpolar(

            r=[0.28] * 24,

            base=[0.72] * 24,

            theta=[
                h * 15
                for h in data["hours"]
            ],

            width=[13.2] * 24,

            marker_color=colors,

            marker_line_color=
                "rgba(255,255,255,0.05)",

            marker_line_width=1.2,

            opacity=0.95,

            customdata=list(

                zip(

                    data["hours"],

                    data["dominant_users"],

                    data["dominant_real_minutes"]
                )
            ),

            hovertemplate=(

                "<b>%{customdata[1]}</b><br>"

                "Hour: %{customdata[0]}:00<br>"

                "Minutes: %{customdata[2]:,.0f}"

                "<extra></extra>"
            )
        )
    )

    # ---------------------------------
    # CENTER TEXT
    # ---------------------------------

    fig.add_annotation(

        x=0.5,
        y=0.49,

        text=(

            "<span style='font-size:15px;color:rgba(255,255,255,0.7)'>"
            "Peak time"
            "</span><br><br>"

            f"<span style='font-size:28px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_hour']}:00 - {data['end_hour']}:00"
            "</span><br><br>"

            f"<span style='font-size:24px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_user']}"
            "</span><br><br>"

            f"<span style='font-size:15px;color:rgba(255,255,255,0.55)'>"
            f"{data['peak_minutes']:,} listening minutes"
            "</span>"
        ),

        showarrow=False,

        font=dict(
            size=16,
            color="white"
        )
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    fig.update_layout(

        polar=dict(

            bgcolor="rgba(0,0,0,0)",

            radialaxis=dict(
                visible=False,
                range=[0, 1.02],
                showgrid=False,
                ticks=""
            ),

            angularaxis=dict(

                tickmode="array",

                tickvals=[
                    0,
                    45,
                    90,
                    135,
                    180,
                    225,
                    270,
                    315
                ],

                ticktext=[
                    "0",
                    "3",
                    "6",
                    "9",
                    "12",
                    "15",
                    "18",
                    "21"
                ],

                tickfont=dict(
                    size=16
                ),

                color="white",

                direction="clockwise",

                showline=False,
                showgrid=False,
                ticks="",

                rotation=90
            )
        ),

        showlegend=False,

        height=420,
        width=420,

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        paper_bgcolor=
            "rgba(0,0,0,0)",

        plot_bgcolor=
            "rgba(0,0,0,0)"
    )

    return fig