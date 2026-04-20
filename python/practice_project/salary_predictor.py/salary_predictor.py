# Project 2
# Salary Predictor AI Model

import pandas as pd


# Dataset

data = {
    "Experience": [1,2,3,4,5,6,7,8,9,10],
    "Salary": [2,3,4,5,6.5,7.5,8.5,9.5,10.5,12]
}


df = pd.DataFrame(data)


print("Salary Dataset Loaded Successfully ✅\n")
print(df)