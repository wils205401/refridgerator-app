import os

class Config():

    # Set up app SECRET_KEY
    SECRET_KEY = "adrian_is_a_dummy"

    # database configurations
    base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False