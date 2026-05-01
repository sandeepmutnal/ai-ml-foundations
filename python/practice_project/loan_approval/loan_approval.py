# Project 3
# Loan Approval GUI App

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Income": [25000, 40000, 50000, 60000, 35000, 80000, 90000, 45000],
    "Credit_Score": [600, 650, 700, 750, 620, 800, 820, 680],
    "Loan_Amount": [100000, 150000, 200000, 250000, 120000, 300000, 350000, 180000],
    "Approved": [0, 0, 1, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)


# Features & Labels

X = df[["Income", "Credit_Score", "Loan_Amount"]]
y = df["Approved"]


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

def predict_loan():
    try:
        income = float(entry_income.get())
        credit = float(entry_credit.get())
        loan = float(entry_loan.get())

        prediction = model.predict([[income, credit, loan]])

        if prediction[0] == 1:
            result_label.config(text="Loan Approved ✅")
        else:
            result_label.config(text="Loan Rejected ❌")

    except:
        result_label.config(text="Enter valid numbers")


# GUI Window

window = tk.Tk()
window.title("Loan Approval AI App")
window.geometry("350x300")


# Inputs

tk.Label(window, text="Income").pack()
entry_income = tk.Entry(window)
entry_income.pack()

tk.Label(window, text="Credit Score").pack()
entry_credit = tk.Entry(window)
entry_credit.pack()

tk.Label(window, text="Loan Amount").pack()
entry_loan = tk.Entry(window)
entry_loan.pack()


# Button

tk.Button(
    window,
    text="Check Loan Approval",
    command=predict_loan
).pack(pady=10)


# Result

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()