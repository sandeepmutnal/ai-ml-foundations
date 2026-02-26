import math

# ---------- GLOBAL ----------
history = []
last_result = None

# ---------- OPERATIONS ----------
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    return "❌ Cannot divide by zero" if b == 0 else a / b

def power(a, b): return a ** b

def square_root(a):
    return "❌ Negative number not allowed" if a < 0 else math.sqrt(a)

def percentage(a, b):
    return (a / 100) * b

# ---------- SCIENTIFIC ----------
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def log(x):
    return "❌ Invalid input" if x <= 0 else math.log10(x)

# ---------- HISTORY ----------
def add_to_history(record):
    history.append(record)

def show_history():
    if not history:
        print("📭 No history")
    else:
        print("\n📜 HISTORY")
        print("-" * 30)
        for item in history:
            print(item)

def undo_last():
    if history:
        removed = history.pop()
        print(f"↩️ Removed: {removed}")
    else:
        print("❌ Nothing to undo")

# ---------- MENU ----------
def menu():
    print("\n" + "="*40)
    print("🧮 ADVANCED CALCULATOR v2")
    print("="*40)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. sin(x)")
    print("9. cos(x)")
    print("10. log(x)")
    print("11. Show History")
    print("12. Undo Last")
    print("13. Use Last Result")
    print("14. Exit")

# ---------- INPUT ----------
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("❌ Invalid input")

# ---------- MAIN ----------
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "14":
        print("👋 Goodbye!")
        break

    elif choice == "11":
        show_history()
        continue

    elif choice == "12":
        undo_last()
        continue

    elif choice == "13":
        if last_result is None:
            print("❌ No previous result")
        else:
            print("👉 Last Result:", last_result)
        continue

    # ---------- SINGLE INPUT ----------
    elif choice in ["6","8","9","10"]:
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

        print("Result:", result)
        add_to_history(f"{exp} = {result}")
        last_result = result

    # ---------- DOUBLE INPUT ----------
    elif choice in ["1","2","3","4","5","7"]:
        print("👉 Type 'M' to use last result")

        val1 = input("Enter first number: ")
        if val1.lower() == "m" and last_result is not None:
            num1 = last_result
        else:
            num1 = float(val1)

        val2 = input("Enter second number: ")
        if val2.lower() == "m" and last_result is not None:
            num2 = last_result
        else:
            num2 = float(val2)

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op = "/"
        elif choice == "5":
            result = power(num1, num2)
            op = "^"
        elif choice == "7":
            result = percentage(num1, num2)
            op = "% of"

        print("Result:", result)
        add_to_history(f"{num1} {op} {num2} = {result}")
        last_result = result

    else:
        print("❌ Invalid choice")