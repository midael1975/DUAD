class Student:
    def __init__(self, id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"