# Day 11 - Basic File Handling in Python

# 1. Writing to a file
file = open("sample.txt", "w")
file.write("Hello, this is my first file handling program.\n")
file.write("Learning Python File Handling.\n")
file.close()

print("Data written to file")

# 2. Reading from a file
file = open("sample.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()

# 3. Appending to a file
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()

# 4. Reading line by line
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()
