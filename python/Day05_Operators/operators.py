# Day 05 - Operators in Python

# 1. Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus
print(a ** b)  # Power
print(a // b)  # Floor Division

# 2. Comparison Operators
print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater or equal
print(a <= b)  # Less or equal

# 3. Logical Operators
x = True
y = False

print(x and y)
print(x or y)
print(not x)

# 4. Assignment Operators
c = 5
c += 2
print(c)

# 5. Bitwise Operators
m = 5   # 0101
n = 3   # 0011

print(m & n)   # AND
print(m | n)   # OR
print(m ^ n)   # XOR
print(~m)      # NOT
print(m << 1)  # Left shift
print(m >> 1)  # Right shift

# 6. Membership Operators
numbers = [1, 2, 3, 4]
print(2 in numbers)
print(5 not in numbers)

# 7. Identity Operators
p = [1, 2]
q = [1, 2]
r = p

print(p is r)
print(p is q)
print(p is not q)
