# Project 11
# Sentiment Analysis Model Evaluation

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("😊 Sentiment Analysis Evaluation Started\n")

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

X_text = df["Text"]
y = df["Sentiment"]

X_train_text, X_test_text, y_train, y_test = train_test_split(
    X_text,
    y,
    test_size=0.25,
    random_state=42
)

vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)