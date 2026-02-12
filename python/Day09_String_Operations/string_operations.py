# Day 09 - String Operations in Python

text = "Hello Python World"

# 1. Indexing
print(text[0])    # First character
print(text[-1])   # Last character

# 2. Slicing
print(text[0:5])      # Hello
print(text[6:12])     # Python
print(text[:5])       # Hello
print(text[6:])       # Python World

# 3. String methods
print(text.upper())       # Convert to uppercase
print(text.lower())       # Convert to lowercase
print(text.split())       # Split into list
print(text.replace("World", "Developer"))

# 4. Length of string
print(len(text))

# 5. Check substring
print("Python" in text)
print("Java" not in text)

# 6. Remove spaces
sample = "   Hello   "
print(sample.strip())
