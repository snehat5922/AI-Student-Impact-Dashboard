import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🔥 Burnout Analytics")

burnout=df.groupby(
    "Burnout_Risk_Level"
).size().reset_index(name="Count")

fig=px.pie(
    burnout,
    names="Burnout_Risk_Level",
    values="Count"
)

st.plotly_chart(fig,use_container_width=True)

fig2=px.violin(
    df,
    x="Burnout_Risk_Level",
    y="Weekly_GenAI_Hours",
    color="Burnout_Risk_Level"
)

st.plotly_chart(fig2,use_container_width=True)
