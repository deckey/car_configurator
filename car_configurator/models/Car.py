import json


class CarTrim(dict):

    def __init__(self, style, description, price):
        self.style = style
        self.description = description
        self.price = price


class Car(dict):

    default_trim = CarTrim('Economy', 'Standard equipment package', 0)

    def __init__(self, _id, type, description, base_price):
        self._id = _id
        self.type = type
        self.description = description
        self.base_price = base_price
        self.trim = self.default_trim.__dict__


class CarEngine(dict):

    def __init__(self, name, power, fuel, price):
        self.name = name
        self.power = power
        self.fuel = fuel
        self.price = price
