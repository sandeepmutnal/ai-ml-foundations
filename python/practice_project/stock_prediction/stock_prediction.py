# Project 12
# Stock Market Prediction AI - Visualization

import pandas as pd
import matplotlib.pyplot as plt

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

print(df)

# Close price trend
plt.plot(df["Day"], df["Close_Price"], marker="o")

plt.title("Stock Close Price Trend")
plt.xlabel("Day")
plt.ylabel("Close Price")

plt.grid(True)
plt.show()

# Volume trend
plt.bar(df["Day"], df["Volume"])

plt.title("Stock Volume Trend")
plt.xlabel("Day")
plt.ylabel("Volume")

plt.show()