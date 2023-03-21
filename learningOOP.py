class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')


class Race():
    def __init__(self, name, driver_limit):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)

    def get_average(self):
        rank_sum = 0
        for driver in self.drivers:
            rank_sum += driver.get_ranking()
        return rank_sum / len(self.drivers)


Piston_Cup = Race('Piston Cup', 12)


class Driver():
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        self.number_of_drivers += 1

    def get_ranking(self):
        return self.ranking

    def get_average(self):
        rank_sum = 0
        for driver in range(1, self.number_of_drivers + 1):
            rank_sum += driver.get_ranking()
        return rank_sum / self.number_of_drivers


Lightning_McQueen = Driver('Lightning McQueen', 19, 2)
blue_guy = Driver('Blue Guy', 35, 1)
one_that_says_kachiga = Driver('one that says kachiga', 27, 12)

Piston_Cup.add_driver(Lightning_McQueen)
Piston_Cup.add_driver(blue_guy)
Piston_Cup.add_driver(one_that_says_kachiga)

print(Piston_Cup.get_average())
print(Lightning_McQueen.get_average())

# my_course = Race('Piston Cup', 12)
# print(my_course.name, my_course.driver_limit, my_course.drivers)

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# myCar.talk('Michael')
