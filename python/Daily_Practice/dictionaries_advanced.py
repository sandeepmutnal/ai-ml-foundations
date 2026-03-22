# Practice Day 08
# Topics: Dictionaries Advanced + Logic Problems

# 1️⃣ Create dictionary
student = {
    "name": "Sandeep",
    "age": 22,
    "course": "Python"
}

print("Student dictionary:", student)


# 2️⃣ Add new key
student["city"] = "Shimoga"
print("Updated dictionary:", student)


# 3️⃣ Update value
student["age"] = 23
print("Updated age:", student)


# 4️⃣ Loop dictionary keys and values
for key, value in student.items():
    print(key, ":", value)


# 5️⃣ Count frequency of elements using dictionary
nums = [1,1,2,3,3,3,4]

frequency = {}

for n in nums:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print("Frequency:", frequency)


# 6️⃣ Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print("Merged dictionary:", merged)