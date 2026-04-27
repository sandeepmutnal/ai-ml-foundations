# Project 3
# Loan Approval Predictor

import pandas as pd
import matplotlib.pyplot as plt


# Dataset

data = {
    "Income": [25000, 40000, 50000, 60000, 35000, 80000, 90000, 45000],
    "Credit_Score": [600, 650, 700, 750, 620, 800, 820, 680],
    "Loan_Amount": [100000, 150000, 200000, 250000, 120000, 300000, 350000, 180000],
    "Approved": [0, 0, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# 🎯 Visualization 1: Income vs Approval

plt.scatter(df["Income"], df["Approved"])

plt.xlabel("Income")
plt.ylabel("Loan Approval (0 = No, 1 = Yes)")
plt.title("Income vs Loan Approval")

plt.show()


# 🎯 Visualization 2: Credit Score vs Approval

plt.scatter(df["Credit_Score"], df["Approved"])

plt.xlabel("Credit Score")
plt.ylabel("Loan Approval (0 = No, 1 = Yes)")
plt.title("Credit Score vs Loan Approval")

plt.show()