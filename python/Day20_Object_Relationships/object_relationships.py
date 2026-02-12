# Day 20 - Object Relationships in Python
# Composition and Aggregation

# 1. Composition Example
class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print(f"Engine with power {self.power} started.")

class Car:
    def __init__(self, model):
        self.model = model
        # Composition: Car contains Engine (created inside Car)
        self.engine = Engine(150)

    def start_car(self):
        print(f"{self.model} car is starting...")
        self.engine.start()

car1 = Car("BMW")
car1.start_car()

print("-----")

# 2. Aggregation Example
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, name, books):
        self.name = name
        # Aggregation: Library has Books (passed from outside)
        self.books = books

    def show_books(self):
        for book in self.books:
            print(book.title)

b1 = Book("Python Basics")
b2 = Book("OOP Concepts")
my_library = Library("City Library", [b1, b2])
my_library.show_books()
