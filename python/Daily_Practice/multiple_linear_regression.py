# Practice Day 25
# Multiple Linear Regression Model

import pandas as pd
from sklearn.linear_model import LinearRegression


# 1️⃣ Create Dataset

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Sleep_Hours": [7, 6, 6, 5, 5],
    "Attendance": [60, 70, 80, 90, 95],
    "Marks": [40, 50, 65, 80, 95]
}

df = pd.DataFrame(data)

print("Dataset:\n")
print(df)


# 2️⃣ Split Features and Label

X = df[["Study_Hours", "Sleep_Hours", "Attendance"]]
y = df["Marks"]


# 3️⃣ Create Model

model = LinearRegression()


# 4️⃣ Train Model

model.fit(X, y)


# 5️⃣ Predict Output

prediction = model.predict([[7, 6, 85]])

print("\nPredicted Marks:")
print(prediction)