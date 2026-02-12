# Day 14 - Attributes and Methods in Python

class Student:
    # Class variable (shared by all objects)
    college = "ABC Engineering College"

    def __init__(self, name, age):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age

    # Instance method
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)

    # Class method
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


# Creating objects
student1 = Student("Sandeep", 22)
student2 = Student("Ravi", 17)

# Instance method call
student1.show_details()
print("-----")

# Class method call
Student.change_college("XYZ University")

student2.show_details()
print("-----")

# Static method call
print("Is Sandeep adult?", Student.is_adult(22))
print("Is Ravi adult?", Student.is_adult(17))
