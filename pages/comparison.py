import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(page_title="Comparison", layout="wide")

st.title("Gabi vs Ash")

# ----------------------------
# LOAD DATA
# ----------------------------
df = load_data()

# ----------------------------
# TOTAL LISTENING
# ----------------------------
total = df.groupby("user")["minutes"].sum().reset_index()

fig = px.bar(
    total,
    x="user",
    y="minutes",
    color="user",
    title="Total Listening Time"
)

fig.update_layout(
    plot_bgcolor="#0B0B0B",
    paper_bgcolor="#0B0B0B",
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# INSIGHT
# ----------------------------
g = total[total["user"] == "Gabi"]["minutes"].values[0]
a = total[total["user"] == "Ash"]["minutes"].values[0]

if g > a:
    st.success("Gabi listens more than Ash")
else:
    st.success("Ashanti listens more than Gabi")

if st.button("Go to Home"):
    st.switch_page("app.py")