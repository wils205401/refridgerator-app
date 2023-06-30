from backend.models import Groceries
from backend.marshals import GroceriesSchema
import requests
from flask import Blueprint

groceries_bp = Blueprint("groceries_api", __name__)

grocery_schema = GroceriesSchema()
groceries_schema = GroceriesSchema(many=True)  # query set - multiple records?



# test routes
@groceries_bp.route("/hello")
def hello_world():
    return "Hello World!"


# create (route for inserting new data into database)
@groceries_bp.route("/add", methods = ["POST"])
def add_grocery():
    name = requests.json["name"]
    date = requests.json["date"]
    expiry_date = requests.json["expiry_date"]
    number_of_units = requests.json["number_of_units"]
    grocery_type = requests.json["grocery_type"]

    # create Groceries object to add to database
    grocery = Groceries(name, date, expiry_date, number_of_units, grocery_type)

    db.session.add(grocery)
    db.session.commit()

    return grocery_schema.jsonify(grocery)


# get all (route for getting all groceries in the database)
@groceries_bp.route("/get", methods = ["GET"])
def get_groceries():
    all_groceries = Groceries.query.all()
    results = groceries_schema.dump(all_groceries)

    return jsonify(results)


# get specific grocery by id
@groceries_bp.route("/get/<id>", methods = ["GET"])
def get_grocery(id):
    grocery = Groceries.query.get(id)

    return grocery_schema.jsonify(grocery)


# update grocery details
@groceries_bp.route("/update/<id>", methods = ["PUT"])
def update_grocery(id):
    grocery = Groceries.query.get(id)

    name = requests.json["name"]
    date = requests.json["date"]
    expiry_date = requests.json["expiry_date"]
    number_of_units = requests.json["number_of_units"]
    grocery_type = requests.json["grocery_type"]

    grocery.name = name
    grocery.date = date
    grocery.expiry_date = expiry_date
    grocery.number_of_units = number_of_units
    grocery.grocery_type = grocery_type

    return grocery_schema.jsonify(grocery)


# delete
@groceries_bp.route("/delete/<id>", methods = ["DELETE"])
def delete_grocery(id):
    grocery = Groceries.query.get(id)

    db.session.delete(grocery)
    db.session.commit()

    return grocery_schema.jsonify(grocery)

# clear_expired

