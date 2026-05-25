def top_listeners(df):

    rankings = (
        df.groupby("user")["ms_played"]
        .sum()
        .reset_index()
    )

    rankings["hours"] = (
        rankings["ms_played"] / 1000 / 60 / 60
    )

    rankings = rankings.sort_values(
        "hours",
        ascending=False
    )

    return rankings