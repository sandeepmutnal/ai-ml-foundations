# Project 10
# TF-IDF Movie Recommendation System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🎬 TF-IDF Movie Recommendation System Started\n")

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

# Similarity Matrix

similarity_matrix = cosine_similarity(
    tfidf_matrix
)

print("Dataset Loaded Successfully ✅")

# User Input

movie_name = input(
    "\nEnter a movie name: "
)

# Check Movie

if movie_name not in df["Movie"].values:
    print("❌ Movie not found")
else:

    movie_index = df[
        df["Movie"] == movie_name
    ].index[0]

    similarity_scores = list(
        enumerate(
            similarity_matrix[movie_index]
        )
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\n🎬 Recommended Movies:\n")

    count = 0

    for i in similarity_scores:

        movie_idx = i[0]

        if df["Movie"][movie_idx] != movie_name:

            print(
                df["Movie"][movie_idx],
                "- Similarity:",
                round(i[1], 3)
            )

            count += 1

        if count == 3:
            break