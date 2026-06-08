# Project 10
# Movie Recommendation System

import pandas as pd

print("🎬 Movie Recommendation System Started\n")

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

    "Genre": [
        "Action",
        "Action",
        "Action",
        "Action",
        "Romance",
        "Romance",
        "Sci-Fi",
        "Sci-Fi"
    ]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")


# Function to Recommend Movies

def recommend_movies(movie_name):

    # Find genre of selected movie
    selected_genre = df[df["Movie"] == movie_name]["Genre"].values[0]

    print(f"\n🎯 Selected Movie: {movie_name}")
    print(f"🎭 Genre: {selected_genre}\n")

    # Recommend similar movies
    recommendations = df[
        (df["Genre"] == selected_genre) &
        (df["Movie"] != movie_name)
    ]

    print("🎬 Recommended Movies:\n")

    for movie in recommendations["Movie"]:
        print("👉", movie)


# User Input

print("Enter a movie name from dataset:")
user_movie = input()

# Check and Recommend

if user_movie in df["Movie"].values:
    recommend_movies(user_movie)
else:
    print("❌ Movie not found in dataset")