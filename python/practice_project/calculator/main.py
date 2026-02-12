


# 📄 main.py (FULL WORKING CODE)


# ==================================
# Python CLI Calculator
# Project 2
# ==================================

import math

# ---------- FUNCTIONS ----------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)

# ---------- MENU FUNCTION ----------

def show_menu():
    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Exit")

# ---------- MAIN PROGRAM ----------

print("=================================")
print("🧮 Welcome to Python CLI Calculator 🧮")
print("=================================")

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice (1-9): "))
        
        if choice == 9:
            print("👋 Goodbye!")
            break

        if choice not in range(1, 9):
            print("❌ Invalid choice. Try again.")
            continue

        if choice == 8:
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
            elif choice == 5:
                print("Result:", modulus(num1, num2))
            elif choice == 6:
                print("Result:", power(num1, num2))
            elif choice == 7:
                print("Result:", floor_division(num1, num2))

    except ValueError:
        print("❌ Please enter valid numbers.")
