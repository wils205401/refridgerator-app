from backend import ma

""" 
This part is used to serialize/de-serialize data. We use flask-marshmallow.
If we send data to the front end, we need to serialize our data, meaning we
convert the data objects into a series of bytes. We then de-serialize in order
to create the data structure.
"""

class GroceriesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "date",
            "expiry_date",
            "number_of_units",
            "grocery_type",
        )