import json
import os
import csv
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
        except:
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

        print(
            f"{i}. {status} [{task['priority']}] "
            f"{task['title']} | Category: {task['category']} "
            f"| Due: {task['due']} | Created: {task['created']}"
        )

    print("================================\n")


# -------------------------------
# Add Task
# -------------------------------

def add_task(tasks):

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty")
        return

    priority = input("Priority (Low/Medium/High): ").capitalize()

    if priority not in ["Low", "Medium", "High"]:
        priority = "Medium"

    category = input("Category (Work/Study/Personal): ").capitalize()

    if category not in ["Work", "Study", "Personal"]:
        category = "Personal"

    due = input("Due date (YYYY-MM-DD) or press Enter: ")

    if due == "":
        due = "No deadline"

    task = {
        "title": title,
        "done": False,
        "priority": priority,
        "category": category,
        "due": due,
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

            print("Task completed!")

        else:
            print("Invalid number")

    except:
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
            print("Invalid number")

    except:
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

            new_title = input("New title: ").strip()

            if new_title:
                tasks[num - 1]["title"] = new_title

            new_priority = input("New priority (Low/Medium/High): ").capitalize()

            if new_priority in ["Low", "Medium", "High"]:
                tasks[num - 1]["priority"] = new_priority

            save_tasks(tasks)

            print("Task updated!")

        else:
            print("Invalid number")

    except:
        print("Enter valid number")


# -------------------------------
# Search Tasks
# -------------------------------

def search_tasks(tasks):

    keyword = input("Enter keyword: ").lower()

    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print("No matching tasks")
        return

    view_tasks(results)


# -------------------------------
# Sort Tasks
# -------------------------------

def sort_by_priority(tasks):

    order = {"High": 1, "Medium": 2, "Low": 3}

    tasks.sort(key=lambda x: order.get(x["priority"], 2))

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

    print("Completed tasks removed")


# -------------------------------
# Statistics
# -------------------------------

def show_stats(tasks):

    total = len(tasks)
    completed = len([t for t in tasks if t["done"]])
    pending = total - completed

    print("\n======= STATS =======")
    print("Total tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)
    print("=====================\n")


# -------------------------------
# Export CSV
# -------------------------------

def export_csv(tasks):

    filename = "tasks_export.csv"

    with open(filename, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            ["Title", "Priority", "Category", "Due", "Status", "Created"]
        )

        for t in tasks:

            writer.writerow([
                t["title"],
                t["priority"],
                t["category"],
                t["due"],
                "Done" if t["done"] else "Pending",
                t["created"]
            ])

    print("Tasks exported to tasks_export.csv")


# -------------------------------
# Menu
# -------------------------------

def menu():

    print("\n=========== TO-DO APP PRO ===========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Search Tasks")
    print("7. Sort by Priority")
    print("8. Show Pending Tasks")
    print("9. Clear Completed")
    print("10. Show Statistics")
    print("11. Export CSV")
    print("12. Exit")
    print("=====================================")


# -------------------------------
# Main
# -------------------------------

def main():

    while True:

        tasks = load_tasks()

        menu()

        choice = input("Choose option (1-12): ")

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
            show_stats(tasks)

        elif choice == "11":
            export_csv(tasks)

        elif choice == "12":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()