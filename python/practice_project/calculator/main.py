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

# ---------------- STATISTICS ----------------
def average(nums):
    return sum(nums) / len(nums)

def total(nums):
    return sum(nums)

def maximum(nums):
    return max(nums)

def minimum(nums):
    return min(nums)

# ---------------- LCM & GCD ----------------
def gcd(a, b):
    return math.gcd(int(a), int(b))

def lcm(a, b):
    return abs(int(a*b)) // math.gcd(int(a), int(b))

# ---------------- GEOMETRY ----------------
def circle_area(r):
    return math.pi * r * r

def triangle_area(b, h):
    return 0.5 * b * h

# ---------------- TEMPERATURE ----------------
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# ---------------- UNIT CONVERSION ----------------
def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000

# ---------------- MATRIX ADDITION ----------------
def matrix_add():

    print("Matrix size (2x2)")

    m1 = []
    m2 = []

    print("Enter Matrix A")

    for i in range(2):
        row = list(map(float, input().split()))
        m1.append(row)

    print("Enter Matrix B")

    for i in range(2):
        row = list(map(float, input().split()))
        m2.append(row)

    result = [[0,0],[0,0]]

    for i in range(2):
        for j in range(2):
            result[i][j] = m1[i][j] + m2[i][j]

    print("Result Matrix:")

    for r in result:
        print(r)

# ---------------- HISTORY ----------------
def add_history(text):
    history.append(text)

def show_history():

    if not history:
        print("📭 No history")
        return

    print("\n📜 HISTORY")
    print("-"*35)

    for h in history:
        print(h)

def clear_history():
    history.clear()
    print("🧹 History cleared")

# ---------------- FILE ----------------
def save_history():

    with open("history.txt","w") as f:
        for h in history:
            f.write(h+"\n")

    print("💾 History saved")

def load_history():

    try:
        with open("history.txt") as f:
            for line in f:
                history.append(line.strip())

        print("📂 History loaded")

    except:
        print("❌ No file found")

# ---------------- MENU ----------------
def menu():

    print("\n"+"="*50)
    print("🧮 ADVANCED PYTHON CALCULATOR v8")
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
    print("16 Max Number")
    print("17 Min Number")

    print("18 GCD")
    print("19 LCM")

    print("20 Circle Area")
    print("21 Triangle Area")

    print("22 Celsius → Fahrenheit")
    print("23 Fahrenheit → Celsius")

    print("24 KM → Meter")
    print("25 Meter → KM")

    print("26 KG → Gram")
    print("27 Gram → KG")

    print("28 Matrix Addition")

    print("29 Show History")
    print("30 Clear History")

    print("31 Save History")
    print("32 Load History")

    print("33 Exit")

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
    if choice == "33":
        print("👋 Goodbye")
        break

# ---------------- HISTORY ----------------
    elif choice == "29":
        show_history()
        continue

    elif choice == "30":
        clear_history()
        continue

# ---------------- FILE ----------------
    elif choice == "31":
        save_history()
        continue

    elif choice == "32":
        load_history()
        continue

# ---------------- MATRIX ----------------
    elif choice == "28":
        matrix_add()
        continue

# ---------------- SINGLE INPUT ----------------
    elif choice in ["6","7","8","9","10","11","12","20","22","23","24","25","26","27"]:

        n = get_number("Enter number: ")

        if choice == "6":
            result = square_root(n)

        elif choice == "7":
            result = sin(n)

        elif choice == "8":
            result = cos(n)

        elif choice == "9":
            result = log(n)

        elif choice == "10":
            result = factorial(n)

        elif choice == "11":
            result = even_odd(n)

        elif choice == "12":
            result = prime_check(n)

        elif choice == "20":
            result = circle_area(n)

        elif choice == "22":
            result = c_to_f(n)

        elif choice == "23":
            result = f_to_c(n)

        elif choice == "24":
            result = km_to_m(n)

        elif choice == "25":
            result = m_to_km(n)

        elif choice == "26":
            result = kg_to_g(n)

        elif choice == "27":
            result = g_to_kg(n)

        print("Result:", result)
        add_history(f"{n} -> {result}")
        last_result = result

# ---------------- TWO INPUT ----------------
    elif choice in ["1","2","3","4","5","13","18","19","21"]:

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        if choice == "1":
            result = add(a,b)

        elif choice == "2":
            result = subtract(a,b)

        elif choice == "3":
            result = multiply(a,b)

        elif choice == "4":
            result = divide(a,b)

        elif choice == "5":
            result = power(a,b)

        elif choice == "13":
            result = random_number(a,b)

        elif choice == "18":
            result = gcd(a,b)

        elif choice == "19":
            result = lcm(a,b)

        elif choice == "21":
            result = triangle_area(a,b)

        print("Result:", result)
        add_history(f"{a},{b} -> {result}")
        last_result = result

# ---------------- MULTI NUMBERS ----------------
    elif choice in ["14","15","16","17"]:

        count = int(get_number("How many numbers: "))

        nums=[]

        for i in range(count):
            nums.append(get_number(f"Number {i+1}: "))

        if choice == "14":
            result = average(nums)

        elif choice == "15":
            result = total(nums)

        elif choice == "16":
            result = maximum(nums)

        elif choice == "17":
            result = minimum(nums)

        print("Result:", result)
        add_history(f"{nums} -> {result}")
        last_result=result

    else:
        print("❌ Invalid choice")