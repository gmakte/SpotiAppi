import streamlit as st

from services.listening_rankings import (
    top_listeners
)


def render_podium(df):

    rankings = top_listeners(df)

    medals = ["🥇", "🥈", "🥉"]

    html = f"""
<div class="podium-card">

<div class="podium-title">
Who listens the most?
</div>
"""

    for i, (_, row) in enumerate(rankings.iterrows()):

        html += f"""
<div class="podium-row">

<div class="podium-left">

<div class="podium-medal">
{medals[i]}
</div>

<div class="podium-user">
{row["user"]}
</div>

</div>

<div class="podium-hours">
{row["hours"]:.0f}h
</div>

</div>
"""

    html += """
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )