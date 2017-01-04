from .js import JsObject
import json
from .models.Car import Car, CarEngine, CarTrim, CarWheel
from .models.Equipment import *
from flask import jsonify
import os

'''
File for creating mockup database, creating and storing all data as json files
'''
dir = os.path.dirname(__file__)
car_file = os.path.join(dir, 'data/car.json')
cars_file = os.path.join(dir, 'data/cars.json')


def cars_find_all():
    with open(cars_file, 'r') as f:
        return json.load(f)


def save_car(car):
    with open(car_file, 'w') as f:
        return json.dump(car, f, separators=(',', ':'), sort_keys=True)


def load_car():
    with open(car_file, 'r') as f:
        return json.load(f)


def find_car(model):
    cars = cars_find_all()
    for car in cars:
        if car['model'] == model:
            return car
    return cars[0]


def find_trim(style):
    trims = create_trims()
    for trim in trims:
        if trim['style'] == style:
            return trim
    return trims[0]


def find_engine(name):
    engines = create_engines()
    for engine in engines:
        if engine['name'] == name:
            return engine
    return engines[0]


def find_wheel(name):
    wheels = create_wheels()
    for wheel in wheels:
        if wheel['name'] == name:
            return wheel
    return wheels[0]


def create_cars():
    ''' initialize values (mockup of database objects) '''
    # cars
    c0 = Car(0, 'Compact', 'City car', 13000)
    c1 = Car(1, 'Hatchback', 'Small family car', 14000)
    c2 = Car(2, 'Sedan', 'Comfort limousine', 15000)
    c3 = Car(3, 'Crossover', 'Weekend escape', 16000)
    c4 = Car(4, 'SUV', 'All terrain vehicle', 18000)
    c5 = Car(5, 'Sports', 'Fast coupe', 22000)
    cars = [car.__dict__ for car in [c0, c1, c2, c3, c4, c5]]
    # save cars list
    with open(cars_file, 'w') as f:
        json.dump([car for car in cars], f,
                  separators=(',', ':'), sort_keys=True)
    return cars


def create_trims():
    # create trim options
    trim_default = CarTrim('Economy', 'Standard equipment', 0)
    trim_basic = CarTrim('Basic', 'Basic package', 1000)
    trim_sport = CarTrim("Sport", "Adjusted suspension", 2000)
    trim_tech = CarTrim("Tech", "Executive equipment", 4000)
    trims = [trim_default, trim_basic, trim_sport, trim_tech]
    return [trim.__dict__ for trim in trims]


def create_engines():
    # engine creation
    e0 = CarEngine('1.2 TSI', '100 HP', 'petrol', 1800)
    e1 = CarEngine('1.4 TSI', '120 HP', 'diesel', 3600)
    e2 = CarEngine('1.8 TCI', '145 HP', 'petrol', 4300)
    e3 = CarEngine('2.2 TFI', '170 HP', 'diesel', 6400)
    e4 = CarEngine('2.8 TDI', '220 HP', 'diesel', 8400)

    engines = [engine.__dict__ for engine in [e0, e1, e2, e3, e4]]
    return engines


def create_wheels():
    # wheels creation
    w0 = CarWheel('Basic', 16, 'steel', 0)
    w1 = CarWheel('Idle', 17, 'alloy', 600)
    w2 = CarWheel('Super', 18, 'alloy', 1200)

    wheels = [wheel.__dict__ for wheel in [w0, w1, w2]]
    return wheels


def initialize():
    return create_cars(), create_trims(), create_engines()


def create_extra_equipment():
    # Equipment composite pattern

    safety = EquipmentComposite('Safety')
    safety.add_children(
        ['Protection assistant', 'Rear side airbags'], [210, 320])

    functionality = EquipmentComposite('Functionality')
    functionality.add_children(
        ['ISOFIX seat system', 'Textile floor mat set', 'Smoking pack'], [150, 120, 80])

    comfort = EquipmentComposite('Comfort')
    comfort.add_children(
        ['Cruise control', 'Panoramic sunroof', 'Parking sensors'], [400, 650, 330])

    # top-level composite
    extra_equipment = EquipmentComposite('Extra equipment')
    extra_equipment.append_child(safety)
    extra_equipment.append_child(functionality)
    extra_equipment.append_child(comfort)

    # return result
    return extra_equipment
