import os

from flask import Flask
from flasgger import Swagger, swag_from

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    swagger = Swagger(app)

    from . import hijri
    app.register_blueprint(hijri.bp)

    return app