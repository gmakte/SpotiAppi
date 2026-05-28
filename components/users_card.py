import streamlit as st
import pandas as pd
import base64
from pathlib import Path


def image_to_base64(path):

    file_dir = Path(__file__).parent

    full_path = file_dir / path

    with open(full_path, "rb") as img:

        return base64.b64encode(
            img.read()
        ).decode()


def render_users_card():

    profiles = pd.read_csv(
        'data/user_profiles.csv'
    )

    html = """
        <div class="users-card">

        <div class="users-title">
        Meet the Listeners
        </div>

        <div class="users-wrapper">
    """

    for _, user in profiles.iterrows():

        encoded = image_to_base64(
            f"../assets/avatars/{user['name'].lower()}.png"
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
                Years
                </div>

            </div>

            </div>
        """

    html += """
        </div>
        </div>
    """

    st.html(html)