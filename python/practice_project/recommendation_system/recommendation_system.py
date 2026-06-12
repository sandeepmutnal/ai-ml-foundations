# Project 10
# GUI Movie Recommendation System

import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset

data = {
    "Movie": [
        "Avengers",
        "Iron Man",
        "Captain America",
        "Thor",
        "Titanic",
        "The Notebook",
        "Interstellar",
        "Inception"
    ],

    "Description": [
        "superhero team saves the world",
        "genius billionaire superhero fights enemies",
        "super soldier protects humanity",
        "god of thunder fights evil forces",
        "romantic story on a ship",
        "emotional love story",
        "space exploration and science fiction adventure",
        "dream manipulation science fiction thriller"
    ]
}

df = pd.DataFrame(data)

# TF-IDF

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    df["Description"]
)

# Recommendation Function

def recommend():

    result_box.delete("1.0", tk.END)

    user_input = entry.get()

    favorite_movies = [
        movie.strip()
        for movie in user_input.split(",")
    ]

    user_descriptions = []

    for movie in favorite_movies:

        if movie in df["Movie"].values:

            description = df[
                df["Movie"] == movie
            ]["Description"].values[0]

            user_descriptions.append(
                description
            )

    if len(user_descriptions) == 0:

        result_box.insert(
            tk.END,
            "❌ No valid movies entered."
        )

        return

    user_profile = " ".join(
        user_descriptions
    )

    user_vector = vectorizer.transform(
        [user_profile]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )[0]

    df["Similarity"] = similarity_scores

    recommendations = df.sort_values(
        by="Similarity",
        ascending=False
    )

    recommendations = recommendations[
        ~recommendations["Movie"].isin(
            favorite_movies
        )
    ]

    result_box.insert(
        tk.END,
        "🎬 Recommended Movies\n\n"
    )

    for _, row in recommendations.head(5).iterrows():

        result_box.insert(
            tk.END,
            f"{row['Movie']} - "
            f"{round(row['Similarity']*100,2)}%\n"
        )

# GUI Window

window = tk.Tk()

window.title(
    "AI Movie Recommendation System"
)

window.geometry("700x500")

# Title

title = tk.Label(
    window,
    text="🎬 AI Movie Recommendation System",
    font=("Arial", 16)
)

title.pack(pady=10)

# Available Movies

movies_label = tk.Label(
    window,
    text="Available Movies:\nAvengers, Iron Man, Captain America, Thor, Titanic, The Notebook, Interstellar, Inception"
)

movies_label.pack(pady=5)

# Input

entry = tk.Entry(
    window,
    width=70
)

entry.pack(pady=10)

# Button

button = tk.Button(
    window,
    text="Get Recommendations",
    command=recommend
)

button.pack(pady=10)

# Output

result_box = scrolledtext.ScrolledText(
    window,
    width=80,
    height=15
)

result_box.pack(pady=10)

# Run App

window.mainloop()