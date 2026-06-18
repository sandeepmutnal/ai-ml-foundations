# Project 12
# Stock Market Prediction AI

import pandas as pd

print("📈 Stock Market Prediction AI Started\n")

# Sample stock dataset
data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Open_Price": [100, 102, 101, 105, 107, 110, 108],
    "High_Price": [105, 106, 104, 108, 111, 113, 112],
    "Low_Price": [98, 100, 99, 103, 105, 108, 106],
    "Volume": [1000, 1200, 1100, 1500, 1700, 1600, 1800],
    "Close_Price": [102, 101, 105, 107, 110, 108, 112]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)