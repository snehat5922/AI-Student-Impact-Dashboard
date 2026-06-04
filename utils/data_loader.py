import pandas as pd

def load_data():
    return pd.read_csv(
        "data/ai_student_impact_dataset.csv"
    )
