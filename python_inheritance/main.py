from classes import Animal, Rabbit, Fish, Hawk

if __name__ == "__main__":
    # Instantiate Objects
    animal_obj = Animal("Black")
    rabbit_obj = Rabbit("Brown")
    fish_obj = Fish("Blue")
    hawk_obj = Hawk("Grey")

    # Call Animal Class Methods
    animal_obj.sleep()
    rabbit_obj.eat()
    fish_obj.sleep()
    hawk_obj.eat()

    # Class Names Differ Based On Object Type
    rabbit_obj.print_color()
    fish_obj.print_color()
    hawk_obj.print_color()

    # SubClass Specific Methods
    rabbit_obj.hop()
    fish_obj.swim()
    hawk_obj.fly()
