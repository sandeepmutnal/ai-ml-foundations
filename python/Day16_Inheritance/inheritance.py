# Day 16 - Inheritance in Python
# Single, Multiple, and Multilevel Inheritance

# 1. Single Inheritance
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

child = Child()
child.show_parent()
child.show_child()

print("-----")

# 2. Multilevel Inheritance
class GrandParent:
    def show_grandparent(self):
        print("This is GrandParent class")

class Parent2(GrandParent):
    def show_parent(self):
        print("This is Parent class")

class Child2(Parent2):
    def show_child(self):
        print("This is Child class")

obj = Child2()
obj.show_grandparent()
obj.show_parent()
obj.show_child()

print("-----")

# 3. Multiple Inheritance
class Father:
    def father_name(self):
        print("Father name")

class Mother:
    def mother_name(self):
        print("Mother name")

class Child3(Father, Mother):
    def child_name(self):
        print("Child name")

child3 = Child3()
child3.father_name()
child3.mother_name()
child3.child_name()
