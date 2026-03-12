import math
import random

# ---------------- GLOBAL VARIABLES ----------------
history = []
last_result = None
memory = None
last_operation = None

# ---------------- BASIC OPERATIONS ----------------
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b

def power(a, b): return a ** b

def square_root(a):
    if a < 0:
        return "❌ Negative number not allowed"
    return math.sqrt(a)

def percentage(a, b):
    return (a / 100) * b

def minimum(a, b): return min(a, b)
def maximum(a, b): return max(a, b)

# ---------------- SCIENTIFIC ----------------
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))

def log(x):
    if x <= 0:
        return "❌ Invalid input"
    return math.log10(x)

def factorial(x):
    if x < 0:
        return "❌ Negative number not allowed"
    return math.factorial(int(x))

# ---------------- EXTRA FEATURES ----------------
def random_number(a, b):
    return random.randint(int(a), int(b))

def average(nums):
    return sum(nums) / len(nums)

def even_odd(n):
    return "Even" if int(n) % 2 == 0 else "Odd"

# ---------------- PRIME CHECK ----------------
def prime_check(n):

    n = int(n)

    if n <= 1:
        return "Not Prime"

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

# ---------------- TEMPERATURE ----------------
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# ---------------- NUMBER GUESS GAME ----------------
def guess_game():

    number = random.randint(1, 10)

    print("🎮 Guess the number (1-10)")

    guess = int(input("Enter guess: "))

    if guess == number:
        print("🎉 Correct!")
    else:
        print("❌ Wrong. Number was:", number)

# ---------------- HISTORY ----------------
def add_to_history(record):
    history.append(record)

def show_history():

    if not history:
        print("📭 No history")
        return

    print("\n📜 HISTORY")
    print("-"*35)

    for item in history:
        print(item)

def clear_history():
    history.clear()
    print("🧹 History cleared")

# ---------------- FILE SAVE ----------------
def save_history():

    with open("calculator_history.txt", "w") as f:
        for item in history:
            f.write(item + "\n")

    print("💾 History saved")

def load_history():

    try:
        with open("calculator_history.txt") as f:
            for line in f:
                history.append(line.strip())

        print("📂 History loaded")

    except:
        print("❌ No file found")

# ---------------- MENU ----------------
def menu():

    print("\n" + "="*50)
    print("🧮 ADVANCED PYTHON CALCULATOR v6")
    print("="*50)

    print("1  Add")
    print("2  Subtract")
    print("3  Multiply")
    print("4  Divide")
    print("5  Power")

    print("6  Square Root")
    print("7  Percentage")

    print("8  sin(x)")
    print("9  cos(x)")
    print("10 log(x)")

    print("11 Minimum")
    print("12 Maximum")

    print("13 Show History")
    print("14 Clear History")

    print("15 Store Memory")
    print("16 Recall Memory")

    print("17 Factorial")
    print("18 Random Number")

    print("19 Average")
    print("20 Even / Odd")

    print("21 Prime Check")

    print("22 Celsius → Fahrenheit")
    print("23 Fahrenheit → Celsius")

    print("24 Number Guess Game")

    print("25 Save History")
    print("26 Load History")

    print("27 Exit")

# ---------------- INPUT ----------------
def get_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except:
            print("❌ Invalid number")

# ---------------- MAIN LOOP ----------------
while True:

    menu()

    choice = input("Enter choice: ")

# ---------------- EXIT ----------------
    if choice == "27":
        print("👋 Goodbye")
        break

# ---------------- HISTORY ----------------
    elif choice == "13":
        show_history()
        continue

    elif choice == "14":
        clear_history()
        continue

# ---------------- MEMORY ----------------
    elif choice == "15":

        if last_result is not None:
            memory = last_result
            print("💾 Stored:", memory)

        else:
            print("❌ No result")

        continue

    elif choice == "16":

        if memory is not None:
            print("📌 Memory:", memory)
        else:
            print("❌ Memory empty")

        continue

# ---------------- FILE ----------------
    elif choice == "25":
        save_history()
        continue

    elif choice == "26":
        load_history()
        continue

# ---------------- GAME ----------------
    elif choice == "24":
        guess_game()
        continue

# ---------------- SINGLE INPUT ----------------
    elif choice in ["6","8","9","10","17","20","21","22","23"]:

        num = get_number("Enter number: ")

        if choice == "6":
            result = square_root(num)
            exp = f"√{num}"

        elif choice == "8":
            result = sin(num)
            exp = f"sin({num})"

        elif choice == "9":
            result = cos(num)
            exp = f"cos({num})"

        elif choice == "10":
            result = log(num)
            exp = f"log({num})"

        elif choice == "17":
            result = factorial(num)
            exp = f"{num}!"

        elif choice == "20":
            result = even_odd(num)
            exp = f"{num}"

        elif choice == "21":
            result = prime_check(num)
            exp = f"{num}"

        elif choice == "22":
            result = c_to_f(num)
            exp = f"{num}C"

        elif choice == "23":
            result = f_to_c(num)
            exp = f"{num}F"

        print("Result:", result)

        add_to_history(f"{exp} = {result}")
        last_result = result

# ---------------- TWO INPUT ----------------
    elif choice in ["1","2","3","4","5","7","11","12","18"]:

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            result = add(a,b)
            op = "+"

        elif choice == "2":
            result = subtract(a,b)
            op = "-"

        elif choice == "3":
            result = multiply(a,b)
            op = "*"

        elif choice == "4":
            result = divide(a,b)
            op = "/"

        elif choice == "5":
            result = power(a,b)
            op = "^"

        elif choice == "7":
            result = percentage(a,b)
            op = "% of"

        elif choice == "11":
            result = minimum(a,b)
            op = "min"

        elif choice == "12":
            result = maximum(a,b)
            op = "max"

        elif choice == "18":
            result = random_number(a,b)
            op = "random"

        print("Result:", result)

        add_to_history(f"{a} {op} {b} = {result}")
        last_result = result

# ---------------- AVERAGE ----------------
    elif choice == "19":

        count = int(get_number("How many numbers: "))

        nums = []

        for i in range(count):
            nums.append(get_number(f"Number {i+1}: "))

        result = average(nums)

        print("Average:", result)

        add_to_history(f"Average {nums} = {result}")
        last_result = result

    else:
        print("❌ Invalid choice")