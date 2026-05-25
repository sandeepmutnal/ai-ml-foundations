# Project 7
# Fake News Detection GUI App

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import tkinter as tk


# Dataset

data = {
    "News": [
        "Government launches new healthcare scheme",
        "Aliens landed in Bangalore yesterday",
        "Scientists discover new medicine for cancer",
        "Actor secretly became king of India",
        "New technology improves solar energy",
        "Moon made of chocolate discovered",
        "Doctors develop new heart treatment",
        "Ghost seen driving bus in Mysore"
    ],

    "Label": [
        "Real",
        "Fake",
        "Real",
        "Fake",
        "Real",
        "Fake",
        "Real",
        "Fake"
    ]
}


df = pd.DataFrame(data)


# Features and Labels

X = df["News"]
y = df["Label"]


# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# TF-IDF Vectorization

vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)


# Train Model

model = MultinomialNB()

model.fit(X_train_vectorized, y_train)


# Prediction Function

def predict_news():
    try:
        news_text = news_entry.get()

        news_vector = vectorizer.transform([news_text])

        prediction = model.predict(news_vector)

        if prediction[0] == "Fake":
            result_label.config(text="❌ Fake News Detected")
        else:
            result_label.config(text="✅ Real News")

    except:
        result_label.config(text="Error in prediction")


# GUI Window

window = tk.Tk()

window.title("Fake News Detection AI App")

window.geometry("500x300")


# Title

title_label = tk.Label(
    window,
    text="Fake News Detection System",
    font=("Arial", 16)
)

title_label.pack(pady=10)


# Input

tk.Label(window, text="Enter News Headline").pack()

news_entry = tk.Entry(window, width=50)

news_entry.pack(pady=10)


# Button

predict_button = tk.Button(
    window,
    text="Predict News",
    command=predict_news
)

predict_button.pack(pady=10)


# Result

result_label = tk.Label(window, text="", font=("Arial", 14))

result_label.pack(pady=20)


# Run App

window.mainloop()