'''
This is the Rest module.  This module contains a single method to create an instance of a Flask app, used to service incoming requests.
The method compiles all blueprints and adds them to the context of the Flask app it returns.
'''

from flask import Flask

def create():
    
    app = Flask(__name__)

    from REST.Blueprints.march_madness import march_madness as march_madness_blueprint
    app.register_blueprint(march_madness_blueprint)

    return app