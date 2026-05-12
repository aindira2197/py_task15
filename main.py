class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for s in self.students:
            print(s)

uni = University("TATU")

uni.add_student("Ali")
uni.add_student("Vali")

uni.show_students()
