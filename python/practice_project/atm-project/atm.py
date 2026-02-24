import os
import json
import sys
from datetime import datetime

# ---------- PATH ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "accounts.json")

# ---------- INIT FILE ----------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

# ---------- LOAD / SAVE ----------
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- HELPERS ----------
def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def generate_acc_no(data):
    return str(100000 + len(data) + 1)

# ---------- REGISTER ----------
def register():
    data = load_data()

    username = input("Create username: ")

    if username in data:
        print("❌ User already exists")
        return

    pin = input("Set 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("❌ Invalid PIN")
        return

    acc_no = generate_acc_no(data)

    data[username] = {
        "account_no": acc_no,
        "pin": pin,
        "balance": 10000,
        "history": []
    }

    save_data(data)

    print(f"✅ Account created! Account No: {acc_no}")

# ---------- LOGIN ----------
def login():
    data = load_data()

    username = input("Enter username: ")

    if username not in data:
        print("❌ User not found")
        return None

    for i in range(3):
        pin = input("Enter PIN: ")
        if pin == data[username]["pin"]:
            print("✅ Login success")
            return username
        else:
            print(f"❌ Wrong PIN ({i+1}/3)")

    print("🚫 Account blocked")
    return None

# ---------- FEATURES ----------
def check_balance(user, data):
    print(f"💰 Balance: ₹{data[user]['balance']}")

def deposit(user, data):
    amt = int(input("Enter amount: ₹"))
    if amt > 0:
        data[user]["balance"] += amt
        data[user]["history"].append(f"{get_time()} → Deposited ₹{amt}")
        save_data(data)
        print("✅ Deposited")

def withdraw(user, data):
    amt = int(input("Enter amount: ₹"))
    if amt <= data[user]["balance"]:
        data[user]["balance"] -= amt
        data[user]["history"].append(f"{get_time()} → Withdraw ₹{amt}")
        save_data(data)
        print("💵 Done")
    else:
        print("❌ Insufficient balance")

def transfer(user, data):
    receiver = input("Receiver username: ")

    if receiver not in data:
        print("❌ User not found")
        return

    amt = int(input("Amount: ₹"))

    if amt <= data[user]["balance"]:
        data[user]["balance"] -= amt
        data[receiver]["balance"] += amt

        data[user]["history"].append(f"{get_time()} → Sent ₹{amt} to {receiver}")
        data[receiver]["history"].append(f"{get_time()} → Received ₹{amt} from {user}")

        save_data(data)
        print("✅ Transfer success")
    else:
        print("❌ Not enough balance")

def history(user, data):
    for h in data[user]["history"]:
        print("➡", h)

# ---------- MENU ----------
def menu(user):
    while True:
        data = load_data()

        print("\n🏦 ATM MENU")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. History")
        print("6. Logout")

        ch = input("Choose: ")

        if ch == "1":
            check_balance(user, data)
        elif ch == "2":
            deposit(user, data)
        elif ch == "3":
            withdraw(user, data)
        elif ch == "4":
            transfer(user, data)
        elif ch == "5":
            history(user, data)
        elif ch == "6":
            break
        else:
            print("❌ Invalid")

# ---------- MAIN ----------
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        ch = input("Choose: ")

        if ch == "1":
            register()
        elif ch == "2":
            user = login()
            if user:
                menu(user)
        elif ch == "3":
            sys.exit()
        else:
            print("❌ Invalid")

if __name__ == "__main__":
    main()