# Project 6
# Disease Prediction System (Interactive Version)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# Dataset

data = {
    "Fever": [1, 1, 0, 1, 0, 0],
    "Cough": [1, 1, 1, 0, 0, 1],
    "Headache": [1, 0, 1, 1, 0, 0],
    "Fatigue": [1, 1, 0, 1, 0, 0],
    "Disease": ["Flu", "Flu", "Cold", "Healthy", "Healthy", "Cold"]
}

df = pd.DataFrame(data)

print("Disease Dataset Loaded Successfully ✅\n")


# Features and Label

X = df[["Fever", "Cough", "Headache", "Fatigue"]]
y = df["Disease"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = DecisionTreeClassifier()

model.fit(X_train, y_train)


# Accuracy

accuracy = model.score(X_test, y_test)

print("Model Accuracy:", round(accuracy * 100, 2), "%")


# User Input

print("\nEnter Symptoms (1 = Yes, 0 = No)")

fever = int(input("Fever: "))
cough = int(input("Cough: "))
headache = int(input("Headache: "))
fatigue = int(input("Fatigue: "))


# Prediction

prediction = model.predict([[fever, cough, headache, fatigue]])


# Final Output

print("\n🩺 Predicted Disease:", prediction[0])