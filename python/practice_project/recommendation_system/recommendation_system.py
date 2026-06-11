# Project 10
# Personalized Recommendation System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("🎬 Personalized Recommendation System\n")

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

# User Preferences

print("Available Movies:\n")
print(df["Movie"].tolist())

print("\nEnter favorite movies separated by comma:")

user_input = input()

favorite_movies = [
    movie.strip()
    for movie in user_input.split(",")
]

# Create User Profile

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

    print("❌ No valid movies entered")

else:

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

    print("\n🎯 Personalized Recommendations:\n")

    print(
        recommendations[
            ["Movie", "Similarity"]
        ].head(5)
    )