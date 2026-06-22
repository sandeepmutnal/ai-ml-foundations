# Project 12
# Stock Market Prediction AI - Interactive Version

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print("📈 Interactive Stock Price Predictor Started\n")

data = {
    "Open_Price": [100, 102, 101, 105, 107, 110, 108, 112, 115, 117],
    "High_Price": [105, 106, 104, 108, 111, 113, 112, 116, 118, 120],
    "Low_Price": [98, 100, 99, 103, 105, 108, 106, 110, 113, 115],
    "Volume": [1000, 1200, 1100, 1500, 1700, 1600, 1800, 1900, 2000, 2100],
    "Close_Price": [102, 101, 105, 107, 110, 108, 112, 115, 117, 119]
}

df = pd.DataFrame(data)

X = df[["Open_Price", "High_Price", "Low_Price", "Volume"]]
y = df["Close_Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nEnter Stock Details:")

open_price = float(input("Open Price: "))
high_price = float(input("High Price: "))
low_price = float(input("Low Price: "))
volume = float(input("Volume: "))

prediction = model.predict([[open_price, high_price, low_price, volume]])

print("\n🎯 Predicted Close Price:", round(prediction[0], 2))