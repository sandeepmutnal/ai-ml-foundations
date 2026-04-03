# Practice Day 21
# Real Dataset Analysis Project

import pandas as pd
import matplotlib.pyplot as plt


# 1️⃣ Load CSV dataset

df = pd.read_csv("students.csv")

print("Original Dataset:\n")
print(df)


# 2️⃣ Dataset Information

print("\nDataset Info:\n")
print(df.info())


# 3️⃣ Handle Missing Values

df["Math"].fillna(df["Math"].mean(), inplace=True)
df["Science"].fillna(df["Science"].mean(), inplace=True)

print("\nAfter Handling Missing Values:\n")
print(df)


# 4️⃣ Add Total Marks Column

df["Total"] = df["Math"] + df["Science"] + df["English"]

print("\nDataset with Total Marks:\n")
print(df)


# 5️⃣ Sort Dataset by Total Marks

sorted_df = df.sort_values("Total", ascending=False)

print("\nSorted Dataset:\n")
print(sorted_df)


# 6️⃣ Find Top Performer

top_student = sorted_df.iloc[0]

print("\nTop Performer:\n")
print(top_student)


# 7️⃣ Visualization

plt.bar(df["Name"], df["Total"])

plt.title("Total Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Total Marks")

plt.show()


# 8️⃣ Save Processed Dataset

df.to_csv("students_processed.csv", index=False)

print("\nProcessed dataset saved successfully!")