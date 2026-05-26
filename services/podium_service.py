import pandas as pd


def top_listeners(df):

    rankings = (

        df.groupby("user")
        .agg(
            hours=(
                "minutes",
                lambda x: x.sum() / 60
            )
        )

        .reset_index()

        .sort_values(
            "hours",
            ascending=False
        )

        .head(3)
    )

    return rankings