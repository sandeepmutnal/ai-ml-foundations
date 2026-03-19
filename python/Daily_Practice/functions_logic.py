# Practice Day 05
# Topics: Functions, Parameters, Return, Logic

# 1️⃣ Simple Function
def greet():
    print("Hello, welcome to Python")

greet()


# 2️⃣ Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Sandeep")


# 3️⃣ Function with return value
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)


# 4️⃣ Check Even or Odd using function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))


# 5️⃣ Find maximum of 3 numbers
def find_max(a, b, c):
    return max(a, b, c)

print("Max:", find_max(10, 25, 15))


# 6️⃣ Count vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

print("Vowels:", count_vowels("education"))


# 7️⃣ Factorial using function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print("Factorial:", factorial(5))