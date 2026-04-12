# Practice Day 30
# Confusion Matrix Example

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# 1️⃣ Dataset

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)


# 2️⃣ Features and Label

X = df[["Study_Hours"]]
y = df["Pass"]


# 3️⃣ Train Model

model = LogisticRegression()

model.fit(X, y)


# 4️⃣ Predictions

predictions = model.predict(X)


# 5️⃣ Confusion Matrix

cm = confusion_matrix(y, predictions)

print("Confusion Matrix:\n")
print(cm)