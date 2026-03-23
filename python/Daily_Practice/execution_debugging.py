# Practice Day 10
# Topics: Execution Flow, Debugging, Tracebacks, Logic Thinking


# 1️⃣ Execution Flow Example

print("Start Program")

def greet():
    print("Inside function")

greet()

print("End Program")


# 2️⃣ Understanding Order of Execution

def step1():
    print("Step 1 running")

def step2():
    print("Step 2 running")

step1()
step2()


# 3️⃣ Debugging Example (fix logic)

num = 5

if num > 10:
    print("Greater than 10")
else:
    print("Less than or equal to 10")


# 4️⃣ Traceback Example (Error Understanding)

numbers = [1, 2, 3]

# Uncomment this line to see traceback error
# print(numbers[5])


# 5️⃣ Fix ZeroDivisionError

a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")


# 6️⃣ Logical Thinking Example

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 7️⃣ Nested Execution Example

for i in range(3):
    print("Outer loop:", i)

    for j in range(2):
        print("Inner loop:", j)