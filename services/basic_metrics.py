def total_songs(df):
    return df[["master_metadata_track_name", "master_metadata_album_artist_name"]].drop_duplicates().shape[0]


def total_artists(df):
    return df["master_metadata_album_artist_name"].nunique()


def total_hours(df):
    return df["ms_played"].sum() / 1000 / 60 / 60