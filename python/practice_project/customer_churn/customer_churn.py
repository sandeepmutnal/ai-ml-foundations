# Project 5
# Customer Churn Prediction

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


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

print("\nTraining Data:", len(X_train))
print("Testing Data:", len(X_test))


# Model

model = LogisticRegression()
model.fit(X_train, y_train)


# Predictions

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)


# Accuracy

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))