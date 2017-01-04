from car_configurator import app
from .models.Car import Car, CarEngine, CarTrim
import datetime
import car_configurator.db as db
from flask import render_template, flash, request, jsonify, make_response, redirect
import json

cars = db.create_cars()


@app.route('/')
def index():
    car = cars[0]
    db.save_car(car)
    return render_template('index.html', car=cars[0])


@app.route('/step1')
def step1():
    '''Car factory page, build your car from class to proceed further'''
    car = db.load_car()
    db.save_car(car)
    return render_template(
        'step1.html',
        title='Step 1: Select car class',
        car=car,
        cars=cars)


@app.route('/step2', methods=["GET", "POST"])
def step2():
    ''' Car trim selector page, select trim level '''
    car = db.load_car()
    trims = db.create_trims()
    if request.method == "POST":
        car_model = request.form['car_model']
        car = db.find_car(car_model)

    db.save_car(car)
    return render_template(
        'step2.html',
        title='Step 2: Select trim level',
        car=car,
        trims=trims)


@app.route('/step3', methods=["GET", "POST"])
def step3():
    ''' Car engine select page, select engine and transmission '''
    car = db.load_car()
    engines = db.create_engines()
    if request.method == "POST":
        trim_style = request.form['trim_style']
        car_trim = db.find_trim(trim_style)
        car = Car.add_trim(car, car_trim)

    db.save_car(car)

    return render_template(
        'step3.html',
        title='Step 3: Select engine & transmission',
        car=car,
        engines=engines)


@app.route('/car')
def get_car():
    car = db.load_car()
    return jsonify(car)


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
        wheels=db.create_wheels())


@app.route('/step5', methods=['GET', 'POST'])
def step5():
    '''Select extra components'''
    car = db.load_car()
    print('step5 car price ', car['price'])
    if request.method == 'POST':
        car_wheel_name = request.form['car_wheel_name']
        wheel = db.find_wheel(car_wheel_name)
        car = Car.add_wheel(car, wheel)
        car_ext_color = request.form['exterior_color']
        car_int_color = request.form['interior_color']
        car_material = request.form['interior_material']
        Car.add_features(car, *(car_ext_color, car_int_color, car_material))

    db.save_car(car)
    extras_equipment=Car.get_extras(car)
    extras = db.create_extra_equipment()

    return render_template(
        'step5.html',
        car=car,
        title='Step 5: Extra components',
        extras_equipment=Car.get_extras(car),
        extras=extras,
        extras_prices=Car.get_extras_prices(car)
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
