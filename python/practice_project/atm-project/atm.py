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

def validate_pin(pin):
    return len(pin) == 4 and pin.isdigit()

# ---------- REGISTER ----------
def register():
    data = load_data()

    username = input("Create username: ")

    if username in data:
        print("❌ User already exists")
        return

    pin = input("Set 4-digit PIN: ")

    if not validate_pin(pin):
        print("❌ Invalid PIN (must be 4 digits)")
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

# ---------- LOGIN (USERNAME / ACC NO) ----------
def login():
    data = load_data()

    user_input = input("Enter Username or Account No: ")

    user = None

    for username in data:
        if username == user_input or data[username]["account_no"] == user_input:
            user = username
            break

    if not user:
        print("❌ User not found")
        return None

    for i in range(3):
        pin = input("Enter PIN: ")
        if pin == data[user]["pin"]:
            print("✅ Login success")
            return user
        else:
            print(f"❌ Wrong PIN ({i+1}/3)")

    print("🚫 Account blocked")
    return None

# ---------- FEATURES ----------
def check_balance(user, data):
    print(f"💰 Balance: ₹{data[user]['balance']}")

def deposit(user, data):
    try:
        amt = int(input("Enter amount: ₹"))

        if amt <= 0:
            print("❌ Invalid amount")
            return

        data[user]["balance"] += amt
        data[user]["history"].append(f"{get_time()} → Deposited ₹{amt}")
        save_data(data)

        print("✅ Deposited")

    except:
        print("❌ Numbers only")

def withdraw(user, data):
    try:
        amt = int(input("Enter amount: ₹"))

        if amt <= 0:
            print("❌ Invalid amount")
        elif amt > data[user]["balance"]:
            print("❌ Insufficient balance")
        else:
            data[user]["balance"] -= amt
            data[user]["history"].append(f"{get_time()} → Withdraw ₹{amt}")
            save_data(data)

            print("💵 Done")

    except:
        print("❌ Numbers only")

def transfer(user, data):
    receiver = input("Receiver username: ")

    if receiver not in data:
        print("❌ User not found")
        return

    try:
        amt = int(input("Amount: ₹"))

        if amt <= 0:
            print("❌ Invalid amount")
        elif amt > data[user]["balance"]:
            print("❌ Not enough balance")
        else:
            data[user]["balance"] -= amt
            data[receiver]["balance"] += amt

            data[user]["history"].append(f"{get_time()} → Sent ₹{amt} to {receiver}")
            data[receiver]["history"].append(f"{get_time()} → Received ₹{amt} from {user}")

            save_data(data)
            print("✅ Transfer success")

    except:
        print("❌ Numbers only")

def show_history(user, data):
    print("\n📜 Full History:")
    if data[user]["history"]:
        for h in data[user]["history"]:
            print("➡", h)
    else:
        print("No transactions")

def mini_statement(user, data):
    print("\n📄 Last 5 Transactions:")
    last = data[user]["history"][-5:]
    if last:
        for h in last:
            print("➡", h)
    else:
        print("No transactions")

# 🆕 DELETE ACCOUNT
def delete_account(user, data):
    confirm = input("Type YES to delete account: ")

    if confirm == "YES":
        del data[user]
        save_data(data)
        print("❌ Account deleted")
        return True
    else:
        print("Cancelled")
        return False

# ---------- MENU ----------
def menu(user):
    while True:
        data = load_data()

        print("\n🏦 ATM MENU")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Full History")
        print("6. Mini Statement")
        print("7. Delete Account")
        print("8. Logout")

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
            show_history(user, data)
        elif ch == "6":
            mini_statement(user, data)
        elif ch == "7":
            if delete_account(user, data):
                break
        elif ch == "8":
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