import pandas as pd
from assets.palette import GENRE_COLORS
GENRE_ORDER = list(GENRE_COLORS.keys())

def prepare_genre_evolution(df, user, timeline_mode, selected_genre):

    df = df[df["user"] == user]

    # aligned comparison mode
    if timeline_mode == "Aligned":
        df = df[
            (df["month"] >= "2023-07")
            &
            (df["month"] <= "2025-03")
        ]

    # only AFTER normalization
    if selected_genre != "All":

        df = df[
            df["genre"] == selected_genre
        ]

    pivot_df = (
        df
        .pivot(
            index="month",
            columns="genre",
            values="pct"
            )
        .fillna(0)
    )

    # chronological order
    pivot_df = pivot_df.sort_index()

    # consistent genre order
    pivot_df = pivot_df.reindex(
        columns=GENRE_ORDER,
        fill_value=0
    )

    # # rolling smoothing
    # pivot_df = (
    #     pivot_df
    #     .rolling(
    #         window=3,
    #         min_periods=1,
    #         center=True
    #     )
    #     .mean()
    # )

    return pivot_df