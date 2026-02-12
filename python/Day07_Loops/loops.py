# Day 07 - Loops in Python

# 1. for loop
print("For loop example:")
for i in range(1, 6):
    print(i)

# 2. while loop
print("\nWhile loop example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. break statement
print("\nBreak example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 4. continue statement
print("\nContinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 5. pass statement
print("\nPass example:")
for i in range(1, 4):
    if i == 2:
        pass  # does nothing, placeholder
    print(i)
