import streamlit as st
import base64
from pathlib import Path

from services.user_services import (
    get_user_profiles
)


def image_to_base64(path):

    file_dir = Path(__file__).parent

    full_path = file_dir / path

    with open(full_path, "rb") as img:

        return base64.b64encode(
            img.read()
        ).decode()


def render_users_card(df):

    profiles = get_user_profiles(df)

    users = [
        {
            "name": "Gabi",
            "image": "../assets/avatars/gabi.png"
        },

        {
            "name": "Ashanti",
            "image": "../assets/avatars/ash.png"
        },

        {
            "name": "Maribel",
            "image": "../assets/avatars/maribel.png"
        }
    ]

    # ---------------------------------
    # MERGE METRICS INTO USERS
    # ---------------------------------

    profile_map = {

        p["name"]: p
        for p in profiles
    }

    for user in users:

        user.update(
            profile_map[user["name"]]
        )

    # ---------------------------------
    # HTML
    # ---------------------------------

    html = """
<div class="users-card">

<div class="users-title">
Meet the Listeners
</div>

<div class="users-wrapper">
"""

    for user in users:

        encoded = image_to_base64(
            user["image"]
        )

        html += f"""
<div class="user-block">

<img
src="data:image/png;base64,{encoded}"
class="user-avatar"/>

<div class="user-name">
{user['name']}
</div>

<div class="user-stats">

<div>
<b>{user['Songs']:,}</b><br>
Songs
</div>

<div>
<b>{user['Artists']:,}</b><br>
Artists
</div>

<div>
<b>{user['Spotify Years']}</b><br>
Spotify Years
</div>

</div>

</div>
"""

    html += """
</div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )