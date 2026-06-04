import streamlit as st

st.set_page_config(
    page_title="AI Student Impact Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.image("assets/banner.png")

st.title("🎓 AI Student Impact Analytics Dashboard")

st.markdown("""
### Explore how Generative AI influences:

- Academic Performance
- GPA Growth
- Burnout Risk
- Study Habits
- Skill Retention
- Student Dependency on AI

Use the sidebar to navigate through pages.
""")

st.success("Dataset Size: 50,000 Students")
