from car_configurator import app
from .models.Car import Car, CarEngine, CarTrim
import datetime
import car_configurator.db as db
from flask import render_template, flash, request
import json
from flask import session


@app.route('/')
def index():
    cars, trims, engines = db.initialize()
    car = cars[0]
    with open('cars_list.json', 'w') as f:
        json.dump(list(cars), f, sort_keys=True,
                  indent=4, separators=(',', ': '))

    return render_template('index.html', cars=cars, car=car)


@app.route('/step1')
def step1():
    cars = db.cars_find_all()
    return render_template(
        'step1.html',
        title='Build your car',
        cars=cars,
        car=cars[0])


@app.route('/step2', methods=["GET", "POST"])
def step2():
    trims = db.create_trims()
    if request.method == "POST":
        car_model = request.form['car_model']
        cars = db.cars_find_all()
        for c in cars:
            if c.get('model') == car_model:
                idx = cars.index(c)
                car = cars[idx]
        db.save_car(car)
    else:
        car = db.load_car()
    session['car'] = car

    return render_template(
        'step2.html',
        title='Select trim level',
        car=car,
        trims=trims)


@app.route('/step3', methods=["GET", "POST"])
def step3():
    car = session['car']
    engines = db.create_engines()
    trims = db.create_trims()

    if request.method == "POST":
        trim_style = request.form['trim_style']
        for t in trims:
            if t.get('style') == trim_style:
                trim = t
        car = Car.add_trim(car, trim)
        db.save_car(car)
    else:
        car = db.load_car()

    return render_template(
        'step3.html',
        title='Select engine & transmission',
        car=car,
        engines=engines)


@app.route('/step4', methods=["GET", "POST"])
def step4():
    car = session['car']
    if request.method == "POST":
        car_engine_name = request.form['car_engine_name']
        car_engine_transmission = request.form['car_engine_transmission']
        engine = db.find_engine(car_engine_name)
        engine['transmission'] = car_engine_transmission

    car = Car.add_engine(car, engine)
    db.save_car(car)

    return render_template(
        'step4.html',
        title='Select exterior features',
        car=car)


@app.route('/step5')
def step5():
    return render_template(
        'step5.html',
        car=car
    )
