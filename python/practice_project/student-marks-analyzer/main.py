def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def main():
    print("Student Marks Analyzer")

    name = input("Enter student name: ")

    # Validate number of subjects
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
        while True:
            try:
                m = float(input(f"Enter mark {i+1}: "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks.append(m)
                total += m
                break
            except ValueError:
                print("Invalid input. Enter numeric value.")

    average = total / subjects
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()
