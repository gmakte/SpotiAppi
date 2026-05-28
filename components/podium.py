import streamlit as st
import pandas as pd

from charts.podium_chart import (
    create_podium_chart
)


def render_podium(df):

    rankings = pd.read_csv('data/top_listeners.csv')

    fig = create_podium_chart(rankings)

    st.html("""
        <div class="clock-section-header">

            <div class="taste-evolution-title-inline">

                <span class="taste-evolution-title">
                    Listening Podium
                </span>

                <div class="taste-evolution-info-floating">

                    <span class="taste-evolution-info-icon">
                        i
                    </span>

                    <div class="taste-evolution-tooltip">
                        Rankings are based on total listening time across each user’s full Spotify history.
                    </div>

                </div>

            </div>

        </div>
    """)

    st.plotly_chart(
        fig,
        use_container_width=True
    )