import pandas as pd


def compute_clock(df):

    # ---------------------------------
    # TIME
    # ---------------------------------

    df["ts"] = pd.to_datetime(
        df["ts"]
    )

    df["hour"] = (
        df["ts"]
        .dt.hour
    )

    # ---------------------------------
    # GROUP
    # ---------------------------------

    grouped = (

        df.groupby(
            ["hour", "user"]
        )["minutes"]

        .sum()
        .reset_index()
    )

    # ---------------------------------
    # BUILD CLOCK DATA
    # ---------------------------------

    hours = list(range(24))

    dominant_users = []
    dominant_minutes = []

    for hour in hours:

        hour_df = grouped[
            grouped["hour"] == hour
        ]

        if hour_df.empty:

            dominant_users.append(None)
            dominant_minutes.append(0)

            continue

        top_row = hour_df.loc[
            hour_df["minutes"].idxmax()
        ]

        dominant_users.append(
            top_row["user"]
        )

        dominant_minutes.append(
            top_row["minutes"]
        )

    # ---------------------------------
    # PEAK TIME
    # ---------------------------------

    peak_index = dominant_minutes.index(
        max(dominant_minutes)
    )

    peak_hour = hours[
        peak_index
    ]

    peak_user = dominant_users[
        peak_index
    ]

    peak_minutes = int(
        dominant_minutes[
            peak_index
        ]
    )

    end_hour = (
        peak_hour + 2
    ) % 24

    # ---------------------------------
    # RETURN
    # ---------------------------------

    return {

        "hours": hours,

        "dominant_users":
            dominant_users,

        "dominant_minutes":
            dominant_minutes,

        "peak_hour":
            peak_hour,

        "peak_user":
            peak_user,

        "peak_minutes":
            peak_minutes,

        "end_hour":
            end_hour
    }