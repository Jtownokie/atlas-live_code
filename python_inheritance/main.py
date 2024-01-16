from classes import Animal, Rabbit, Fish, Hawk

if __name__ == "__main__":
    animal_obj = Animal("Black")
    rabbit_obj = Rabbit("Brown")
    fish_obj = Fish("Blue")
    hawk_obj = Hawk("Grey")

    animal_obj.sleep()
    rabbit_obj.eat()
    fish_obj.sleep()
    hawk_obj.eat()

    rabbit_obj.print_color()
    fish_obj.print_color()
    hawk_obj.print_color()
