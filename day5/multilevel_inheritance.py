class employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time


class adminstaff(employee):
    def __init__(self, role):
        self.role = role


class accountant(adminstaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


acc1 = accountant(25000, "CA")
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)
