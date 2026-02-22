import os
import json
import sys
from datetime import datetime

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "account_data.json")

os.makedirs(DATA_DIR, exist_ok=True)

# ---------- SAVE ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- LOAD ----------
def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "pin": "1234",
            "balance": 10000,
            "history": []
        }
        save_data(default_data)
        return default_data

    with open(DATA_FILE, "r") as f:
        return json.load(f)

data = load_data()

# ---------- HELPERS ----------
def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# ---------- FUNCTIONS ----------

def check_balance():
    print(f"\n💰 Balance: ₹{data['balance']}")

def deposit_money():
    try:
        amount = int(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("❌ Invalid amount")
            return

        if amount > 100000:
            print("⚠️ Deposit limit is ₹1,00,000")
            return

        data["balance"] += amount
        data["history"].append(f"{get_time()} → Deposited ₹{amount}")
        save_data(data)

        print("✅ Deposited successfully")

    except ValueError:
        print("❌ Numbers only")

def withdraw_money():
    try:
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("❌ Invalid amount")
        elif amount > data["balance"]:
            print("❌ Insufficient balance")
        else:
            data["balance"] -= amount
            data["history"].append(f"{get_time()} → Withdrawn ₹{amount}")
            save_data(data)

            print("💵 Collect your cash")

    except ValueError:
        print("❌ Numbers only")

def change_pin():
    old_pin = input("Enter old PIN: ")

    if old_pin == data["pin"]:
        new_pin = input("Enter new PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            data["pin"] = new_pin
            save_data(data)
            print("✅ PIN changed")
        else:
            print("❌ PIN must be 4 digits")
    else:
        print("❌ Wrong PIN")

def show_history():
    print("\n📜 Full Transaction History:")
    if data["history"]:
        for t in data["history"]:
            print("➡", t)
    else:
        print("No transactions")

def mini_statement():
    print("\n📄 Last 5 Transactions:")
    last = data["history"][-5:]
    if last:
        for t in last:
            print("➡", t)
    else:
        print("No transactions")

# ---------- MAIN ----------

def login():
    attempts = 0
    while attempts < 3:
        pin = input("Enter PIN: ")
        if pin == data["pin"]:
            print("✅ Login successful")
            return True
        else:
            attempts += 1
            print(f"❌ Wrong PIN ({attempts}/3)")
    print("🚫 Card blocked")
    return False

def atm_menu():
    while True:
        print("\n====== 🏦 ATM ======")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Full History")
        print("6. Mini Statement")
        print("7. Logout")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            show_history()
        elif choice == "6":
            mini_statement()
        elif choice == "7":
            print("🔒 Logged out")
            return
        elif choice == "8":
            print("🙏 Thank you")
            sys.exit()
        else:
            print("❌ Invalid option")

# ---------- RUN ----------
if __name__ == "__main__":
    print("📁 Saving to:", DATA_FILE)

    while True:
        if login():
            atm_menu()