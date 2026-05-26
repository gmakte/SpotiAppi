import pandas as pd


def compute_clock(df):

    # ---------------------------------
    # TIME
    # ---------------------------------

    df["ts"] = pd.to_datetime(
        df["ts"]
    )

    df["hour"] = (
        df["ts"].dt.hour
    )

    df["minute_block"] = (

        df["ts"].dt.minute // 30
    )

    # ---------------------------------
    # HALF-HOUR SLOT
    # ---------------------------------

    df["slot"] = (

        df["hour"] * 2 +

        df["minute_block"]
    )

    # ---------------------------------
    # TOTAL MINUTES PER USER
    # ---------------------------------

    user_totals = (

        df.groupby("user")["minutes"]

        .sum()
        .to_dict()
    )

    # ---------------------------------
    # GROUPED DATA
    # ---------------------------------

    grouped = (

        df.groupby(
            ["slot", "user"]
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

    slots = list(range(48))

    dominant_users = []

    dominant_minutes = []

    dominant_real_minutes = []

    for slot in slots:

        slot_df = grouped[
            grouped["slot"] == slot
        ]

        if slot_df.empty:

            dominant_users.append(None)

            dominant_minutes.append(0)

            dominant_real_minutes.append(0)

            continue

        top_row = slot_df.loc[
            slot_df[
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
            top_row["minutes"]
        )

    # ---------------------------------
    # PEAK
    # ---------------------------------

    peak_index = dominant_minutes.index(
        max(dominant_minutes)
    )

    peak_slot = slots[
        peak_index
    ]

    peak_hour = peak_slot // 2

    peak_minute = (
        "00"
        if peak_slot % 2 == 0
        else "30"
    )

    end_slot = (
        peak_slot + 2
    ) % 48

    end_hour = end_slot // 2

    end_minute = (
        "00"
        if end_slot % 2 == 0
        else "30"
    )

    peak_user = dominant_users[
        peak_index
    ]

    peak_minutes = int(
        dominant_real_minutes[
            peak_index
        ]
    )

    # ---------------------------------
    # RETURN
    # ---------------------------------

    return {

        "slots":
            slots,

        "dominant_users":
            dominant_users,

        "dominant_minutes":
            dominant_minutes,

        "dominant_real_minutes":
            dominant_real_minutes,

        "peak_hour":
            peak_hour,

        "peak_minute":
            peak_minute,

        "end_hour":
            end_hour,

        "end_minute":
            end_minute,

        "peak_user":
            peak_user,

        "peak_minutes":
            peak_minutes
    }