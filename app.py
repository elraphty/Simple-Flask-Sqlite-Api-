from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App
app = Flask(__name__)
basedir = os.path.join(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)

# init marshmallow
ma = Marshmallow(app)

# product class
class Product(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty
 

@app.route('/', methods=['GET'])
def index():
  return jsonify({'msg': 'hello'})

# product schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# init schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

## Run
if __name__ == "__main__":
    app.run(debug=True)