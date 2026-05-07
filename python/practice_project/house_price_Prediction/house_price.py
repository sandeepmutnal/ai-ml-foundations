# Project 4
# House Price Predictor GUI App

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Area": [1000, 1500, 2000, 2500, 3000, 1200, 1800, 2200],
    "Bedrooms": [2, 3, 3, 4, 4, 2, 3, 4],
    "Location_Score": [5, 6, 7, 8, 9, 5, 7, 8],
    "Price": [30, 45, 60, 75, 90, 35, 55, 70]
}

df = pd.DataFrame(data)


# Features & Labels

X = df[["Area", "Bedrooms", "Location_Score"]]
y = df["Price"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# Prediction Function

def predict_price():
    try:
        area = float(entry_area.get())
        bedrooms = float(entry_bedrooms.get())
        location = float(entry_location.get())

        prediction = model.predict([[area, bedrooms, location]])

        result_label.config(
            text="Predicted Price: ₹" + str(round(prediction[0], 2)) + " Lakhs"
        )

    except:
        result_label.config(text="Please enter valid numbers")


# GUI Window

window = tk.Tk()
window.title("House Price Predictor AI App")
window.geometry("400x320")


# Inputs

tk.Label(window, text="Area (sq.ft)").pack()
entry_area = tk.Entry(window)
entry_area.pack()

tk.Label(window, text="Bedrooms").pack()
entry_bedrooms = tk.Entry(window)
entry_bedrooms.pack()

tk.Label(window, text="Location Score (1-10)").pack()
entry_location = tk.Entry(window)
entry_location.pack()


# Button

tk.Button(
    window,
    text="Predict House Price",
    command=predict_price
).pack(pady=10)


# Result Label

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()