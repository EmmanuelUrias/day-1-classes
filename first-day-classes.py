# Example base class
class Car:
    # Class attribute
    gravity = -9.8
    # Use the __init__ method to assign values to object properties

    def __init__(self, name):
        self.name = name
    # Custom method with no extra parameters

    def start(self):
        print("Vroom!")
    # Custom method with one parameter

    def talk(self, driver):
        print(f"Greetings {driver}, I am {self.name}!")

# Example inherited class


class RobotCar(Car):
    # Use the __init__ method to assign values to object properties
    def __init__(self, name, speed, type):
        # Call the __init__ method of the parent class since name is already a property
        super().__init__(name)
        # New properties of the inherited class
        self.speed = speed
        self.type = type


# Create base class instance
my_car = Car("Kitt")
# Create inherited class instance
my_car_2 = RobotCar("Speedy", 180, "sentient")

# Call the custom method
my_car.start()
my_car.talk("John")

# Print the class attributes
print(my_car.name)
print(my_car.gravity)

# Call inherited method
my_car_2.start()

# Print inherited attributes
print(my_car_2.speed)
