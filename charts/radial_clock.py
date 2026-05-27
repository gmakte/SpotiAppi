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

            r=[0.30] * 24,

            base=[0.50] * 24,

            theta=[
                h * 15
                for h in data["hours"]
            ],

            width=[13] * 24,

            marker_color=colors,

            marker_line_color=
                "rgba(255,255,255,0.04)",

            marker_line_width=1,

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
        y=0.5,

        text=(

            "<span style='font-size:12px;color:rgba(255,255,255,0.65)'>"
            "Peak time"
            "</span><br><br>"

            f"<span style='font-size:28px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_hour']}:00 - {data['end_hour']}:00"
            "</span><br><br>"

            f"<span style='font-size:20px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_user']}"
            "</span><br><br>"

            f"<span style='font-size:14px;color:rgba(255,255,255,0.5)'>"
            f"{data['peak_minutes']:,} listening minutes"
            "</span>"
        ),

        showarrow=False,

        font=dict(
            size=14,
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
                range=[0, 0.96],
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
                    size=9,
                    color="white"
                ),

                ticklabelstep=1,

                color="white",
                # layer="below traces",

                direction="clockwise",

                showline=False,
                showgrid=False,
                ticks="",

                rotation=90
            )
        ),

        showlegend=False,

        height=260,
        width=260,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        paper_bgcolor=
            "rgba(0,0,0,0)",

        plot_bgcolor=
            "rgba(0,0,0,0)"
    )

    return fig