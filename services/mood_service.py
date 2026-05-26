import pandas as pd


def compute_mood_distribution(df):

    mood_order = [
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

    mood_df = (

        df.groupby(
            ["user", "mood"]
        )

        .size()

        .reset_index(
            name="count"
        )
    )

    mood_df["percentage"] = (

        mood_df.groupby("user")[
            "count"
        ]

        .transform(
            lambda x:
            x / x.sum() * 100
        )
    )

    mood_df["mood"] = pd.Categorical(

        mood_df["mood"],

        categories=mood_order,

        ordered=True
    )

    mood_df = mood_df.sort_values(
        "mood"
    )

    return mood_df