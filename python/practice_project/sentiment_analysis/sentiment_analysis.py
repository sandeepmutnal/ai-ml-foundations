# Project 11
# Sentiment Analysis using TF-IDF

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

print("😊 Sentiment Analysis System Started\n")

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

# TF-IDF

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["Text"])

y = df["Sentiment"]

# Train Model

model = LogisticRegression()

model.fit(X, y)

print("✅ Model Trained Successfully")

# Test Prediction

test_text = [
    "I love this service"
]

test_vector = vectorizer.transform(
    test_text
)

prediction = model.predict(
    test_vector
)

print("\nPrediction:")

print(
    test_text[0],
    "→",
    prediction[0]
)