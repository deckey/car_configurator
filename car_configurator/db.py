import json
from .models.Car import Car, CarEngine, CarTrim

'''
File for creating mockup database, creating and storing all data as json files
'''


def cars_find_all():
    with open('cars_list.json', 'r') as f:
        cars = json.load(f)
    return cars


def save_car(car):
    with open('car.json', 'w') as f:
        json.dump(car, f, sort_keys=True, indent=4, separators=(',', ': '))


def load_car():
    with open('car.json', 'r') as f:
        car = json.load(f)
    return car


def find_car(model):
    cars = cars_find_all()
    for car in cars:
        if car['model'] == model:
            print('CAR FOUND...', car)
            return car
    return cars[0]


def find_engine(name):
    engines = create_engines()
    for engine in engines:
        if engine['name'] == name:
            return engine
    return engines[0]


def create_cars():
    ''' initialize values (mockup of database objects) '''
    # cars
    c0 = Car(0, 'Compact', 'City car', 13000)
    c1 = Car(1, 'Hatchback', 'Small family car', 14000)
    c2 = Car(2, 'Sedan', 'Comfort limousine', 15000)
    c3 = Car(3, 'Crossover', 'Weekend escape', 16000)
    c4 = Car(4, 'SUV', 'All terrain vehicle', 18000)
    c5 = Car(5, 'Sports', 'Fast coupe', 22000)
    cars_list = [car.__dict__ for car in [c0, c1, c2, c3, c4, c5]]

    # save cars list
    with open('cars_list.json', 'w') as f:
        cars = json.dump(list(cars_list), f, sort_keys=True,
                         indent=4, separators=(',', ': '))

    # save first car as starting option
    save_car(cars_list[0])
    return cars_list


def create_trims():
    # create trim options
    trim_default = CarTrim('Economy', 'Standard equipment package', 0)
    trim_sport = CarTrim("Sport", "Sport suspension mode", 2000)
    trim_tech = CarTrim("Tech", "Executive level equipment", 4000)
    trims = [trim.__dict__ for trim in [trim_default, trim_sport, trim_tech]]
    return trims


def create_engines():
    # engine creation
    e0 = CarEngine('1.2 TSI', '100 HP', 'petrol', 1800)
    e1 = CarEngine('1.4 TSI', '120 HP', 'diesel', 3600)
    e2 = CarEngine('1.8 TCI', '145 HP', 'petrol', 4300)
    e3 = CarEngine('2.2 TFI', '170 HP', 'diesel', 6400)
    e4 = CarEngine('2.8 TDI', '220 HP', 'diesel', 8400)

    engines = [engine.__dict__ for engine in [e0, e1, e2, e3, e4]]
    return engines


def initialize():
    return create_cars(), create_trims(), create_engines()
