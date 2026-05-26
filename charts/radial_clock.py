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

        r=[0.28] * 48,
        base=[0.72] * 48,

        theta=[
            s * 7.5
            for s in data["slots"]
        ],

        width=[7.2] * 48,

        marker_color=colors,

        marker_line_color=
            "rgba(0,0,0,0)",

        marker_line_width=1,

        opacity=0.95,

        customdata=[

            (
                s,
                data["dominant_users"][i],
                data["dominant_real_minutes"][i],
                f"{s//2:02d}:{'00' if s % 2 == 0 else '30'}"
            )

            for i, s in enumerate(data["slots"])
        ],

        hovertemplate=(

            "<b>%{customdata[1]}</b><br>"

            "Time: %{customdata[3]}<br>"

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

            "<span style='font-size:16px;color:rgba(255,255,255,0.7)'>"
            "Peak time"
            "</span><br><br>"

            f"<span style='font-size:28px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_hour']}:{data['peak_minute']} - {data['end_hour']}:{data['end_minute']}"            "</span><br>"

            f"<span style='font-size:24px;color:{USER_COLORS[data['peak_user']]};font-weight:700'>"
            f"{data['peak_user']}"
            "</span><br>"

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
                range=[0, 1.05],
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