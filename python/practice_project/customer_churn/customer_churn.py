# Project 5
# Customer Churn Prediction (Interactive Version)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Monthly_Bill": [500, 700, 300, 1000, 1200, 400, 900, 1500],
    "Tenure": [2, 5, 1, 10, 12, 3, 8, 15],
    "Support_Calls": [5, 2, 6, 1, 0, 4, 2, 1],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")


# Features and Label

X = df[["Monthly_Bill", "Tenure", "Support_Calls"]]
y = df["Churn"]


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

bill = float(input("Enter Monthly Bill: "))
tenure = float(input("Enter Customer Tenure: "))
calls = float(input("Enter Support Calls: "))


# Prediction

prediction = model.predict([[bill, tenure, calls]])


# Final Result

if prediction[0] == 1:
    print("\n⚠️ Customer May Leave")
else:
    print("\n✅ Customer Will Stay")