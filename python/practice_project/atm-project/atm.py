correct_pin = 1234
balance = 10000
attempts = 0

# PIN verification
while attempts < 3:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("PIN verified successfully")
        break
    else:
        attempts += 1
        print("Incorrect PIN")

if attempts == 3:
    print("Card blocked. Too many attempts.")
else:
    # ATM Menu
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        choice = int(input("Choose option: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")

        elif choice == 3:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid option")
