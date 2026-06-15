# Project 11
# Interactive Sentiment Analysis System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("😊 Interactive Sentiment Analysis System Started\n")

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
        "Nothing special"
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
        "Neutral"
    ]
}

df = pd.DataFrame(data)

# Features and Label
X_text = df["Text"]
y = df["Sentiment"]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

# Train Model
model = LogisticRegression()
model.fit(X, y)

print("✅ Model Trained Successfully")

# User Input
user_review = input("\nEnter your review: ")

# Convert input to vector
user_vector = vectorizer.transform([user_review])

# Prediction
prediction = model.predict(user_vector)

print("\n🎯 Sentiment Result:", prediction[0])