# Practice Day 14
# Topics: Virtual Environment + pip + Libraries

# Import numpy
import numpy as np

# Create numpy array
arr = np.array([1, 2, 3, 4, 5])

print("Numpy array:", arr)


# Import pandas
import pandas as pd

# Create dataframe
data = {
    "Name": ["Sandeep", "Rahul", "Priya"],
    "Age": [22, 23, 21]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# Simple dataframe operation
print("\nColumn Names:")
print(df.columns)


print("\nAverage Age:")
print(df["Age"].mean())