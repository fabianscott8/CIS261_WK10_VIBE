#Fabian Scott
#CIS261
#WK10 VIBE Coding - Student Grade Calculator

# File name for storing student records
DATA_FILE = "student_grades.txt"


# ==================================================================
# UTILITY FUNCTIONS
# ==================================================================

def calculate_average(test1, test2, test3):
    """
    Calculate the average of three test scores.

    Args:
        test1, test2, test3 (float): The three test scores

    Returns:
        float: The average score rounded to 2 decimal places
    """
    return round((test1 + test2 + test3) / 3, 2)


def calculate_grade(average):
    """
    Calculate letter grade based on average score.

    Grading scale: A = 90-100, B = 80-89, C = 70-79, D = 60-69, F = below 60

    Args:
        average (float): The average score

    Returns:
        str: The letter grade (A, B, C, D, or F)
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# ==================================================================
# FILE I/O FUNCTIONS
# ==================================================================

def load_students_from_file(filename):
    """
    Load student records from a pipe-delimited file.

    Args:
        filename (str): The name of the file to load from

    Returns:
        list: A list of student dictionaries
    """
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    student = {
                        'name': parts[0],
                        'id': parts[1],
                        'test1': float(parts[2]),
                        'test2': float(parts[3]),
                        'test3': float(parts[4]),
                        'average': float(parts[5]),
                        'grade': parts[6]
                    }
                    students.append(student)
        print(f"Loaded {len(students)} student record(s) from file.")
    except FileNotFoundError:
        print("No existing student file found. Starting with an empty roster.")
    except Exception as e:
        print(f"Error loading student records: {e}")
    return students


def save_students_to_file(students, filename):
    """
    Save all student records to a pipe-delimited file.

    Args:
        students (list): The list of student dictionaries
        filename (str): The name of the file to save to
    """
    try:
        with open(filename, 'w') as file:
            for student in students:
                line = (f"{student['name']}|{student['id']}|"
                        f"{student['test1']:.2f}|{student['test2']:.2f}|{student['test3']:.2f}|"
                        f"{student['average']:.2f}|{student['grade']}\n")
                file.write(line)
        print(f"Saved {len(students)} student record(s) to file.")
    except Exception as e:
        print(f"Error saving student records: {e}")


# ==================================================================
# MENU FEATURE FUNCTIONS
# ==================================================================

def add_student(students):
    """
    Prompt the user for student information, calculate the average and
    letter grade, and append the new student to the list.

    Args:
        students (list): The list of student dictionaries
    """
    print("\n" + "=" * 60)
    print("ADD NEW STUDENT")
    print("=" * 60)

    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    try:
        test1 = float(input("Enter Test 1 score: "))
        test2 = float(input("Enter Test 2 score: "))
        test3 = float(input("Enter Test 3 score: "))
    except ValueError:
        print("Invalid score entered. Student was not added.")
        return

    average = calculate_average(test1, test2, test3)
    grade = calculate_grade(average)

    student = {
        'name': name,
        'id': student_id,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'average': average,
        'grade': grade
    }
    students.append(student)

    print(f"\nAdded student: {name} (ID: {student_id})")
    print(f"  Average: {average:.2f} | Grade: {grade}")


def display_all_students(students):
    """
    Display all student records in a formatted table.

    Args:
        students (list): The list of student dictionaries
    """
    print("\n" + "=" * 70)
    print("ALL STUDENT RECORDS")
    print("=" * 70)

    if not students:
        print("No student records found.")
        print("=" * 70)
        return

    print(f"{'Name':<20}{'ID':<10}{'Test 1':<10}{'Test 2':<10}{'Test 3':<10}{'Average':<10}{'Grade':<6}")
    print("-" * 70)
    for student in students:
        print(f"{student['name']:<20}{student['id']:<10}"
              f"{student['test1']:<10.2f}{student['test2']:<10.2f}{student['test3']:<10.2f}"
              f"{student['average']:<10.2f}{student['grade']:<6}")
    print("=" * 70)
    print(f"Total students: {len(students)}")


def search_student(students):
    """
    Search for a student by name (case-insensitive) and display their
    information if found.

    Args:
        students (list): The list of student dictionaries
    """
    print("\n" + "=" * 60)
    print("SEARCH STUDENT")
    print("=" * 60)

    search_name = input("Enter student name to search: ").strip()

    for student in students:
        if student['name'].lower() == search_name.lower():
            print("\nFound student:")
            print(f"  Name: {student['name']}")
            print(f"  ID: {student['id']}")
            print(f"  Test 1: {student['test1']:.2f}")
            print(f"  Test 2: {student['test2']:.2f}")
            print(f"  Test 3: {student['test3']:.2f}")
            print(f"  Average: {student['average']:.2f}")
            print(f"  Grade: {student['grade']}")
            return

    print(f"No student found with name: {search_name.lower()}")


def view_class_statistics(students):
    """
    Calculate and display class statistics including the highest average,
    lowest average, class average, and grade distribution.

    Args:
        students (list): The list of student dictionaries
    """
    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)

    if not students:
        print("No student records found.")
        return

    averages = [student['average'] for student in students]
    class_average = sum(averages) / len(averages)

    highest = max(students, key=lambda s: s['average'])
    lowest = min(students, key=lambda s: s['average'])

    print(f"\nClass Average: {class_average:.2f}")
    print(f"Highest Average: {highest['average']:.2f} ({highest['name']})")
    print(f"Lowest Average: {lowest['average']:.2f} ({lowest['name']})")

    grade_counts = {}
    for student in students:
        grade_counts[student['grade']] = grade_counts.get(student['grade'], 0) + 1

    print("\nGrade Distribution:")
    for grade, count in grade_counts.items():
        print(f"  {grade}: {count} student(s)")


# ==================================================================
# MENU FUNCTIONS
# ==================================================================

def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 60)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit (or press ESC)")
    print("=" * 60)


# ==================================================================
# MAIN PROGRAM
# ==================================================================

def main():
    """Run the Student Grade Calculator program."""
    print("=" * 60)
    print("WELCOME TO STUDENT GRADE CALCULATOR")
    print("=" * 60)

    students = load_students_from_file(DATA_FILE)

    while True:
        display_menu()
        choice = input("Select an option (1-5) or press ESC to exit: ")

        if choice == "\x1b" or choice.strip().upper() == "ESC":
            print("\nSaving records...")
            save_students_to_file(students, DATA_FILE)
            print("Thank you for using Student Grade Calculator!")
            break
        elif choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            view_class_statistics(students)
        elif choice == "5":
            print("\nSaving records...")
            save_students_to_file(students, DATA_FILE)
            print("Thank you for using Student Grade Calculator!")
            break
        else:
            print("Invalid choice. Please select an option from 1-5 or press ESC.")


if __name__ == "__main__":
    main()
