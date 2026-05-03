# Project 4
# House Price Predictor

import pandas as pd
import matplotlib.pyplot as plt


# Dataset

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Location_Score": [5, 6, 7, 8, 9, 5, 7, 8],
    "Price": [30, 45, 60, 75, 90, 35, 55, 70]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# 📊 Visualization 1: Area vs Price

plt.scatter(df["Area"], df["Price"])

plt.xlabel("Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Area vs House Price")

plt.show()


# 📊 Visualization 2: Bedrooms vs Price

plt.scatter(df["Bedrooms"], df["Price"])

plt.xlabel("Bedrooms")
plt.ylabel("Price (Lakhs)")
plt.title("Bedrooms vs House Price")

plt.show()


# 📊 Visualization 3: Location Score vs Price

plt.scatter(df["Location_Score"], df["Price"])

plt.xlabel("Location Score")
plt.ylabel("Price (Lakhs)")
plt.title("Location Score vs House Price")

plt.show()