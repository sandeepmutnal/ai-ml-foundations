# Project 1
# Student Marks Predictor

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

print("Dataset:\n", df)


# 2️⃣ Features and Label

X = df[["Study_Hours", "Sleep_Hours", "Attendance"]]
y = df["Marks"]


# 3️⃣ Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))


# 4️⃣ Create Model

model = LinearRegression()


# 5️⃣ Train Model

model.fit(X_train, y_train)


# 6️⃣ Predict Test Data

predictions = model.predict(X_test)

print("\nTest Predictions:")
print(predictions)


# 7️⃣ Accuracy Score

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy (R² Score):", accuracy)


# 8️⃣ Predict New Student Marks

new_prediction = model.predict([[7, 6, 85]])

print("\nPredicted Marks for New Student:")
print(new_prediction)