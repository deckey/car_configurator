import os
from car_configurator import app
from dotenv import load_dotenv
load_dotenv()
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
app.run(host="0.0.0.0", debug=DEBUG, port=PORT)
