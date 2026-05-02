# Project 4
# House Price Predictor

import pandas as pd


# Dataset

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Location_Score": [5, 6, 7, 8, 9, 5, 7, 8],
    "Price": [30, 45, 60, 75, 90, 35, 55, 70]  # in Lakhs
}


df = pd.DataFrame(data)

print("House Dataset Loaded Successfully ✅\n")
print(df)