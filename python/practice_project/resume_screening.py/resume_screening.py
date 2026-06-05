# Project 9
# Resume Screening Dashboard

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("📄 Resume Screening Dashboard Started\n")

# Dataset

data = {
    "Resume": [
        "Python developer with experience in machine learning and data analysis",
        "Web developer skilled in HTML CSS JavaScript and React",
        "Data scientist with Python SQL and machine learning knowledge",
        "Android developer with Java and Kotlin experience",
        "AI engineer working on deep learning and NLP projects"
    ],

    "Name": [
        "Aarav",
        "Diya",
        "Rohan",
        "Kiran",
        "Sana"
    ]
}

df = pd.DataFrame(data)

# User Job Description

job_description = input("Enter Job Description: ")

# Vectorization

vectorizer = TfidfVectorizer()

resume_vectors = vectorizer.fit_transform(df["Resume"])

job_vector = vectorizer.transform([job_description])

# Similarity Scores

scores = cosine_similarity(
    job_vector,
    resume_vectors
)[0]

# Add Score Column

df["Score"] = scores

# Sort

df = df.sort_values(
    by="Score",
    ascending=False
)

# Add Rank

df["Rank"] = range(1, len(df) + 1)

# Dashboard Table

dashboard = df[
    ["Rank", "Name", "Score"]
]

print("\n🏆 Candidate Dashboard\n")

print(dashboard)

# Best Candidate

best = df.iloc[0]

print("\n🥇 Best Candidate:")
print(best["Name"])

print("Score:", round(best["Score"], 3))