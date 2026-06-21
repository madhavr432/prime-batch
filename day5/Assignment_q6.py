from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name):
        self.name= name
    @abstractmethod
    def salary(self):
        pass
class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend
    def salary(self):
        return self.stipend
class FullTime(Employee):
    def __init__(self, name, monthlysalary):
        super().__init__(name)
        self.monthlysalary = monthlysalary
    def salary(self):
        return self.monthlysalary
class Contract(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def salary(self):
        return self.hourly_rate * self.hours_worked
employees = [
    Intern("Alice", 5000),
    FullTime("Bob", 40000),
    Contract("Charlie", 800, 50)
]

for emp in employees:
    print(f"{emp.name}'s Salary: {emp.salary()}")    
