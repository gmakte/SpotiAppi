import plotly.graph_objects as go


def create_venn_chart(data):

    fig = go.Figure()

    users = data["users"]

    totals = data["totals"]

    max_total = max(totals)

    # ---------------------------------
    # SCALE RADII
    # ---------------------------------

    radii = [
        1.6 + (t / max_total) * 1.0
        for t in totals
    ]

    if data["mode"] == 2:
        r1, r2 = radii

    else:
        r1, r2, r3 = radii

    # ---------------------------------
    # CIRCLES
    # ---------------------------------

    if data["mode"] == 2:

        circles = [

            dict(
                cx=2.8,
                cy=3.0,
                r=r1,

                line="#4f6dff",
                fill="rgba(79,109,255,0.28)"
            ),

            dict(
                cx=5.0,
                cy=3.0,
                r=r2,

                line="#FF8FD8",
                fill="rgba(255,143,216,0.28)"
            )
        ]

    else:

        circles = [

            dict(
                cx=2.8,
                cy=3.2,
                r=r1,

                line="#4f6dff",
                fill="rgba(79,109,255,0.28)"
            ),

            dict(
                cx=5.2,
                cy=3.2,
                r=r2,

                line="#FF8FD8",
                fill="rgba(255,143,216,0.28)"
            ),

            dict(
                cx=4.0,
                cy=1.2,
                r=r3,

                line="#FF8A3D",
                fill="rgba(255,158,87,0.28)"
            )
        ]

    # ---------------------------------
    # DRAW CIRCLES
    # ---------------------------------

    for c in circles:

        fig.add_shape(
            type="circle",

            x0=c["cx"] - c["r"],
            y0=c["cy"] - c["r"],

            x1=c["cx"] + c["r"],
            y1=c["cy"] + c["r"],

            line=dict(
                color=c["line"],
                width=3
            ),

            fillcolor=c["fill"]
        )

    # ---------------------------------
    # LABELS
    # ---------------------------------

    if data["mode"] == 2:

        labels = [

            (
                circles[0]["cx"] - 0.9,
                circles[0]["cy"],
                users[0],
                data["a_only"]
            ),

            (
                circles[1]["cx"] + 0.9,
                circles[1]["cy"],
                users[1],
                data["b_only"]
            ),

            (
                (circles[0]["cx"] + circles[1]["cx"]) / 2,
                circles[0]["cy"],
                "",
                data["ab"]
            ),
        ]

    else:

        labels = [

            (
                circles[0]["cx"] - 0.9,
                circles[0]["cy"] + 0.1,
                users[0],
                data["a_only"]
            ),

            (
                circles[1]["cx"] + 0.9,
                circles[1]["cy"] + 0.1,
                users[1],
                data["b_only"]
            ),

            (
                circles[2]["cx"],
                circles[2]["cy"] - 1.2,
                users[2],
                data["c_only"]
            ),

            (
                (circles[0]["cx"] + circles[1]["cx"]) / 2,
                circles[0]["cy"] + 0.3,
                "",
                data["ab"]
            ),

            (
                circles[0]["cx"] - 0.10,
                circles[2]["cy"] + 0.35,
                "",
                data["ac"]
            ),

            (
                circles[1]["cx"] - 0.03,
                circles[2]["cy"] + 0.35,
                "",
                data["bc"]
            ),

            (
                circles[2]["cx"],
                circles[2]["cy"] + 0.7,
                "",
                data["abc"]
            ),
        ]

    # ---------------------------------
    # DRAW LABELS
    # ---------------------------------

    for x, y, name, value in labels:

        if name:

            text = (
                f"<b>{name}</b><br>{value:,}"
            )

        else:

            text = f"<b>{value:,}</b>"

        fig.add_annotation(
            x=x,
            y=y,

            text=text,

            showarrow=False,

            font=dict(
                size=20,
                color="white"
            )
        )

    # ---------------------------------
    # AXES / LAYOUT
    # ---------------------------------

    fig.update_xaxes(
        visible=False,
        range=[-0.5, 8]
    )

    if data["mode"] == 2:

        y_range = [0, 6]

    else:

        y_range = [-2.5, 5]

    fig.update_yaxes(
        visible=False,
        range=y_range,
        scaleanchor="x"
    )

    fig.update_layout(
        height=500,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    return fig