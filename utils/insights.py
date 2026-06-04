def generate_insights(df):

    insights = []

    insights.append(
        f"Average GPA: {df['Post_Semester_GPA'].mean():.2f}"
    )

    insights.append(
        f"Average AI Usage: {df['Weekly_GenAI_Hours'].mean():.2f} hrs"
    )

    insights.append(
        f"Average Skill Retention: {df['Skill_Retention_Score'].mean():.2f}"
    )

    return insights
