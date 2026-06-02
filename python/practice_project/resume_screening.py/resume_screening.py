# Project 9
# Resume Screening AI System

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("📄 Resume Screening AI System Started\n")


# Dataset

data = {
    "Resume": [
        "Python developer with experience in machine learning and data analysis",
        "Web developer skilled in HTML CSS JavaScript and React",
        "Data scientist with Python SQL and machine learning knowledge",
        "Android developer with Java and Kotlin experience",
        "AI engineer working on deep learning and NLP projects"
    ],

    "Job_Role": [
        "Data Scientist",
        "Web Developer",
        "Data Scientist",
        "Mobile Developer",
        "AI Engineer"
    ]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully ✅\n")


# Resume Text

resumes = df["Resume"]


# TF-IDF Vectorization

vectorizer = TfidfVectorizer()

resume_vectors = vectorizer.fit_transform(resumes)

print("TF-IDF Vectorization Completed ✅")

print("\nShape:")
print(resume_vectors.shape)

print("\nFeatures:")
print(vectorizer.get_feature_names_out())