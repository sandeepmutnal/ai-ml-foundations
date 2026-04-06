# Practice Day 24
# Train/Test Split + Model Accuracy

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 1️⃣ Create Dataset

data = {
    "Study_Hours": [2, 4, 6, 8, 10, 1, 3, 5, 7, 9],
    "Marks": [40, 50, 65, 80, 95, 35, 45, 60, 75, 85]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)


# 2️⃣ Split Features and Labels

X = df[["Study_Hours"]]
y = df["Marks"]


# 3️⃣ Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


print("\nTraining Data:\n", X_train)
print("\nTesting Data:\n", X_test)


# 4️⃣ Train Model

model = LinearRegression()

model.fit(X_train, y_train)


# 5️⃣ Predict Test Data

predictions = model.predict(X_test)

print("\nPredictions:\n", predictions)


# 6️⃣ Accuracy Score

accuracy = model.score(X_test, y_test)

print("\nModel Accuracy (R² Score):", accuracy)