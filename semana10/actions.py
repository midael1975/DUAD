import re

def is_valid_name(name):
    return bool(name.strip()) and not any(char.isdigit() for char in name)

def is_valid_section(section):
    return bool(re.match(r"^[0-9]{2}[A-Z]$", section))

def student_exists(students, name, section):
    return any(s["name"].lower() == name.lower() and s["section"].lower() == section.lower() for s in students)

def validate_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")

def add_students(students):
    try:
        n = int(input("How many students do you want to add? "))
    except ValueError:
        print("Invalid number. Returning to menu.")
        return

    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        while True:
            try:
                name = input("Full name: ")
                if not is_valid_name(name):
                    raise ValueError("Invalid name. Must not be empty or contain numbers.")

                section = input("Section (e.g., 10A, 11B): ")
                if not is_valid_section(section):
                    raise ValueError("Invalid section format. Example: 10A, 11B.")

                if student_exists(students, name, section):
                    raise ValueError("Student already exists. No duplicates allowed.")

                break
            except ValueError as e:
                print(f" {e}")
                continue

        spanish = validate_grade("Spanish")
        english = validate_grade("English")
        social = validate_grade("Social Studies")
        science = validate_grade("Science")

        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science,
            "average": (spanish + english + social + science) / 4
        }
        students.append(student)

def delete_student(students):
    if not students:
        print("No students registered.")
        return
    try:
        name = input("Enter the full name of the student to delete: ")
        section = input("Enter the section of the student: ")

        for s in students:
            if s["name"].lower() == name.lower() and s["section"].lower() == section.lower():
                confirm = input(f"Are you sure you want to delete {s['name']} ({s['section']})? (y/n): ")
                if confirm.lower() == "y":
                    students.remove(s)
                    print("Student deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return
        print("Student not found.")
    except Exception as e:
        print(f"Error while deleting student: {e}")

def view_students(students):
    if not students:
        print("No students registered.")
        return
    print("\n--- Students ---")
    for student in students:
        print(f"Name: {student['name']} | Section: {student['section']} | Average: {student['average']:.2f}")

def view_general_average(students):
    if not students:
        print("No students registered.")
        return
    general_avg = sum(student["average"] for student in students) / len(students)
    print(f"\nGeneral Average: {general_avg:.2f}")

def view_top3(students):
    if not students:
        print("No students registered.")
        return
    top3 = sorted(students, key=lambda x: x["average"], reverse=True)[:3]
    print("\n--- Top 3 Students ---")
    for i, s in enumerate(top3, start=1):
        print(f"{i}. {s['name']} ({s['section']}) - Average: {s['average']:.2f}")



def view_failed_students(students):
    if not students:
        print("No students registered.")
        return

    print("\n--- Failed Students ---")
    failed_list = []

    for student in students:
        failed_subjects = {
            subj: student[subj]
            for subj in ["spanish", "english", "social", "science"]
            if student[subj] < 60
        }

        if failed_subjects:
            failed_list.append((student, failed_subjects))

    if not failed_list:
        print("No failed students.")
        return

    for student, subjects in failed_list:
        failed_info = ", ".join([f"{subj.capitalize()} ({grade})" for subj, grade in subjects.items()])
        print(f"{student['name']} | {student['section']} | Failed subjects: {failed_info}")

