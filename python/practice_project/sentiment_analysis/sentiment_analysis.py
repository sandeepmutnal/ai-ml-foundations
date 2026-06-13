# Project 11
# Sentiment Analysis System

import pandas as pd

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

print("Dataset Loaded Successfully ✅\n")

print(df)