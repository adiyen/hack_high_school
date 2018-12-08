from teacher import Teacher
from student import Student

class Classroom:
    capacity = 20

    def __init__(self, name):
        self.teacher = Teacher(name)
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)

    def status(self):
        print(f"This classroom has a standard capacity of {self.capacity} and is run by {self.teacher.name}. It currently has {len(self.students)} students")

    def begin_class(self):
        for student in self.students:
            print(f"{self.teacher.name}: Welcome to class, {student.name}")
            print(f"{student.name}: Good morning, {self.teacher.name}")