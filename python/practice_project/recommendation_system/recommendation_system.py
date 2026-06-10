# Project 10
# Recommendation Dashboard

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🎬 Recommendation Dashboard Started\n")

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

print("Available Movies:\n")
print(df["Movie"].tolist())

movie_name = input(
    "\nEnter Movie Name: "
)

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

    recommendations = []

    rank = 1

    for item in similarity_scores:

        idx = item[0]
        score = item[1]

        if df["Movie"][idx] != movie_name:

            recommendations.append(
                [
                    rank,
                    df["Movie"][idx],
                    round(score, 3)
                ]
            )

            rank += 1

        if rank > 5:
            break

    dashboard = pd.DataFrame(
        recommendations,
        columns=[
            "Rank",
            "Movie",
            "Similarity"
        ]
    )

    print("\n🎬 Recommendation Dashboard\n")

    print(dashboard)