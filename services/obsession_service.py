import pandas as pd


def compute_obsession_metrics(df):

    grouped = (
        df.groupby("user")
        .agg(
            total_streams=(
                "master_metadata_track_name",
                "count"
            ),

            unique_songs=(
                "master_metadata_track_name",
                "nunique"
            ),

            skipped=(
                "skipped",
                "sum"
            ),

            total_minutes=(
                "minutes",
                "sum"
            )
        )
        .reset_index()
    )

    grouped["skip_rate"] = (
        grouped["skipped"] /
        grouped["total_streams"]
    )

    grouped["replay_intensity"] = (
        grouped["total_streams"] /
        grouped["unique_songs"]
    )

    grouped["unique_ratio"] = (
        grouped["unique_songs"] /
        grouped["total_streams"]
    )

    return grouped