# Day 10 - List, Tuple, Set, Dictionary in Python

# 1. List
fruits = ["apple", "banana", "mango"]
print(fruits)

# Indexing
print(fruits[0])

# Add elements
fruits.append("orange")
print(fruits)

# Remove elements
fruits.remove("banana")
print(fruits)

# Looping
for fruit in fruits:
    print(fruit)

print("-----")

# 2. Tuple
colors = ("red", "green", "blue")
print(colors)

# Indexing
print(colors[1])

# Looping
for color in colors:
    print(color)

print("-----")

# 3. Set
numbers = {1, 2, 3}
print(numbers)

# Add element
numbers.add(4)
print(numbers)

# Remove element
numbers.remove(2)
print(numbers)

# Looping
for num in numbers:
    print(num)

print("-----")

# 4. Dictionary
student = {
    "name": "Sandeep",
    "age": 22,
    "course": "Python"
}
print(student)

# Access value
print(student["name"])

# Add / update value
student["age"] = 23
student["city"] = "Bangalore"
print(student)

# Remove key
student.pop("city")
print(student)

# Looping
for key, value in student.items():
    print(key, ":", value)
