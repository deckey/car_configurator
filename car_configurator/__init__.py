#!/usr/local/bin/python3
from flask import Flask

app = Flask(__name__)
app.secret_key = 'topsecretkey'

import car_configurator.routes

if __name__=='__main__':
	app.run(port=5000)
