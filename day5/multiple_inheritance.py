class teacher:
    def __init__(self, salary):
        self.salary = salary


class student:
    def __init__(self, gpa):
        self.gpa = gpa


class TA(teacher, student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        student.__init__(self, gpa)
        self.name = name


ta1 = TA(15_000, 9.3, "madhav")
print(ta1.name, ta1.gpa, ta1.salary)
