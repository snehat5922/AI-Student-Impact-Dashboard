import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🤖 AI Usage Insights")

fig=px.box(
    df,
    x="Primary_Use_Case",
    y="Weekly_GenAI_Hours",
    color="Primary_Use_Case"
)

st.plotly_chart(fig,use_container_width=True)

fig2=px.sunburst(
    df,
    path=[
        "Prompt_Engineering_Skill",
        "Primary_Use_Case"
    ]
)

st.plotly_chart(fig2,use_container_width=True)
