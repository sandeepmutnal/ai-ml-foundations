# Project 9
# Resume Screening AI System (GUI)

import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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


# TF-IDF Model

vectorizer = TfidfVectorizer()
resume_vectors = vectorizer.fit_transform(df["Resume"])


# GUI Function

def analyze_resumes():

    job_description = entry.get()

    if not job_description.strip():
        result_box.insert(tk.END, "Please enter job description\n")
        return

    job_vector = vectorizer.transform([job_description])

    scores = cosine_similarity(job_vector, resume_vectors)[0]

    df["Score"] = scores

    sorted_df = df.sort_values(by="Score", ascending=False)

    sorted_df["Rank"] = range(1, len(sorted_df) + 1)

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, "🏆 Candidate Ranking:\n\n")

    for _, row in sorted_df.iterrows():
        result_box.insert(
            tk.END,
            f"{row['Rank']}. {row['Name']} - {round(row['Score']*100,2)}%\n"
        )

    best = sorted_df.iloc[0]

    result_box.insert(tk.END, "\n🥇 Best Candidate:\n")
    result_box.insert(tk.END, f"{best['Name']} ({round(best['Score']*100,2)}%)\n")


# GUI Window

window = tk.Tk()
window.title("Resume Screening AI System")
window.geometry("650x500")


# Title

title = tk.Label(
    window,
    text="AI Resume Screening System",
    font=("Arial", 16)
)

title.pack(pady=10)


# Input Box

entry = tk.Entry(window, width=60)
entry.pack(pady=10)


# Button

btn = tk.Button(
    window,
    text="Analyze Candidates",
    command=analyze_resumes
)

btn.pack(pady=10)


# Output Area

result_box = scrolledtext.ScrolledText(
    window,
    width=70,
    height=20
)

result_box.pack(pady=10)


# Run App

window.mainloop()