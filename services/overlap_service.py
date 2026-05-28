def compute_overlaps(df):

    users = sorted(df["user"].dropna().unique())

    user_sets = {}

    for user in users:

        user_df = df[df["user"] == user]

        artists = set(
            user_df["master_metadata_album_artist_name"]
            .dropna()
        )

        user_sets[user] = artists

    # ---------------------------------
    # TWO USERS
    # ---------------------------------

    if len(users) == 2:

        a, b = users

        A = user_sets[a]
        B = user_sets[b]

        return {

            "mode": 2,

            "users": [a, b],

            "totals": [
                len(A),
                len(B)
            ],

            "a_only": len(A - B),
            "b_only": len(B - A),

            "ab": len(A & B)
        }

    # ---------------------------------
    # THREE USERS
    # ---------------------------------

    elif len(users) == 3:

        a, b, c = users

        A = user_sets[a]
        B = user_sets[b]
        C = user_sets[c]

        return {

            "mode": 3,

            "users": [a, b, c],

            "totals": [
                len(A),
                len(B),
                len(C)
            ],

            "a_only": len(A - B - C),
            "b_only": len(B - A - C),
            "c_only": len(C - A - B),

            "ab": len((A & B) - C),
            "ac": len((A & C) - B),
            "bc": len((B & C) - A),

            "abc": len(A & B & C),
        }