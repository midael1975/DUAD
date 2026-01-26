from student import Student

def find_student(students, id):
    for s in students:
        if s.id == id:
            return s
    return None


def add_student(students, id, name, age, grade):
    if find_student(students, id):
        print("There is already a student with that ID.")
        return

    student = Student(id, name, age, grade)
    students.append(student)
    print("Student added successfully.")


def update_student(student, name=None, age=None, grade=None):
    if name:
        student.name = name
    if age:
        student.age = age
    if grade:
        student.grade = grade
    print("Updated student information.")


def delete_student(students, id):
    student = find_student(students, id)
    if student:
        students.remove(student)
        print("Student deleted.")
    else:
        print("Student not found.")


def list_students(students):
    if not students:
        print("There are no registered students.")
        return

    for s in students:
        print(f"{s.id} | {s.name} | {s.age} | {s.grade}")