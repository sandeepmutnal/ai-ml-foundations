# Project 9
# Interactive Resume Screening AI System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("📄 Interactive Resume Screening AI System Started\n")


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


# TF-IDF Vectorization

vectorizer = TfidfVectorizer()

resume_vectors = vectorizer.fit_transform(df["Resume"])


# USER INPUT (Interactive)

print("🧑 Enter Job Description:")
job_description = input()


# Convert Job Description into Vector

job_vector = vectorizer.transform([job_description])


# Similarity Calculation

similarity_scores = cosine_similarity(job_vector, resume_vectors)[0]


# Add Scores

df["Score"] = similarity_scores


# Sort Candidates

df_sorted = df.sort_values(by="Score", ascending=False)


# Output Ranking

print("\n🏆 Candidate Ranking:\n")

for index, row in df_sorted.iterrows():
    print(f"{row['Name']} - Score: {round(row['Score'], 3)}")


# Best Candidate

best_candidate = df_sorted.iloc[0]

print("\n🥇 Best Match:")
print(best_candidate["Name"], "with score", round(best_candidate["Score"], 3))