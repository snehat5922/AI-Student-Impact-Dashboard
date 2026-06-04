import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv("data/ai_student_impact_dataset.csv")

st.title("📈 GPA Analysis")

df["GPA_Improvement"] = (
    df["Post_Semester_GPA"]
    - df["Pre_Semester_GPA"]
)

fig=px.scatter(
    df.sample(5000),
    x="Weekly_GenAI_Hours",
    y="GPA_Improvement",
    color="Major_Category",
    title="AI Usage vs GPA Improvement"
)

st.plotly_chart(fig,use_container_width=True)

major_gpa=df.groupby(
    "Major_Category"
)["Post_Semester_GPA"].mean().reset_index()

fig2=px.bar(
    major_gpa,
    x="Major_Category",
    y="Post_Semester_GPA",
    title="Average GPA by Major"
)

st.plotly_chart(fig2,use_container_width=True)
