import math
import random

# ---------------- GLOBAL VARIABLES ----------------
history = []
last_result = None
memory = None

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
        return "❌ Negative number"
    return math.sqrt(a)

# ---------------- SCIENTIFIC ----------------
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))

def log(x):
    if x <= 0:
        return "❌ Invalid input"
    return math.log10(x)

def factorial(x):
    if x < 0:
        return "❌ Negative number"
    return math.factorial(int(x))

# ---------------- NUMBER FEATURES ----------------
def even_odd(n):
    return "Even" if int(n) % 2 == 0 else "Odd"

def prime_check(n):

    n = int(n)

    if n <= 1:
        return "Not Prime"

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

# ---------------- RANDOM ----------------
def random_number(a, b):
    return random.randint(int(a), int(b))

# ---------------- AVERAGE ----------------
def average(nums):
    return sum(nums) / len(nums)

def total(nums):
    return sum(nums)

# ---------------- LCM & GCD ----------------
def gcd(a, b):
    return math.gcd(int(a), int(b))

def lcm(a, b):
    return abs(int(a*b)) // math.gcd(int(a), int(b))

# ---------------- AREA ----------------
def circle_area(r):
    return math.pi * r * r

def triangle_area(b, h):
    return 0.5 * b * h

# ---------------- TEMPERATURE ----------------
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# ---------------- HISTORY ----------------
def add_history(text):
    history.append(text)

def show_history():

    if not history:
        print("📭 No history yet")
        return

    print("\n📜 HISTORY")
    print("-"*35)

    for item in history:
        print(item)

def clear_history():
    history.clear()
    print("🧹 History cleared")

# ---------------- FILE ----------------
def save_history():

    with open("history.txt","w") as f:
        for h in history:
            f.write(h + "\n")

    print("💾 History saved")

def load_history():

    try:
        with open("history.txt") as f:
            for line in f:
                history.append(line.strip())

        print("📂 History loaded")

    except:
        print("❌ No saved file")

# ---------------- MENU ----------------
def menu():

    print("\n"+"="*50)
    print("🧮 ADVANCED PYTHON CALCULATOR v7")
    print("="*50)

    print("1  Add")
    print("2  Subtract")
    print("3  Multiply")
    print("4  Divide")
    print("5  Power")

    print("6  Square Root")
    print("7  sin(x)")
    print("8  cos(x)")
    print("9  log(x)")

    print("10 Factorial")
    print("11 Even / Odd")
    print("12 Prime Check")

    print("13 Random Number")

    print("14 Average")
    print("15 Sum of Numbers")

    print("16 GCD")
    print("17 LCM")

    print("18 Circle Area")
    print("19 Triangle Area")

    print("20 Celsius → Fahrenheit")
    print("21 Fahrenheit → Celsius")

    print("22 Show History")
    print("23 Clear History")

    print("24 Save History")
    print("25 Load History")

    print("26 Exit")

# ---------------- INPUT ----------------
def get_number(text):

    while True:
        try:
            return float(input(text))
        except:
            print("❌ Invalid number")

# ---------------- MAIN LOOP ----------------
while True:

    menu()

    choice = input("Enter choice: ")

# ---------------- EXIT ----------------
    if choice == "26":
        print("👋 Goodbye")
        break

# ---------------- HISTORY ----------------
    elif choice == "22":
        show_history()
        continue

    elif choice == "23":
        clear_history()
        continue

# ---------------- FILE ----------------
    elif choice == "24":
        save_history()
        continue

    elif choice == "25":
        load_history()
        continue

# ---------------- SINGLE INPUT ----------------
    elif choice in ["6","7","8","9","10","11","12","18","20","21"]:

        n = get_number("Enter number: ")

        if choice == "6":
            result = square_root(n)
            exp = f"√{n}"

        elif choice == "7":
            result = sin(n)
            exp = f"sin({n})"

        elif choice == "8":
            result = cos(n)
            exp = f"cos({n})"

        elif choice == "9":
            result = log(n)
            exp = f"log({n})"

        elif choice == "10":
            result = factorial(n)
            exp = f"{n}!"

        elif choice == "11":
            result = even_odd(n)
            exp = f"{n}"

        elif choice == "12":
            result = prime_check(n)
            exp = f"{n}"

        elif choice == "18":
            result = circle_area(n)
            exp = f"Circle radius {n}"

        elif choice == "20":
            result = c_to_f(n)
            exp = f"{n}C"

        elif choice == "21":
            result = f_to_c(n)
            exp = f"{n}F"

        print("Result:", result)
        add_history(f"{exp} = {result}")
        last_result = result

# ---------------- TWO INPUT ----------------
    elif choice in ["1","2","3","4","5","13","16","17","19"]:

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            result = add(a,b)
            op="+"

        elif choice == "2":
            result = subtract(a,b)
            op="-"

        elif choice == "3":
            result = multiply(a,b)
            op="*"

        elif choice == "4":
            result = divide(a,b)
            op="/"

        elif choice == "5":
            result = power(a,b)
            op="^"

        elif choice == "13":
            result = random_number(a,b)
            op="random"

        elif choice == "16":
            result = gcd(a,b)
            op="gcd"

        elif choice == "17":
            result = lcm(a,b)
            op="lcm"

        elif choice == "19":
            result = triangle_area(a,b)
            op="triangle area"

        print("Result:", result)
        add_history(f"{a} {op} {b} = {result}")
        last_result = result

# ---------------- MULTI NUMBER ----------------
    elif choice in ["14","15"]:

        count = int(get_number("How many numbers: "))

        nums=[]

        for i in range(count):
            nums.append(get_number(f"Number {i+1}: "))

        if choice == "14":
            result = average(nums)
            text="Average"

        else:
            result = total(nums)
            text="Sum"

        print(text+":", result)
        add_history(f"{text} {nums} = {result}")
        last_result=result

    else:
        print("❌ Invalid choice")