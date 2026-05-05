# Project 4
# House Price Predictor (Interactive Version)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Location_Score": [5, 6, 7, 8, 9, 5, 7, 8],
    "Price": [30, 45, 60, 75, 90, 35, 55, 70]
}

df = pd.DataFrame(data)


# Features and Label

X = df[["Area", "Bedrooms", "Location_Score"]]
y = df["Price"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# Accuracy

accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")


# User Input

print("\nEnter House Details:")

area = float(input("Enter Area (sq.ft): "))
bedrooms = float(input("Enter Number of Bedrooms: "))
location = float(input("Enter Location Score (1-10): "))


# Prediction

prediction = model.predict([[area, bedrooms, location]])


print("\n🎯 Predicted House Price:", round(prediction[0], 2), "Lakhs")