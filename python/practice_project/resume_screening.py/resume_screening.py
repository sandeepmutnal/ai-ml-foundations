# Project 9
# Resume Screening AI System

import pandas as pd

print("📄 Resume Screening AI System Started\n")


# Sample Resume Dataset

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

print(df)