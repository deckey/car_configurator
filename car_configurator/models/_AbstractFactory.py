from abc import abstractmethod, ABCMeta
from .Car import Car
import json
import os

'''
File for creating mockup database, creating and storing all data as json files
'''
dir = os.path.dirname(__file__)
car_file = os.path.join(dir, '../data/car.json')
cars_file = os.path.join(dir, '../data/cars.json')


class AbstractCarFactory():
    __metaclass__ = ABCMeta

    # for demo purposes, only 'default' factory is used
    @abstractmethod
    def create_factory(self, factory):
        if factory == "default":
            return DefaultCarFactory()
        elif factory == "nissan":
            return NissanCarFactory()
        elif factory == "honda":
            return HondaCarFactory()

    @abstractmethod
    def create_cars(self):
        return self.cars


class DefaultCarFactory(AbstractCarFactory):
    ''' concrete factory / initialize values (mockup of database objects) '''

    def __init__(self):
        # cars
        self.c0 = Car(0, 'Compact', 'City car', 13000)
        self.c1 = Car(1, 'Hatchback', 'Small family car', 14000)
        self.c2 = Car(2, 'Sedan', 'Comfort limousine', 15000)
        self.c3 = Car(3, 'Crossover', 'Weekend escape', 16000)
        self.c4 = Car(4, 'SUV', 'All terrain vehicle', 18000)
        self.c5 = Car(5, 'Sports', 'Fast coupe', 22000)
        self.cars = [car.__dict__ for car in [self.c0, self.c1, self.c2, self.c3, self.c4, self.c5]]

    def create_cars(self):
        # save cars list
        with open(cars_file, 'w') as f:
            json.dump(
                [car for car in self.cars],
                f,
                separators=(',', ':'),
                sort_keys=True)
        return self.cars
