class Herbivore:
    def __init__(self):
        self.food_type = "Plants"

    def eat(self):
        print("Herbivore eats plants.")

class Carnivore:
    def __init__(self):
        self.food_type = "Meat"

    def eat(self):
        print("Carnivore eats meat.")

class Omnivore:
    def __init__(self):
        self.food_type = "Plants and Meat"

    def eat(self):
        print("Omnivore eats both plants and meat.")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)
        self.name = "Bear"

    def eat(self):
        print(f"{self.name} can eat plants, meat, and fish!")
b = Bear()
b.eat()