# Practice Day 15
# Topic: NumPy Arrays (AI/ML Foundation)

import numpy as np


# 1️⃣ Creating numpy array

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)


# 2️⃣ Array from range

arr2 = np.arange(1, 11)

print("Array 1 to 10:", arr2)


# 3️⃣ Zeros array

zeros_array = np.zeros(5)

print("Zeros array:", zeros_array)


# 4️⃣ Ones array

ones_array = np.ones(5)

print("Ones array:", ones_array)


# 5️⃣ Array indexing

print("First element:", arr[0])


# 6️⃣ Array slicing

print("Slice (1 to 3):", arr[1:4])


# 7️⃣ Array math operations

print("Addition:", arr + 5)

print("Multiplication:", arr * 2)


# 8️⃣ Statistics operations

print("Sum:", np.sum(arr))

print("Mean:", np.mean(arr))

print("Max:", np.max(arr))

print("Min:", np.min(arr))


# 9️⃣ Shape (Very important in ML)

matrix = np.array([[1, 2], [3, 4]])

print("Matrix:\n", matrix)

print("Shape:", matrix.shape)