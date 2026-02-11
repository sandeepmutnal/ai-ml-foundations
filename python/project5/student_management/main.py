import json
import os

FILE = "students.json"


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }


def load_students():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_students(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = Student(name, age, marks)
    data = load_students()
    data.append(student.to_dict())
    save_students(data)

    print("Student added successfully!")


def view_students():
    data = load_students()

    if not data:
        print("No students found.")
        return

    for s in data:
        print(s["name"], "| Age:", s["age"], "| Marks:", s["marks"])


def menu():
    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


menu()
