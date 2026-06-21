class student:
    def __init__(self, name, roll_no, marks):
        self._name = "Unknown"
        self._roll_no = 1
        self._marks = 0

        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name == "":
            print("Error: Name cannot be empty.")
        else:
            self._name = name

    def get_roll_no(self):
        return self._roll_no

    def set_roll_no(self, roll_no):
        if roll_no < 1 or roll_no > 100:
            print("Error: Roll number has to be between 1 & 100.")
        else:
            self._roll_no = roll_no

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if marks < 0:
            print("Error: Marks cannot be negative.")
        else:
            self._marks = marks


if __name__ == "__main__":
    s1 = student("Alice", 25, 85)
    print(f"Name: {s1.get_name()}, Roll No: {s1.get_roll_no()}, Marks: {s1.get_marks()}")
    
    s1.set_marks(-10)
    s1.set_roll_no(150)
    s1.set_name("")
    
    print(f"Final State -> Name: {s1.get_name()}, Roll No: {s1.get_roll_no()}, Marks: {s1.get_marks()}")
