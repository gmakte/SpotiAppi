import pandas as pd
from assets.palette import GENRE_COLORS
GENRE_ORDER = list(GENRE_COLORS.keys())

def prepare_genre_evolution(df, user, timeline_mode):

    user_df = df[df["user"] == user].copy()

    # remove sparse early activity
    if user == "Maribel":
        user_df = user_df[user_df["month"] != "2015-08"]


    # aligned comparison mode
    if timeline_mode == "Aligned":
        user_df = user_df[
            (user_df["month"] >= "2023-07")
            &
            (user_df["month"] <= "2025-03")
        ]

    monthly = (
        user_df
        .groupby(["month", "genre"])["ms_played"]
        .sum()
        .reset_index()
    )

    # total listening per month
    totals = (
        monthly
        .groupby("month")["ms_played"]
        .transform("sum")
    )

    # normalize to percentages
    monthly["pct"] = monthly["ms_played"] / totals

    pivot_df = (
        monthly
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

    # rolling smoothing
    pivot_df = (
        pivot_df
        .rolling(
            window=3,
            min_periods=1,
            center=True
        )
        .mean()
    )

    return pivot_df