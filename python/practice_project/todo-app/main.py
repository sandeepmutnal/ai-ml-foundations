import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


# -------------------------------
# File Operations
# -------------------------------

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)
        return []

    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# -------------------------------
# Display Tasks
# -------------------------------

def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n========== TASK LIST ==========")

    for i, task in enumerate(tasks, 1):

        status = "✅" if task["done"] else "❌"
        priority = task["priority"]
        created = task["created"]

        print(f"{i}. {status} [{priority}] {task['title']} (Created: {created})")

    print("================================\n")


# -------------------------------
# Add Task
# -------------------------------

def add_task(tasks):

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = input("Priority (Low/Medium/High): ").capitalize()

    if priority not in ["Low", "Medium", "High"]:
        priority = "Medium"

    task = {
        "title": title,
        "done": False,
        "priority": priority,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully!")


# -------------------------------
# Mark Done
# -------------------------------

def mark_done(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Enter task number: "))

        if 1 <= num <= len(tasks):

            tasks[num - 1]["done"] = True
            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Invalid task number")

    except ValueError:
        print("Enter valid number")


# -------------------------------
# Delete Task
# -------------------------------

def delete_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:

        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):

            removed = tasks.pop(num - 1)

            save_tasks(tasks)

            print(f"Deleted: {removed['title']}")

        else:
            print("Invalid task number")

    except ValueError:
        print("Enter valid number")


# -------------------------------
# Edit Task
# -------------------------------

def edit_task(tasks):

    view_tasks(tasks)

    if not tasks:
        return

    try:

        num = int(input("Enter task number to edit: "))

        if 1 <= num <= len(tasks):

            new_title = input("Enter new title: ").strip()

            if new_title:

                tasks[num - 1]["title"] = new_title

                save_tasks(tasks)

                print("Task updated!")

            else:
                print("Title cannot be empty")

        else:
            print("Invalid number")

    except ValueError:
        print("Enter valid number")


# -------------------------------
# Search Task
# -------------------------------

def search_tasks(tasks):

    keyword = input("Enter keyword to search: ").lower()

    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print("No matching tasks found.")
        return

    view_tasks(results)


# -------------------------------
# Sort Tasks by Priority
# -------------------------------

def sort_by_priority(tasks):

    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    tasks.sort(key=lambda x: priority_order.get(x["priority"], 2))

    save_tasks(tasks)

    print("Tasks sorted by priority!")


# -------------------------------
# Show Pending Tasks
# -------------------------------

def show_pending(tasks):

    pending = [t for t in tasks if not t["done"]]

    view_tasks(pending)


# -------------------------------
# Clear Completed
# -------------------------------

def clear_completed(tasks):

    tasks[:] = [t for t in tasks if not t["done"]]

    save_tasks(tasks)

    print("Completed tasks removed!")


# -------------------------------
# Menu
# -------------------------------

def menu():

    print("\n=========== TO-DO APP ===========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Sort by Priority")
    print("8. Show Pending Tasks")
    print("9. Clear Completed Tasks")
    print("10. Exit")
    print("=================================")


# -------------------------------
# Main Loop
# -------------------------------

def main():

    while True:

        tasks = load_tasks()

        menu()

        choice = input("Choose option (1-10): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            mark_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            edit_task(tasks)

        elif choice == "6":
            search_tasks(tasks)

        elif choice == "7":
            sort_by_priority(tasks)

        elif choice == "8":
            show_pending(tasks)

        elif choice == "9":
            clear_completed(tasks)

        elif choice == "10":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()