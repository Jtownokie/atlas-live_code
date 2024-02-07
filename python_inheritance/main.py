from classes import Animal, Rabbit, Fish, Hawk

if __name__ == "__main__":
    # Instantiate Objects
    animal_obj = Animal("Black")
    rabbit_obj = Rabbit("Brown")
    fish_obj = Fish("Blue")
    hawk_obj = Hawk("Grey")
    # Call Animal Class Methods
    animal_obj.eat()
    animal_obj.sleep()
    print(animal_obj.alive)
    print(animal_obj.color)

    rabbit_obj.eat()
    rabbit_obj.hop()
    rabbit_obj.print_color()
    # Class Names Differ Based On Object Type
    fish_obj.print_color()
    hawk_obj.print_color()
    # SubClass Specific Methods
