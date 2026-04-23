# Project 2
# Salary Predictor AI Model

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [2,3,4,5,6.5,7.5,8.5,9.5,10.5,12]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")
print(df)


# Features and Label

X = df[["Experience"]]
y = df["Salary"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))


# Create Model

model = LinearRegression()


# Train Model

model.fit(X_train, y_train)


# Predict Test Data

predictions = model.predict(X_test)

print("\nTest Predictions:")
print(predictions)


# Accuracy Score

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy (R² Score):", round(accuracy, 2))


# Predict New Salary

new_prediction = model.predict([[5]])

print("\nPredicted Salary for 5 Years Experience:")
print(round(new_prediction[0], 2), "LPA")