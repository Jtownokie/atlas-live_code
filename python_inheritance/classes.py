# Understanding Inheritance

class Animal:
    def __init__(self, color):
        self.color = color

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

    def print_color(self):
        print(f"The {self.__class__.__name__}'s color is {self.color}")

class Rabbit(Animal):
    def __init__(self, color):
        self.color = color

    def hop(self):
        print("The Rabbit is hopping")

class Fish(Animal):
    def __init__(self, color):
        super().__init__(color)

    def swim(self):
        print("The Fish is swimming")

class Hawk(Animal):
    def __init__(self, color):
        super().__init__(color)

    def fly(self):
        print("The Hawk is flying")
