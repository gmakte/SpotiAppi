import plotly.graph_objects as go


def create_mood_chart(mood_df):

    colors = {

        "Happy": "#FFD166",
        "Energetic": "#FF8A3D",
        "Calm": "#6FAF98",
        "Dreamy": "#FF8FD8",

        "Romantic": "#FF5CA8",

        "Confident": "#7B61FF",
        "Inspiring": "#4D96FF",

        "Dark": "#9B2242",
        "Dramatic": "#C44536",
        "Melancholic": "#4F6DFF"
    }

    fig = go.Figure()

    users = mood_df["user"].unique()

    moods = [
    "Happy",
    "Energetic",
    "Calm",
    "Dreamy",
    "Romantic",
    "Confident",
    "Inspiring",
    "Dark",
    "Dramatic",
    "Melancholic"
    ]

    for mood in moods:

        subset = mood_df[
            mood_df["mood"] == mood
        ]

        fig.add_trace(

            go.Bar(

                y=subset["user"],

                x=subset["percentage"],

                name=mood.capitalize(),

                orientation="h",

                marker=dict(
                    color=colors[mood]
                ),

                text=[
                    f"{v:.0f}%"
                    if v > 6 else ""
                    for v in subset[
                        "percentage"
                    ]
                ],

                textposition="inside"
            )
        )

    fig.update_layout(

        barmode="stack",

        height=320,

        paper_bgcolor=
        "rgba(0,0,0,0)",

        plot_bgcolor=
        "rgba(0,0,0,0)",

        font=dict(
            color="white"
        ),

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        legend=dict(
            orientation="h",
            y=1.15
        ),

        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),

        yaxis=dict(
            showgrid=False,
            zeroline=False
        )
    )

    return fig