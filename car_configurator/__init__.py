from flask import Flask

app = Flask(__name__)
app.secret_key = 'topsecretkey'

import car_configurator.routes
