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
        "Melancholic",
        "Dreamy",
        "Dark"
    ]

    mood_order = [

        mood
        for mood in preferred_order

        if mood in mood_df["mood"].unique()
    ]

    users = sorted(
        mood_df["user"].unique(),
        reverse=True
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

            normalized = percentage / 60

            opacity = (
                normalized ** 0.95
            ) * 0.95 + 0.08

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
                x1=col_i + 0.94,

                y0=row_i + 0.03,
                y1=row_i + 0.94,

                fillcolor=fill,

                line=dict(

                    width=3 if percentage == max_percentage else 1,

                    color=(

                        "rgba(255,255,255,0.55)"

                        if percentage == max_percentage

                        else "rgba(255,255,255,0.02)"
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

                y=1.18,

                sizex=0.34,

                sizey=0.34,

                xanchor="center",

                yanchor="middle",

                layer="above"
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

        showticklabels=False,

        autorange="reversed",

        showgrid=False,

        zeroline=False,

        range=[0, len(users)]
    )

    # ---------------------------------
    # LAYOUT
    # ---------------------------------

    fig.update_layout(

        height=520,

        paper_bgcolor=
        "rgba(0,0,0,0)",

        plot_bgcolor=
        "rgba(0,0,0,0)",

        margin=dict(
            l=10,
            r=10,
            t=130,
            b=20
        ),

        font=dict(
            color="white"
        )
    )

    return fig