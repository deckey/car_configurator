
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


class CarWheel(dict):

    def __init__(self, name, size, material, price):
        self.name = name
        self.size = size
        self.material = material
        self.price = price


class CarFeatures(dict):

    def __init__(self, *features):
        self.ext_color, self.int_color, self.material = features


class CarExtra(dict):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Car(dict):

    default_trim = CarTrim('Economy', 'Standard equipment', 0)
    default_engine = CarEngine('1.2 TSI', '100 HP', 'petrol', 0)
    default_wheel = CarWheel('Basic', 16, 'steel', 0)
    default_features = CarFeatures(*('Pearl white', 'Light grey', 'Cloth'))
    default_extras = []

    def __init__(self, _id, model, description, base_price):
        self._id = _id
        self.model = model
        self.description = description
        self.base_price = base_price
        self.trim = self.default_trim.__dict__
        self.engine = self.default_engine.__dict__
        self.wheel = self.default_wheel.__dict__
        self.features = self.default_features.__dict__
        self.extras = self.default_extras
        self.extras_price = 0

        self.price = self.base_price + self.trim['price']
        + self.engine['price'] + self.wheel['price']

    @staticmethod
    def add_trim(car, trim):
        car['trim'] = trim
        car['price'] = Car.get_price(car)
        return car

    @staticmethod
    def add_engine(car, engine):
        car['engine'] = engine
        car['price'] = Car.get_price(car)
        return car

    @staticmethod
    def add_wheel(car, wheel):
        car['wheel'] = wheel
        car['price'] = Car.get_price(car)
        return car

    @staticmethod
    def add_features(car, *features):
        car["features"]['ext_color'] = features[0]
        car["features"]['int_color'] = features[1]
        car["features"]['material'] = features[2]
        return car

    @staticmethod
    def create_extras(car, extras, prices):
        items = []
        for extra, price in zip(extras.split(','), prices.split(',')):
            new_extra = CarExtra(extra, price)
            items.append(new_extra.__dict__)
        car['extras'] = items
        return car

    @staticmethod
    def add_extras(car, extras, prices):
        car['extras'] = [{'name': equipment, 'price': price} for equipment, price in zip(extras, prices)]
        extras_total_price = sum([price for price in prices])
        return extras_total_price

    @staticmethod
    def calculate_extras(car, extras):
        print('INCOMING EXTRAS: ', extras)

    @staticmethod
    def get_extras(car):
        car_extras = []
        for extra in car['extras']:
            car_extras.append(extra['name'])
        return ",".join(car_extras)

    @staticmethod
    def get_extras_prices(car):
        extras_price_list = ''
        for extra in car['extras']:
            extras_price_list += extra['price'] + ','
        return extras_price_list

    @staticmethod
    def get_price(car):
        return car['base_price'] + car['trim']['price'] + car['engine']['price'] + car['wheel']['price'] + car['extras_price']
