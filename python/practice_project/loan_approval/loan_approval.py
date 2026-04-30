# Project 3
# Loan Approval Predictor (Interactive Version)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Income": [25000, 40000, 50000, 60000, 35000, 80000, 90000, 45000],
    "Credit_Score": [600, 650, 700, 750, 620, 800, 820, 680],
    "Loan_Amount": [100000, 150000, 200000, 250000, 120000, 300000, 350000, 180000],
    "Approved": [0, 0, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")


# Features and Label

X = df[["Income", "Credit_Score", "Loan_Amount"]]
y = df["Approved"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = LogisticRegression()
model.fit(X_train, y_train)


# Accuracy

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")


# User Input

print("\nEnter Customer Details:")

income = float(input("Enter Income: "))
credit = float(input("Enter Credit Score: "))
loan = float(input("Enter Loan Amount: "))


# Prediction

prediction = model.predict([[income, credit, loan]])


# Output Result

if prediction[0] == 1:
    print("\n🎯 Loan Approved ✅")
else:
    print("\n❌ Loan Rejected")