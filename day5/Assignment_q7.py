class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        if self.age is not None:
            print(f"Age: {self.age}")
        if self.address is not None:
            print(f"Address: {self.address}")


p1 = Person("Alice")
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30, "New York")        

print("Person 1:")
p1.display_info()

print("\nPerson 2:")
p2.display_info()

print("\nPerson 3:")
p3.display_info()
