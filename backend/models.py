from backend import db
import datetime
import enum

# Build out functionality for recording what users have in the refridgerator
# on the UI, there will be a button "Add ingredient"

"""
Create models, or database tables, used to store data from the app.

groceries:
    - date (the date the user records grocery into system - hopefully coincides with purchase date)
    - expiry_date
    - name
    - number_of_units
"""

class GroceryTypes(enum.Enum):
    baking_goods = "Baking Goods"
    beverages = "Beverages"
    canned_goods = "Canned Goods" 
    dairy = "Dairy"
    fish = "Fish"
    frozen = "Frozen"
    grains = "Grains"
    meat = "Meat"
    pet = "Pet"
    produce = "Produce"
    snacks = "Snacks"
    spices = "Spices"
    other = "Other"


class Groceries(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)
    expiry_date = db.Column(db.DateTime)
    number_of_units = db.Column(db.Integer)
    grocery_type = db.Column(db.Enum(GroceryTypes))

    def __init__(self, name, date, expiry_date, number_of_units, grocery_type):
        self.name = name
        self.date = date
        self.expiry_date = expiry_date
        self.number_of_units = number_of_units
        self.grocery_type = grocery_type

    def __repr__(self):
        return f"<Groceries {self.name}>"
    

# python -m flask --app backend shell
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application