import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()


def create_app(test_config=None):
    """
    Application Factory

    This function contains any configuration and setup the application needs
    and returns the application 
    """
    # create Flask instance
    app = Flask(__name__, instance_relative_config = False)
    # load default configurations
    app.config.from_object("backend.config.Config")

    # Initialize plugins
    db.init_app(app)
    ma.init_app(app)  # NOTE - not sure if this works

    with app.app_context():
        # include routes and models
        from . import models, routes
        # create tables in database - SUPPOSEDLY
        db.create_all()
        # register blueprints
        app.register_blueprint(routes.groceries_bp)

        # NOTE - may need to use Blueprints

    return app










