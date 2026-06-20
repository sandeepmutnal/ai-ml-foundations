# Project 12
# Stock Market Prediction AI - Model Training

import pandas as pd
from sklearn.linear_model import LinearRegression

print("📈 Stock Market Prediction AI Started\n")

data = {
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Open_Price": [100, 102, 101, 105, 107, 110, 108],
    "High_Price": [105, 106, 104, 108, 111, 113, 112],
    "Low_Price": [98, 100, 99, 103, 105, 108, 106],
    "Volume": [1000, 1200, 1100, 1500, 1700, 1600, 1800],
    "Close_Price": [102, 101, 105, 107, 110, 108, 112]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)

# Features and Label
X = df[["Open_Price", "High_Price", "Low_Price", "Volume"]]
y = df["Close_Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict close price
prediction = model.predict([[111, 114, 109, 1900]])

print("\nPredicted Close Price:")
print(round(prediction[0], 2))