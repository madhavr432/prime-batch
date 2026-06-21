class student:
    def __init__(self, name, cgpa):
        print("constructor was called")
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
stu1 = student("Madhav", 9.0)
stu2 = student("Urvashi", 8.4)
stu3 = student("Rahul", 9.2)

# print(stu1.name)
# print(stu2.name)
# print(stu3.name)
# print(stu1.cgpa)
# print(stu3.cgpa)
# print(stu2.cgpa)
print(stu1.get_cgpa())