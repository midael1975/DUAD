import csv
from student import Student

def load_students_from_csv(filename):
    students = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    id=row["id"],
                    name=row["name"],
                    age=row["age"],
                    grade=row["grade"]
                )
                students.append(student)
    except FileNotFoundError:
        print("File not found. A new one will be created when you save.")
    return students


def save_students_to_csv(filename, students):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        fieldnames = ["id", "name", "age", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            writer.writerow(student.to_dict())