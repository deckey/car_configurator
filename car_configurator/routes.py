from car_configurator import app
from .models.Car import Car, CarEngine, CarTrim
import datetime
import car_configurator.db as db
from flask import render_template, flash, request
import json

cars, trims, engines = db.initialize()


@app.route('/')
def index():
    ''' Index page, configurator start button and project description '''
    return render_template(
        'index.html',
        car=db.load_car())


@app.route('/step1')
def step1():
    '''Car factory page, build your car from class to proceed further'''
    return render_template(
        'step1.html',
        title='Build your car',
        cars=cars,
        car=db.load_car())


@app.route('/step2', methods=["GET", "POST"])
def step2():
    ''' Car trim selector page, select trim level '''
    car = db.load_car()
    if request.method == "POST":
        car_model = request.form['car_model']
        for c in cars:
            if c.get('model') == car_model:
                idx = cars.index(c)
                car = cars[idx]
        db.save_car(car)

    return render_template(
        'step2.html',
        title='Select trim level',
        car=car,
        trims=trims)


@app.route('/step3', methods=["GET", "POST"])
def step3():
    ''' Car engine select page, select engine and transmission '''
    car = db.load_car()
    if request.method == "POST":
        trim_style = request.form['trim_style']
        for t in trims:
            if t.get('style') == trim_style:
                trim = t
        Car.add_trim(car, trim)
        db.save_car(car)

    return render_template(
        'step3.html',
        title='Select engine & transmission',
        car=car,
        engines=engines)


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
    db.save_car(car)

    return render_template(
        'step4.html',
        title='Select exterior features',
        car=car)


@app.route('/step5')
def step5():
    car = db.load_car()
    return render_template(
        'step5.html',
        car=car
    )
