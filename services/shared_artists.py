import pandas as pd


def compute_shared_artists(df):

    # TOTAL LISTENING PER USER
    user_totals = (
        df.groupby("user")["minutes"]
        .sum()
    )

    # ARTIST MINUTES
    grouped = (
        df.groupby(
            ["user", "master_metadata_album_artist_name"]
        )["minutes"]
        .sum()
        .reset_index()
    )

    # NORMALIZE
    grouped["normalized"] = grouped.apply(
        lambda row:
        row["minutes"] / user_totals[row["user"]],
        axis=1
    )

    # PIVOT
    pivot = grouped.pivot(
        index="master_metadata_album_artist_name",
        columns="user",
        values="normalized"
    ).fillna(0)

    # SHARED BY 2+ USERS
    shared = pivot[(pivot > 0).sum(axis=1) >= 2]

    # BALANCED SHARED SCORE
    shared["score"] = shared.min(axis=1)

    shared = (
        shared.sort_values(
            "score",
            ascending=False
        )
        .head(5)
        .reset_index()
    )

    # PERCENT FORMAT
    shared["score"] = (
        shared["score"] * 100
    )

    return shared[
        [
            "master_metadata_album_artist_name",
            "score"
        ]
    ]