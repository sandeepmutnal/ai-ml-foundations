# Day 19 - Special Methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages


b1 = Book("Python Basics", 120)

print(b1)          # __str__
print(repr(b1))    # __repr__
print(len(b1))     # __len__
