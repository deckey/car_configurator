import json
from .models.Car import Car, CarEngine, CarTrim, CarWheel
from .models._Factory import CarPartFactory
from .models.Equipment import *
import os

'''
File for creating mockup database, creating and storing all data as json files
'''
dir = os.path.dirname(__file__)
car_file = os.path.join(dir, 'data/car.json')
cars_file = os.path.join(dir, 'data/cars.json')

trim_factory = CarPartFactory().factory('trim')
engine_factory = CarPartFactory().factory('engine')


def load_cars():
    with open(cars_file, 'r') as f:
        return json.load(f)


def save_car(car):
    with open(car_file, 'w') as f:
        return json.dump(car, f, separators=(',', ':'), sort_keys=True)


def load_car():
    with open(car_file, 'r') as f:
        return json.load(f)


def find_car(model):
    cars = load_cars()
    for car in cars:
        if car['model'] == model:
            return car
    return cars[0]


def find_trim(style):
    trims = trim_factory.create_parts()
    for trim in trims:
        if trim['style'] == style:
            return trim
    return trims[0]


def find_engine(name):
    engines = engine_factory.create_parts()
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
