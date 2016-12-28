from car_configurator import app
from flask import render_template
from .models.Car import Car, CarEngine, CarTrim
import json
import datetime
from flask import request
import car_configurator.db as db


# set start values
cars = db.create_cars()
trims = db.create_trims()
engines = db.create_engines()
car = db.load_car()


@app.route('/')
def index():
    cars, trims, engines = db.initialize()

    with open('cars_list.json', 'w') as f:
        json.dump(list(cars), f, sort_keys=True,
                  indent=4, separators=(',', ': '))

    return render_template('index.html', cars=cars, car=car)


@app.route('/step1')
def step1():
    cars, trims, engines = db.initialize()
    return render_template(
        'step1.html',
        title='Build your car',
        cars=cars,
        car=car)


@app.route('/step2', methods=["GET", "POST"])
def step2():
    cars, trims, engines = db.initialize()
    if request.method == "POST":
        cls = request.form['type']
        cars = db.cars_find_all()
        for c in cars:
            if c.get('type') == cls:
                idx = cars.index(c)
                car = cars[idx]
        db.save_car(car)
    else:
        car = db.load_car()

    return render_template(
        'step2.html',
        title='Select trim level',
        car=car,
        trims=trims)


@app.route('/step3', methods=["GET", "POST"])
def step3():
    cars, trims, engines = db.initialize()
    car = cars[0]
    if request.method == "POST":
        car['trim']['style'] = request.form['style']
        car['trim']['price'] = int(request.form['trim_price'])
        db.save_car(car)
    else:
        car = db.load_car()

    return render_template(
        'step3.html',
        title='Select engine & transmission',
        car=car,
        engines=engines)


@app.route('/step4')
def step4():
    cars, trims, engines = db.initialize()
    return render_template('step4.html', cars=cars, car=car)
