from car_configurator import app
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix

app.config['REVERSE_PROXY_PATH'] = '/configurator'
ReverseProxyPrefixFix(app)

app.run(host="0.0.0.0", debug=True, port=5000)
