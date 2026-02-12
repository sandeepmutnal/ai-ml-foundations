# Day 04 - Input and Output in Python

# 1. Taking input from user
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)

# 2. Input is always string by default
# Convert string to integer
age = int(age)

# 3. Basic print formatting
print("Name:", name)
print("Age:", age)

# 4. Using f-string (recommended)
print(f"My name is {name} and I am {age} years old")

# 5. Taking multiple inputs
city = input("Enter your city: ")
course = input("Enter your course: ")

print(f"I live in {city} and I am learning {course}")
