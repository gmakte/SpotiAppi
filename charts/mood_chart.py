import base64

import plotly.graph_objects as go

from assets.palette import (
    MOOD_COLORS,
    MOOD_ICONS)


def hex_to_rgb(hex_color):

    hex_color = hex_color.lstrip("#")

    return tuple(

        int(
            hex_color[i:i+2],
            16
        )

        for i in (0, 2, 4)
    )

def get_base64_image(path):

    with open(path, "rb") as img_file:

        return base64.b64encode(
            img_file.read()
        ).decode()


def create_mood_chart(mood_df):

    # ---------------------------------
    # ORDER
    # ---------------------------------

    preferred_order = [

        "Happy",
        "Energetic",
        "Calm",
        "Dreamy",
        "Dark",
        "Melancholic"
    ]

    mood_order = [

        mood
        for mood in preferred_order

        if mood in mood_df["mood"].unique()
    ]

    users = list(
        mood_df["user"].unique()
    )

    fig = go.Figure()

    # ---------------------------------
    # DRAW CELLS
    # ---------------------------------

    for row_i, user in enumerate(users):

        max_percentage = (

            mood_df[
                mood_df["user"] == user
            ]["percentage"]

            .max()
        )

        for col_i, mood in enumerate(mood_order):

            subset = mood_df[

                (mood_df["user"] == user)
                &
                (mood_df["mood"] == mood)
            ]

            if len(subset) > 0:

                percentage = (
                    subset[
                        "percentage"
                    ].iloc[0]
                )

            else:

                percentage = 0

            # ---------------------------------
            # STRONGER CONTRAST
            # ---------------------------------

            normalized = percentage / 100

            opacity = (
                normalized ** 0.90
            ) * 0.92 + 0.03

            r, g, b = hex_to_rgb(
                MOOD_COLORS[mood.lower()]
            )

            fill = (
                f"rgba({r}, {g}, {b}, "
                f"{float(opacity)})"
            )

            # ---------------------------------
            # CELL
            # ---------------------------------

            fig.add_shape(

                type="rect",

                x0=col_i + 0.03,
                x1=col_i + 0.97,

                y0=row_i + 0.03,
                y1=row_i + 0.97,

                fillcolor=fill,

                line=dict(

                    width=2 if percentage == max_percentage else 1,

                    color=(

                        "rgba(255,255,255,0.45)"

                        if percentage == max_percentage

                        else "rgba(255,255,255,0.03)"
                    )
                )
            )

            # ---------------------------------
            # MAIN TEXT
            # ---------------------------------

            fig.add_annotation(

                x=col_i + 0.5,
                y=row_i + 0.5,

                text=f"{percentage:.0f}%",

                showarrow=False,

                font=dict(

                    size=18,

                    color="white"
                )
            )

    # ---------------------------------
    # ICONS + LABELS
    # ---------------------------------

    for mood in mood_order:

        icon_base64 = get_base64_image(
            MOOD_ICONS[mood]
        )

        x_pos = (
            mood_order.index(mood)
            + 0.5
        )

        fig.add_layout_image(

            dict(

                source=f"data:image/png;base64,{icon_base64}",

                xref="x",

                yref="paper",

                x=x_pos,

                y=1.08,

                sizex=0.16,

                sizey=0.16,

                xanchor="center",

                yanchor="middle",

                layer="above"
            )
        )

        fig.add_annotation(

            x=x_pos,

            y=1.01,

            xref="x",

            yref="paper",

            text=mood,

            showarrow=False,

            font=dict(

                size=12,

                color="rgba(255,255,255,0.70)"
            )
        )

    fig.update_xaxes(

        tickmode="array",

        showticklabels=False,

        tickvals=[
            i + 0.5
            for i in range(
                len(mood_order)
            )
        ],

        side="top",

        showgrid=False,
        zeroline=False,

        tickfont=dict(
            size=20
        ),

        range=[0, len(mood_order)]
    )

    # ---------------------------------
    # Y LABELS
    # ---------------------------------

    fig.update_yaxes(

        tickmode="array",

        tickvals=[
            i + 0.5
            for i in range(
                len(users)
            )
        ],

        ticktext=users,

        autorange="reversed",

        showgrid=False,
        zeroline=False,

        tickfont=dict(
            size=18
        ),

        range=[0, len(users)]
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    fig.update_layout(

        height=360,

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

        font=dict(
            color="white"
        )
    )

    return fig