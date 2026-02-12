# Day 08 - Functions in Python

# 1. Basic function
def greet():
    print("Hello, welcome to Python!")

greet()

# 2. Function with parameters
def greet_user(name):
    print(f"Hello, {name}")

greet_user("Sandeep")

# 3. Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# 4. Default arguments
def greet_with_default(name="User"):
    print(f"Hello, {name}")

greet_with_default()
greet_with_default("Sandeep")

# 5. Keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=22, name="Sandeep")

# 6. Variable-length arguments (*args)
def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4))

# 7. Variable-length keyword arguments (**kwargs)
def student_details(**details):
    print(details)

student_details(name="Sandeep", course="Python", level="Beginner")

# 8. Lambda function
square = lambda x: x * x
print(square(5))
