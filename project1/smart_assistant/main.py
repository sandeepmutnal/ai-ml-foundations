# ======================================
# SMART PERSONAL ASSISTANT - PYTHON
# Covers: Basics → Functions → Files → Errors
# ======================================

# ---------- GLOBAL DATA ----------
tasks = []          # List
users = set()       # Set (unique users)

# ---------- FUNCTIONS ----------

def welcome():
    print("\n==============================")
    print("🤖 SMART PERSONAL ASSISTANT")
    print("==============================")

def get_user():
    name = input("Enter your name: ").strip().title()
    users.add(name)
    return name

def show_menu():
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. Calculator")
    print("7. Exit")

def add_task():
    title = input("Enter task title: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    print("✅ Task added successfully")

def view_tasks():
    if not tasks:
        print("⚠ No tasks available")
        return

    print("\n📋 TASK LIST:")
    for index, task in enumerate(tasks):
        status = "✔ Done" if task["done"] else "❌ Not Done"
        print(f"{index + 1}. {task['title']} - {status}")

def mark_task_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("🎉 Task marked as done")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")

def save_tasks():
    try:
        with open("data.txt", "w") as file:
            for task in tasks:
                file.write(f"{task['title']},{task['done']}\n")
        print("💾 Tasks saved to file")
    except Exception as e:
        print("Error saving file:", e)

def load_tasks():
    tasks.clear()
    try:
        with open("data.txt", "r") as file:
            for line in file:
                title, done = line.strip().split(",")
                tasks.append({
                    "title": title,
                    "done": done == "True"
                })
        print("📂 Tasks loaded successfully")
    except FileNotFoundError:
        print("⚠ No saved file found")

def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Choose operation: +  -  *  /")
        op = input("Operator: ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b if b != 0 else "Cannot divide by zero")
        else:
            print("Invalid operator")
    except ValueError:
        print("❌ Enter valid numbers")

# ---------- MAIN PROGRAM ----------

welcome()
user = get_user()
print(f"\nHello {user}! 👋")

while True:
    show_menu()
    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_done()
        elif choice == 4:
            save_tasks()
        elif choice == 5:
            load_tasks()
        elif choice == 6:
            calculator()
        elif choice == 7:
            print("👋 Goodbye! Thanks for using Smart Assistant")
            break
        else:
            print("❌ Invalid choice")

    except ValueError:
        print("❌ Please enter a number only")
