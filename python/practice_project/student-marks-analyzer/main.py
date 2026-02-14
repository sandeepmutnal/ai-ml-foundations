import os


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def add_student():
    name = input("\nEnter student name: ")

    while True:
        try:
            subjects = int(input("Enter number of subjects: "))
            if subjects <= 0:
                print("Subjects must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    marks = []
    total = 0

    for i in range(subjects):
        subject_name = input(f"Enter subject {i+1} name: ")

        while True:
            try:
                m = float(input(f"Enter marks for {subject_name}: "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks.append({
                    "subject": subject_name,
                    "marks": m
                })
                total += m
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = total / subjects
    grade = calculate_grade(average)
    status = "PASS" if average >= 50 else "FAIL"

    student_data = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": round(average, 2),
        "grade": grade,
        "status": status
    }

    print("\nStudent added successfully!")
    return student_data


def view_students(students):
    if not students:
        print("\nNo student data available.")
        return

    print("\n--- Student Records ---")

    for s in students:
        print(f"\nName: {s['name']}")

        for subject in s["marks"]:
            print(f"{subject['subject']}: {subject['marks']}")

        print(f"Total: {s['total']}")
        print(f"Average: {s['average']}")
        print(f"Grade: {s['grade']}")
        print(f"Status: {s['status']}")
        print("-" * 20)


def save_results(students):
    if not students:
        print("No students to save.")
        return

    file_path = os.path.join(os.path.dirname(__file__), "result.txt")

    with open(file_path, "w") as f:
        f.write("Student Marks Analyzer\n\n")

        for s in students:
            f.write(f"Name: {s['name']}\n")

            for subject in s["marks"]:
                f.write(f"{subject['subject']}: {subject['marks']}\n")

            f.write(f"Total: {s['total']}\n")
            f.write(f"Average: {s['average']}\n")
            f.write(f"Grade: {s['grade']}\n")
            f.write(f"Status: {s['status']}\n")
            f.write("-" * 20 + "\n")

    print(f"All results saved to: {file_path}")


def main():
    students = []

    while True:
        print("\n📊 Student Marks Analyzer")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Results")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            student = add_student()
            students.append(student)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            save_results(students)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
