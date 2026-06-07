# Project 10
# Movie Recommendation System

import pandas as pd

print("🎬 Movie Recommendation System Started\n")

# Movie Dataset

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

print(df)