from car_configurator import app
from .models.Car import Car, CarEngine, CarTrim
from .models._Factory import CarPartFactory, CarEngineFactory, CarTrimFactory
from .models._AbstractFactory import AbstractCarFactory
import datetime
import car_configurator.db as db
from flask import render_template, request
import json

# AbstractCarFactory with 'default' factory, can be scaled-up with more factories
default_factory = AbstractCarFactory().create_factory('default')

# store cars and 'current' car as mock files (simulating DB storage)
cars = default_factory.create_cars()
car = db.save_car(cars[0])

# CarPartFactory
trim_factory = CarPartFactory().factory('trim')
trims = trim_factory.create_parts()

engine_factory = CarPartFactory().factory('engine')
engines = engine_factory.create_parts()


@app.route('/')
def index():
    ''' Home page '''
    return render_template('index.html')


@app.route('/step1')
def step1():
    ''' Car class selection '''
    return render_template(
        'step1.html',
        title='Step 1: Select car class',
        car=car,
        cars=cars)


@app.route('/step2', methods=["GET", "POST"])
def step2():
    ''' Trim selection page, select trim level '''
    car = db.load_car()
    if request.method == "POST":
        car_model = request.form['car_model']
        car = db.find_car(car_model)

    db.save_car(car)
    return render_template(
        'step2.html',
        title='Step 2: Select trim level',
        car=car,
        trims=trims,
        icon="trim")


@app.route('/step3', methods=["GET", "POST"])
def step3():
    ''' Car engine select page, select engine and transmission '''
    car = db.load_car()
    if request.method == "POST":
        trim_style = request.form['trim_style']
        car_trim = db.find_trim(trim_style)
        car = Car.add_trim(car, car_trim)

    db.save_car(car)

    return render_template(
        'step3.html',
        title='Step 3: Select engine & transmission',
        car=car,
        engines=engines,
        icon="engine")


@app.route('/step4', methods=["GET", "POST"])
def step4():
    ''' Select exterior features and include them in the car '''
    car = db.load_car()
    if request.method == "POST":
        car_engine_name = request.form['car_engine_name']
        car_engine_transmission = request.form['car_engine_transmission']
        engine = db.find_engine(car_engine_name)
        engine['transmission'] = car_engine_transmission
        car = Car.add_engine(car, engine)
    else:
        engine = car['engine']

    db.save_car(car)
    return render_template(
        'step4.html',
        title='Step 4: Select features',
        car=car,
        wheels=db.create_wheels(),
        icon="features")


@app.route('/step5', methods=['GET', 'POST'])
def step5():
    '''Select extra components'''
    car = db.load_car()
    if request.method == 'POST':
        car_wheel_name = request.form['car_wheel_name']
        wheel = db.find_wheel(car_wheel_name)
        car = Car.add_wheel(car, wheel)
        car_ext_color = request.form['exterior_color']
        car_int_color = request.form['interior_color']
        car_material = request.form['interior_material']
        Car.add_features(car, *(car_ext_color, car_int_color, car_material))

    db.save_car(car)
    extras_equipment = Car.get_extras(car)
    extras = db.create_extra_equipment()

    return render_template(
        'step5.html',
        car=car,
        title='Step 5: Extra components',
        extras_equipment=Car.get_extras(car),
        extras=extras,
        extras_prices=Car.get_extras_prices(car),
        icon="extras"
    )


@app.route('/summary', methods=['GET', 'POST'])
def summary():
    ''' Summary page '''
    car = db.load_car()
    extras_price = 0
    if request.method == "POST":
        extras = request.form['extras']
        extras_prices = request.form['extras_price']
        extras_total_price = request.form['extras_total_price']
        car = Car.create_extras(car, extras, extras_prices)
        car['extras_price'] = int(extras_total_price)

    car['price'] = Car.get_price(car)
    db.save_car(car)
    return render_template(
        'summary.html',
        car=car,
        equipment=Car.get_extras(car),
        title='Summary'
    )
