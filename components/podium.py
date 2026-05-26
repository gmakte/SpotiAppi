import streamlit as st

from charts.podium_chart import (
    create_podium_chart
)

from services.podium_service import (
    top_listeners
)


def render_podium(df):

    rankings = top_listeners(df)

    fig = create_podium_chart(rankings)

    st.markdown(
        "### Listening Podium"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )