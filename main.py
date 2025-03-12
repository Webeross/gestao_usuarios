from flask import Flask
from routes.home import simple_page
from routes.cliente import cliente_route

app = Flask(__name__)

app.register_blueprint(simple_page)
app.register_blueprint(cliente_route, url_prefix='/clientes')

app.run(debug=True, port=4000)