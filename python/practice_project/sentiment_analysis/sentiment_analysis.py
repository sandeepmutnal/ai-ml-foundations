# Project 11
# GUI Sentiment Analysis App

import tkinter as tk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "Text": [
        "I love this product",
        "Amazing experience",
        "Very happy with service",
        "This is terrible",
        "Worst purchase ever",
        "I hate this",
        "It is okay",
        "Average quality",
        "Nothing special",
        "Excellent service",
        "Bad quality",
        "Not good not bad"
    ],
    "Sentiment": [
        "Positive",
        "Positive",
        "Positive",
        "Negative",
        "Negative",
        "Negative",
        "Neutral",
        "Neutral",
        "Neutral",
        "Positive",
        "Negative",
        "Neutral"
    ]
}

df = pd.DataFrame(data)

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Text"])
y = df["Sentiment"]

model = LogisticRegression()
model.fit(X, y)

# Prediction function
def predict_sentiment():
    review = entry.get()

    if review.strip() == "":
        result_label.config(text="Please enter a review")
        return

    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)[0]

    if prediction == "Positive":
        result_label.config(text="😊 Positive Sentiment")
    elif prediction == "Negative":
        result_label.config(text="😡 Negative Sentiment")
    else:
        result_label.config(text="😐 Neutral Sentiment")

# GUI
window = tk.Tk()
window.title("Sentiment Analysis AI App")
window.geometry("500x300")

title = tk.Label(
    window,
    text="Sentiment Analysis AI System",
    font=("Arial", 16)
)
title.pack(pady=10)

entry = tk.Entry(window, width=60)
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Analyze Sentiment",
    command=predict_sentiment
)
button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()