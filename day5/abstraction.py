from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Roar!!!")
class Dog(Animal):
    def make_sound(self):
        print("Woof!!!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!!!")
class Cow(Animal):
    def make_sound(self):
        print("moooo!!!")
cow = Cow()
cow.make_sound()
lion = Lion()
lion.make_sound()