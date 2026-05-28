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

def compute_hourly_mood_map(df):

    mood_map = {}

    users = df["user"].unique()

    for user in users:

        user_df = df[
            df["user"] == user
        ]

        hourly_moods = []

        for hour in range(24):

            hour_df = user_df[
                user_df["hour"] == hour
            ]

            # no listening during this hour
            if len(hour_df) == 0:

                hourly_moods.append(
                    "Dark"
                )

                continue

            # count moods
            mood_counts = (

                hour_df

                .groupby("mood")

                .size()
            )

            dominant_mood = (

                mood_counts.idxmax()
            )

            hourly_moods.append(
                dominant_mood
            )

        mood_map[user] = hourly_moods

    return mood_map