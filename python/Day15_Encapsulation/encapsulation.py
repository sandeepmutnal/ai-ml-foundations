# Day 15 - Encapsulation in Python
# Public, Protected, and Private attributes

class BankAccount:

    def __init__(self, owner, balance):
        # Public attribute
        self.owner = owner

        # Protected attribute (by convention)
        self._balance = balance

        # Private attribute (name mangling)
        self.__account_type = "Savings"

    # Public method
    def show_account(self):
        print("Owner:", self.owner)
        print("Balance:", self._balance)
        print("Account Type:", self.__account_type)

    # Public method to update protected attribute
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Amount deposited:", amount)

    # Public method to access private attribute
    def get_account_type(self):
        return self.__account_type


# Creating object
account = BankAccount("Sandeep", 5000)

# Accessing public attribute
print(account.owner)

# Accessing protected attribute (possible, but not recommended)
print(account._balance)

# Accessing private attribute using method
print(account.get_account_type())

# Using methods
account.deposit(2000)
account.show_account()
