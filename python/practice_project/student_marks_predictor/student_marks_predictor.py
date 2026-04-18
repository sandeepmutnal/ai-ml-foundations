# Project 1
# Student Marks Predictor (Interactive Version)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 1️⃣ Dataset

data = {
    "Study_Hours": [2,4,6,8,10,3,5,7,9],
    "Sleep_Hours": [7,6,6,5,5,7,6,6,5],
    "Attendance": [60,70,80,90,95,65,75,85,92],
    "Marks": [40,50,65,80,95,45,60,75,88]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅")


# 2️⃣ Features and Label

X = df[["Study_Hours", "Sleep_Hours", "Attendance"]]
y = df["Marks"]


# 3️⃣ Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 4️⃣ Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# 5️⃣ Accuracy Score

accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", round(accuracy * 100, 2), "%")


# 6️⃣ Take User Input

print("\nEnter Student Details:")

study_hours = float(input("Enter Study Hours: "))
sleep_hours = float(input("Enter Sleep Hours: "))
attendance = float(input("Enter Attendance (%): "))


# 7️⃣ Predict Marks

prediction = model.predict([[study_hours, sleep_hours, attendance]])

print("\n🎯 Predicted Marks:", round(prediction[0], 2))