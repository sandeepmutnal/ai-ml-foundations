# Day 06 - Conditional Statements in Python

# 1. if statement
age = 18

if age >= 18:
    print("You are eligible to vote")

# 2. if - else statement
marks = 45

if marks >= 40:
    print("You passed the exam")
else:
    print("You failed the exam")

# 3. if - elif - else statement
score = 72

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# Real-world example
balance = 5000
withdraw = 3000

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")
