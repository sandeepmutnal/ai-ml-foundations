# Project 3
# Loan Approval Predictor

import pandas as pd
from sklearn.linear_model import LogisticRegression


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


# Features and Label

X = df[["Income", "Credit_Score", "Loan_Amount"]]
y = df["Approved"]


# Create Model

model = LogisticRegression()


# Train Model

model.fit(X, y)


# Predict Loan Approval

prediction = model.predict([[50000, 720, 200000]])

print("\nLoan Prediction (1 = Approved, 0 = Rejected):")
print(prediction)