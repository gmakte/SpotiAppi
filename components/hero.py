# import streamlit as st

# from services.basic_metrics import (
#     total_songs,
#     total_artists,
#     total_hours
# )



# def render_hero(df):

#     songs = total_songs(df)
#     artists = total_artists(df)
#     hours = total_hours(df)

#     html = f"""
#     <div class="main-card">

#     <div class="hero-title gradient-text">
#     Three people.<br>
#     Three musical identities.
#     </div>

#     <div class="metrics-row">

#     <div class="metric-block">
#     <div class="metric-icon">🎵</div>
#     <div class="metric-value">{songs:,}</div>
#     <div class="metric-label">songs</div>
#     </div>

#     <div class="metric-block">
#     <div class="metric-icon">👥</div>
#     <div class="metric-value">{artists:,}</div>
#     <div class="metric-label">artists</div>
#     </div>

#     <div class="metric-block">
#     <div class="metric-icon">🕒</div>
#     <div class="metric-value">{hours:,.0f}</div>
#     <div class="metric-label">hours</div>
#     </div>

#     </div>

#     </div>
#     """

#     st.markdown(
#         html,
#         unsafe_allow_html=True
#     )


import streamlit as st
from assets.palette import USER_COLORS

def render_hero():

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