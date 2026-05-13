# Project 5
# Customer Churn Prediction GUI App

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Monthly_Bill": [500, 700, 300, 1000, 1200, 400, 900, 1500],
    "Tenure": [2, 5, 1, 10, 12, 3, 8, 15],
    "Support_Calls": [5, 2, 6, 1, 0, 4, 2, 1],
    "Churn": [1, 0, 1, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)


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


# Train Model

model = LogisticRegression()
model.fit(X_train, y_train)


# Prediction Function

def predict_churn():
    try:
        bill = float(entry_bill.get())
        tenure = float(entry_tenure.get())
        calls = float(entry_calls.get())

        prediction = model.predict([[bill, tenure, calls]])

        if prediction[0] == 1:
            result_label.config(text="⚠️ Customer May Leave")
        else:
            result_label.config(text="✅ Customer Will Stay")

    except:
        result_label.config(text="Please enter valid numbers")


# GUI Window

window = tk.Tk()
window.title("Customer Churn Prediction AI App")
window.geometry("400x320")


# Inputs

tk.Label(window, text="Monthly Bill").pack()
entry_bill = tk.Entry(window)
entry_bill.pack()

tk.Label(window, text="Customer Tenure").pack()
entry_tenure = tk.Entry(window)
entry_tenure.pack()

tk.Label(window, text="Support Calls").pack()
entry_calls = tk.Entry(window)
entry_calls.pack()


# Button

tk.Button(
    window,
    text="Predict Customer Churn",
    command=predict_churn
).pack(pady=10)


# Result Label

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()