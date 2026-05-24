import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("Listening trends between friends")

daily = df.groupby(["date", "user"])["minutes"].sum().reset_index()

fig = px.line(daily, x="date", y="minutes", color="user")

st.plotly_chart(fig, use_container_width=True)

if st.button("Go to Home"):
    st.switch_page("app.py")