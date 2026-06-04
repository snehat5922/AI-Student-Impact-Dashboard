import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("🧠 Student Behavior Analytics")

fig=px.scatter(
    df.sample(5000),
    x="Traditional_Study_Hours",
    y="Skill_Retention_Score",
    color="Paid_Subscription"
)

st.plotly_chart(fig,use_container_width=True)

fig2=px.scatter_matrix(
    df.sample(3000),
    dimensions=[
        "Weekly_GenAI_Hours",
        "Traditional_Study_Hours",
        "Perceived_AI_Dependency",
        "Skill_Retention_Score"
    ]
)

st.plotly_chart(fig2,use_container_width=True)
