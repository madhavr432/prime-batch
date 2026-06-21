class employee:
    def get_designation(self):
        print("designation = Employee")
class teacher(employee):
    def get_designation(self):
        print("designation = Teacher")
t1 = teacher()
t1.get_designation()