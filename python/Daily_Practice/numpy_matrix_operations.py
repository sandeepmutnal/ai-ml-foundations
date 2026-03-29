# Practice Day 16
# Topic: NumPy Matrix Operations (2D Arrays)

import numpy as np


# 1️⃣ Create 2D array (matrix)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Matrix:\n", matrix)


# 2️⃣ Shape of matrix

print("Shape:", matrix.shape)


# 3️⃣ Reshape array

arr = np.arange(1, 10)

reshaped = arr.reshape(3, 3)

print("\nReshaped Matrix:\n", reshaped)


# 4️⃣ Row indexing

print("\nFirst row:", reshaped[0])


# 5️⃣ Column indexing

print("Second column:", reshaped[:, 1])


# 6️⃣ Matrix addition

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("\nMatrix Addition:\n", a + b)


# 7️⃣ Matrix multiplication

print("\nMatrix Multiplication:\n", np.dot(a, b))


# 8️⃣ Transpose matrix

print("\nTranspose:\n", reshaped.T)


# 9️⃣ Flatten matrix

print("\nFlattened Matrix:\n", reshaped.flatten())