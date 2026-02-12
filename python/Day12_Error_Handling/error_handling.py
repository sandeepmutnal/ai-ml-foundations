# Day 12 - Basic Error Handling in Python

# 1. try and except
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a number.")

print("Program continues...")

# 2. Handling multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")

# 3. finally block
try:
    file = open("test.txt", "w")
    file.write("Error handling example")
except Exception as e:
    print("Error occurred:", e)
finally:
    file.close()
    print("File closed successfully")
