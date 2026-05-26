import plotly.graph_objects as go


def create_obsession_chart(metrics):

    fig = go.Figure()

    colors = {
        0: "#4f6dff",
        1: "#FF8FD8",
        2: "#FF8A3D"
    }

    # ---------------------------------
    # AXIS RANGES
    # ---------------------------------

    x_min = metrics["skip_rate"].min()
    x_max = metrics["skip_rate"].max()

    y_min = metrics["replay_intensity"].min()
    y_max = metrics["replay_intensity"].max()

    x_padding = (
        x_max - x_min
    ) * 0.30

    y_padding = (
        y_max - y_min
    ) * 0.30

    median_x = (
        x_min + x_max
    ) / 2

    median_y = (
        y_min + y_max
    ) / 2

    # ---------------------------------
    # QUADRANT CROSS
    # ---------------------------------

    fig.add_vline(
        x=median_x,

        line_dash="dash",

        line_color=
        "rgba(255,255,255,0.18)",

        line_width=2
    )

    fig.add_hline(
        y=median_y,

        line_dash="dash",

        line_color=
        "rgba(255,255,255,0.18)",

        line_width=2
    )

    # ---------------------------------
    # QUADRANT BACKGROUNDS
    # ---------------------------------

    # TOP LEFT
    fig.add_shape(
        type="rect",

        x0=x_min - x_padding,
        x1=median_x,

        y0=median_y,
        y1=y_max + y_padding,

        fillcolor="rgba(79,109,255,0.13)",
        line_width=0,

        layer="below"
    )

    # TOP RIGHT
    fig.add_shape(
        type="rect",

        x0=median_x,
        x1=x_max + x_padding,

        y0=median_y,
        y1=y_max + y_padding,

        fillcolor="rgba(255,102,196,0.13)",
        line_width=0,

        layer="below"
    )

    # BOTTOM LEFT
    fig.add_shape(
        type="rect",

        x0=x_min - x_padding,
        x1=median_x,

        y0=y_min - y_padding,
        y1=median_y,

        fillcolor="rgba(91,255,152,0.13)",
        line_width=0,

        layer="below"
    )

    # BOTTOM RIGHT
    fig.add_shape(
        type="rect",

        x0=median_x,
        x1=x_max + x_padding,

        y0=y_min - y_padding,
        y1=median_y,

        fillcolor="rgba(255,158,87,0.13)",
        line_width=0,

        layer="below"
    )

    # ---------------------------------
    # POINTS
    # ---------------------------------

    for i, row in metrics.iterrows():

        fig.add_trace(
            go.Scatter(

                x=[row["skip_rate"]],
                y=[row["replay_intensity"]],

                mode="markers+text",

                text=[row["user"]],

                textposition="top center",

                marker=dict(
                    size=24,

                    color=colors.get(
                        i,
                        "white"
                    ),

                    line=dict(
                        width=2,
                        color="rgba(255,255,255,0.2)"
                    )
                ),

                textfont=dict(
                    size=16,
                    color="white"
                ),

                hovertemplate=
                f"""
                <b>{row['user']}</b><br>
                Skip rate: {row['skip_rate']:.2%}<br>
                Replay intensity: {row['replay_intensity']:.2f}
                <extra></extra>
                """
            )
        )

    # ---------------------------------
    # QUADRANT LABELS
    # ---------------------------------

    fig.add_annotation(
        x=x_min - x_padding * 0.9,
        y=y_max + y_padding * 0.55,

        text="<b>Comfort Zone</b>",

        showarrow=False,

        xanchor="left",

        font=dict(
            size=18,
            color="#4f6dff"
        )
    )

    fig.add_annotation(
        x=x_max + x_padding * 0.9,
        y=y_max + y_padding * 0.55,

        text="<b>Commitment Issues</b>",

        showarrow=False,

        xanchor="right",

        font=dict(
            size=18,
            color="#FF8FD8"
        )
    )

    fig.add_annotation(
        x=x_min - x_padding * 0.9,
        y=y_min - y_padding * 0.55,

        text="<b>Emotionally balanced</b>",

        showarrow=False,

        xanchor="left",

        font=dict(
            size=18,
            color="#58D23A"
        )
    )

    fig.add_annotation(
        x=x_max + x_padding * 0.9,
        y=y_min - y_padding * 0.55,

        text="<b>Short Attention Span</b>",

        showarrow=False,

        xanchor="right",

        font=dict(
            size=18,
            color="#FF8A3D"
        )
    )

    # ---------------------------------
    # AXES
    # ---------------------------------

    fig.update_xaxes(

        title="Skip rate",

        range=[
            x_min - x_padding,
            x_max + x_padding
        ],

        tickvals=[],

        showline=False,
        linecolor="rgba(255,255,255,0.25)",
        linewidth=2,

        gridcolor=
        "rgba(255,255,255,0.05)",

        zeroline=False
    )

    fig.update_yaxes(

        title="Replay intensity",

        range=[
            y_min - y_padding,
            y_max + y_padding
        ],

        tickvals=[],

        showline=False,
        linecolor="rgba(255,255,255,0.25)",
        linewidth=2,

        gridcolor=
        "rgba(255,255,255,0.05)",

        zeroline=False
    )

    # ---------------------------------
    # AXIS ARROWS
    # ---------------------------------

    # X-axis arrow
    fig.add_annotation(
        x=x_max + x_padding,
        y=y_min - y_padding,
        ax=x_min - x_padding,
        ay=y_min - y_padding,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor="rgba(255,255,255,0.45)"
    )

    # Y-axis arrow
    fig.add_annotation(
        x=x_min - x_padding,
        y=y_max + y_padding,
        ax=x_min - x_padding,
        ay=y_min - y_padding,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=2,
        arrowcolor="rgba(255,255,255,0.45)"
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
            l=50,
            r=50,
            t=50,
            b=50
        ),

        font=dict(
            color="white"
        ),

        showlegend=False
    )

    return fig