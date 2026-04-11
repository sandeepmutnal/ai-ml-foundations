# Practice Day 29
# Data Visualization using Matplotlib

import matplotlib.pyplot as plt


# 1️⃣ Dataset

study_hours = [2, 4, 6, 8, 10]
marks = [40, 50, 65, 80, 95]


# 2️⃣ Create Plot

plt.plot(study_hours, marks)


# 3️⃣ Add Labels

plt.xlabel("Study Hours")
plt.ylabel("Marks")


# 4️⃣ Add Title

plt.title("Study Hours vs Marks Graph")


# 5️⃣ Show Graph

plt.show()