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
    # TOTAL MINUTES PER USER
    # ---------------------------------

    user_totals = (

        df.groupby("user")["minutes"]

        .sum()
        .to_dict()
    )

    total_minutes_all = sum(
        user_totals.values()
    )

    # ---------------------------------
    # GROUPED DATA
    # ---------------------------------

    grouped = (

        df.groupby(
            ["hour", "user"]
        )["minutes"]

        .sum()
        .reset_index()
    )

    # ---------------------------------
    # NORMALIZATION
    # ---------------------------------

    grouped["normalized"] = (

        grouped.apply(

            lambda row:

            row["minutes"] /

            user_totals[
                row["user"]
            ],

            axis=1
        )
    )

    # ---------------------------------
    # BUILD CLOCK
    # ---------------------------------

    hours = list(range(24))

    dominant_users = []

    dominant_minutes = []

    dominant_real_minutes = []

    for hour in hours:

        hour_df = grouped[
            grouped["hour"] == hour
        ]

        if hour_df.empty:

            dominant_users.append(None)

            dominant_minutes.append(0)

            dominant_real_minutes.append(0)

            continue

        top_row = hour_df.loc[
            hour_df[
                "normalized"
            ].idxmax()
        ]

        dominant_users.append(
            top_row["user"]
        )

        dominant_minutes.append(
            top_row["normalized"]
        )

        dominant_real_minutes.append(
            int(top_row["minutes"])
        )

    # ---------------------------------
    # PEAK CLOCK TIME
    # ---------------------------------

    peak_index = dominant_minutes.index(
        max(dominant_minutes)
    )

    peak_hour = hours[
        peak_index
    ]

    end_hour = (
        peak_hour + 1
    ) % 24

    peak_user = dominant_users[
        peak_index
    ]

    peak_minutes = int(
        dominant_real_minutes[
            peak_index
        ]
    )

    # ---------------------------------
    # LISTENING SHARE
    # ---------------------------------

    listening_share = []

    for user, minutes in user_totals.items():

        # -----------------------------
        # SHARE %
        # -----------------------------

        share = round(
            (minutes / total_minutes_all)
            * 100
        )

        # -----------------------------
        # USER PEAK HOUR
        # -----------------------------

        user_df = grouped[
            grouped["user"] == user
        ]

        top_hour_row = user_df.loc[
            user_df["minutes"].idxmax()
        ]

        user_peak_hour = int(
            top_hour_row["hour"]
        )

        user_peak_end = (
            user_peak_hour + 1
        ) % 24

        user_peak_minutes = int(
            top_hour_row["minutes"]
        )

        # -----------------------------
        # INSIGHT
        # -----------------------------

        if (
            user_peak_hour >= 0 and
            user_peak_hour < 6
        ):

            insight = (
                f"{user} owns the late night."
            )

        elif (
            user_peak_hour >= 6 and
            user_peak_hour < 12
        ):

            insight = (
                f"{user} is the morning person."
            )

        elif (
            user_peak_hour >= 12 and
            user_peak_hour < 18
        ):

            insight = (
                f"{user} takes over the afternoon."
            )

        else:

            insight = (
                f"{user} dominates the evening."
            )

        listening_share.append({

            "user":
                user,

            "minutes":
                int(minutes),

            "share":
                share,

            "peak_hour":
                user_peak_hour,

            "peak_end_hour":
                user_peak_end,

            "peak_minutes":
                user_peak_minutes,

            "insight":
                insight
        })

    # ---------------------------------
    # RETURN
    # ---------------------------------

    return {

        "hours":
            hours,

        "dominant_users":
            dominant_users,

        "dominant_minutes":
            dominant_minutes,

        "dominant_real_minutes":
            dominant_real_minutes,

        "peak_hour":
            peak_hour,

        "end_hour":
            end_hour,

        "peak_user":
            peak_user,

        "peak_minutes":
            peak_minutes,

        "listening_share":
            listening_share
    }