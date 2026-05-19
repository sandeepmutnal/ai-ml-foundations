# Project 6
# Disease Prediction GUI App

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "Fever": [1, 1, 0, 1, 0, 0],
    "Cough": [1, 1, 1, 0, 0, 1],
    "Headache": [1, 0, 1, 1, 0, 0],
    "Fatigue": [1, 1, 0, 1, 0, 0],
    "Disease": ["Flu", "Flu", "Cold", "Healthy", "Healthy", "Cold"]
}

df = pd.DataFrame(data)


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


# Prediction Function

def predict_disease():
    try:
        fever = int(entry_fever.get())
        cough = int(entry_cough.get())
        headache = int(entry_headache.get())
        fatigue = int(entry_fatigue.get())

        prediction = model.predict([[fever, cough, headache, fatigue]])

        result_label.config(
            text="🩺 Predicted Disease: " + prediction[0]
        )

    except:
        result_label.config(text="Please enter only 0 or 1")


# GUI Window

window = tk.Tk()
window.title("Disease Prediction AI App")
window.geometry("400x350")


# Inputs

tk.Label(window, text="Fever (1 = Yes, 0 = No)").pack()
entry_fever = tk.Entry(window)
entry_fever.pack()

tk.Label(window, text="Cough (1 = Yes, 0 = No)").pack()
entry_cough = tk.Entry(window)
entry_cough.pack()

tk.Label(window, text="Headache (1 = Yes, 0 = No)").pack()
entry_headache = tk.Entry(window)
entry_headache.pack()

tk.Label(window, text="Fatigue (1 = Yes, 0 = No)").pack()
entry_fatigue = tk.Entry(window)
entry_fatigue.pack()


# Button

tk.Button(
    window,
    text="Predict Disease",
    command=predict_disease
).pack(pady=10)


# Result Label

result_label = tk.Label(window, text="")
result_label.pack()


# Run App

window.mainloop()