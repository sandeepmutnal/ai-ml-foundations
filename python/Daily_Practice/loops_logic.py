# Practice Day 02
# Topics: Loops, Conditionals, Logic Building

# 1️⃣ Print numbers from 1 to 10
print("Numbers from 1 to 10")
for i in range(1, 11):
    print(i)


# 2️⃣ Print even numbers from 1 to 20
print("\nEven numbers from 1 to 20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 3️⃣ Sum of numbers from 1 to 100
total = 0

for i in range(1, 101):
    total += i

print("\nSum of numbers 1 to 100:", total)


# 4️⃣ Multiplication Table
num = int(input("\nEnter a number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 5️⃣ Check Positive / Negative / Zero
number = int(input("\nEnter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# 6️⃣ Find Largest Number in List
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("\nLargest number:", largest)


# 7️⃣ Count numbers in a list
nums = [1,2,3,4,5,6,7]

count = 0

for n in nums:
    count += 1

print("Total numbers in list:", count)