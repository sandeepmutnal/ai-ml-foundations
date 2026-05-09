# Project 5
# Customer Churn Prediction

import pandas as pd
import matplotlib.pyplot as plt


# Dataset

data = {
    "Monthly_Bill": [500, 700, 300, 1000, 1200, 400, 900, 1500],
    "Tenure": [2, 5, 1, 10, 12, 3, 8, 15],
    "Support_Calls": [5, 2, 6, 1, 0, 4, 2, 1],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# 📊 Visualization 1: Monthly Bill vs Churn

plt.scatter(df["Monthly_Bill"], df["Churn"])

plt.xlabel("Monthly Bill")
plt.ylabel("Churn (0 = Stay, 1 = Leave)")
plt.title("Monthly Bill vs Customer Churn")

plt.show()


# 📊 Visualization 2: Support Calls vs Churn

plt.scatter(df["Support_Calls"], df["Churn"])

plt.xlabel("Support Calls")
plt.ylabel("Churn (0 = Stay, 1 = Leave)")
plt.title("Support Calls vs Customer Churn")

plt.show()


# 📊 Visualization 3: Tenure vs Churn

plt.scatter(df["Tenure"], df["Churn"])

plt.xlabel("Customer Tenure")
plt.ylabel("Churn (0 = Stay, 1 = Leave)")
plt.title("Tenure vs Customer Churn")

plt.show()