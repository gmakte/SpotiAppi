def get_user_profiles(df):

    profiles = []

    for user in df["user"].unique():

        user_df = df[
            df["user"] == user
        ]

        songs = len(user_df[["master_metadata_track_name", "master_metadata_album_artist_name"]].drop_duplicates())

        artists = (
            user_df[
                "master_metadata_album_artist_name"
            ]
            .nunique()
        )

        years = (
            user_df["year"]
            .nunique()
        )

        profiles.append({

            "name": user,

            "Songs": songs,

            "Artists": artists,

            "Spotify Years": years
        })

    return profiles