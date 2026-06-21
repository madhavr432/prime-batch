class student:
    college_name = "ABC college" #class attributes
    pi = 3.1
    def __init__(self, name, gpa):
        self.name = name #instance attributes
        self.gpa = gpa
        self.pi = 3.14
stu1 = student("Rahul", 9.2)
print(stu1.name)
print(stu1.pi)
print(student.pi)
print(stu1.college_name)
print(student.college_name)