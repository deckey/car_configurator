import json


class CarTrim(dict):

    def __init__(self, style, description, price):
        self.style = style
        self.description = description
        self.price = price


class CarEngine(dict):

    default_transmission = 'Manual'

    def __init__(self, name, power, fuel, price):
        self.name = name
        self.power = power
        self.fuel = fuel
        self.price = price
        self.transmission = self.default_transmission


class Car(dict):

    default_trim = CarTrim('Economy', 'Standard equipment package', 0)
    default_engine = CarEngine('1.2 TSI', '100 HP', 'petrol', 0)

    def __init__(self, _id, model, description, base_price):
        self._id = _id
        self.model = model
        self.description = description
        self.base_price = base_price
        self.trim = self.default_trim.__dict__
        self.engine = self.default_engine.__dict__
        self.price = self.base_price

    @staticmethod
    def add_trim(car, trim):
        car['trim'] = trim
        car['price'] = car['base_price'] + trim['price']
        return car

    @staticmethod
    def add_engine(car, engine):
        car['engine'] = engine
        car['price'] = car['base_price'] + car['trim']['price'] + engine['price']
        return car
