# Project 6
# Disease Prediction System

import pandas as pd


# Dataset

data = {
    "Fever": [1, 1, 0, 1, 0, 0],
    "Cough": [1, 1, 1, 0, 0, 1],
    "Headache": [1, 0, 1, 1, 0, 0],
    "Fatigue": [1, 1, 0, 1, 0, 0],
    "Disease": ["Flu", "Flu", "Cold", "Flu", "Healthy", "Cold"]
}


df = pd.DataFrame(data)

print("Disease Dataset Loaded Successfully ✅\n")
print(df)