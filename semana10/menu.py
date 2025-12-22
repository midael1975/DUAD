from actions import (
    add_students,
    delete_student,
    view_students,
    view_top3,
    view_general_average,
    view_failed_students
)
from data import export_to_csv, import_from_csv

students = []

def show_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add students")
        print("2. Delete student")
        print("3. View top 3 students")
        print("4. View general average")
        print("5. View failed students")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Exit")
        
        option = input("Select an option: ")
        
        if option == "1":
            add_students(students)
        if option == "2":
            delete_student(students)
        if option == "3":
            view_top3(students)
        if option == "4":
            view_general_average(students)
        if option == "5":
            view_failed_students(students)
        if option == "6":
            export_to_csv(students)
        if option == "7":
            import_from_csv(students)
        if option == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a valid option.")










