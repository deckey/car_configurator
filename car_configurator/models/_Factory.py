from .Car import CarTrim, CarEngine


class CarPartFactory(object):
    @staticmethod
    def factory(type):
        if type == "trim":
            return CarTrimFactory()
        if type == "engine":
            return CarEngineFactory()

    def create_parts(self):
        raise NotImplementedError


class CarTrimFactory(CarPartFactory):
    def create_parts(self):
        # create trim options
        trim_default = CarTrim('Economy', 'Standard equipment', 0)
        trim_basic = CarTrim('Basic', 'Basic package', 1000)
        trim_sport = CarTrim("Sport", "Adjusted suspension", 2000)
        trim_tech = CarTrim("Tech", "Executive equipment", 4000)
        return [trim.__dict__ for trim in [trim_default, trim_basic, trim_sport, trim_tech]]


class CarEngineFactory(CarPartFactory):
    def create_parts(self):
        # engine creation
        e0 = CarEngine('1.2 TSI', '100 HP', 'petrol', 1800)
        e1 = CarEngine('1.4 TSI', '120 HP', 'diesel', 3600)
        e2 = CarEngine('1.8 TCI', '145 HP', 'petrol', 4300)
        e3 = CarEngine('2.2 TFI', '170 HP', 'diesel', 6400)
        e4 = CarEngine('2.8 TDI', '220 HP', 'diesel', 8400)
        return [engine.__dict__ for engine in [e0, e1, e2, e3, e4]]

