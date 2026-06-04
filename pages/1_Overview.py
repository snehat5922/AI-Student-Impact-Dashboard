import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("📊 Dataset Overview")

col1,col2,col3,col4=st.columns(4)

col1.metric("Students",len(df))
col2.metric("Avg GPA",round(df["Post_Semester_GPA"].mean(),2))
col3.metric("Avg AI Hours",round(df["Weekly_GenAI_Hours"].mean(),2))
col4.metric("Avg Skill Retention",round(df["Skill_Retention_Score"].mean(),2))

fig = px.pie(
    df,
    names="Major_Category",
    title="Students by Major"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.histogram(
    df,
    x="Weekly_GenAI_Hours",
    nbins=40,
    title="AI Usage Distribution"
)

st.plotly_chart(fig2,use_container_width=True)
