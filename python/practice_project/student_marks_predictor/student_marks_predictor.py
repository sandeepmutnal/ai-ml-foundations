# Project 1
# Student Marks Predictor

import pandas as pd
from sklearn.linear_model import LinearRegression


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


# 3️⃣ Create Model

model = LinearRegression()


# 4️⃣ Train Model

model.fit(X, y)


# 5️⃣ Predict Marks

prediction = model.predict([[7, 6, 85]])

print("\nPredicted Marks:")
print(prediction)