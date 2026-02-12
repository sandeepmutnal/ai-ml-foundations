# Day 13 - Classes and Objects in Python

# Creating a class
class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating objects
student1 = Student("Sandeep", 22, "Python")
student2 = Student("Ravi", 21, "AI")

# Calling methods using objects
student1.display_details()
print("-----")
student2.display_details()
