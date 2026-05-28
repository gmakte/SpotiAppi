import streamlit as st
from assets.palette import USER_COLORS

def render_hero(df):

    html = f"""
        <div class="main-card">

            <div class="hero-content">

                <div class="hero-title">

                    <span style="color:{USER_COLORS['Ashanti']}">
                        Three people.
                    </span>

                    <span style="color:{USER_COLORS['Gabi']}">
                        Three musical
                    </span>

                    <span style="color:{USER_COLORS['Maribel']}">
                        identities.
                    </span>

                </div>

                <div class="hero-subtitle">
                    Exploring our listening habits,<br>
                    similarities and personalities.
                </div>

            </div>

        </div>
        """

    st.html(html)