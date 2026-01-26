from csv_utils import load_students_from_csv, save_students_to_csv
from student_utils import *

FILENAME = "students1.csv"

def menu():
    print("\n--- Student Control System ---")
    print("1. List students")
    print("2. Add student")
    print("3. Find student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Save and exit")

    return input("Select an option: ")


def main():
    students = load_students_from_csv(FILENAME)

    while True:
        option = menu()

        if option == "1":
            list_students(students)

        elif option == "2":
            id = input("ID: ")
            name = input("Nombre: ")
            age = input("Edad: ")
            grade = input("Nota: ")
            add_student(students, id, name, age, grade)

        elif option == "3":
            id = input("Student ID: ")
            student = find_student(students, id)
            if student:
                print(f"{student.id} | {student.name} | {student.age} | {student.grade}")
            else:
                print("Student not found.")

        elif option == "4":
            id = input("Student ID: ")
            student = find_student(students, id)
            if student:
                name = input("New name (enter to avoid changing): ")
                age = input("New age (enter to not change): ")
                grade = input("New grade (enter to not change): ")
                update_student(student, name or None, age or None, grade or None)
            else:
                print("Student not found.")

        elif option == "5":
            id = input("Student ID: ")
            delete_student(students, id)

        elif option == "6":
            save_students_to_csv(FILENAME, students)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()