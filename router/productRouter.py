# from controllers.productcontrollers import *
from controllers.productcontrollers import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
product = Blueprint('product', __name__)

# @product.route('/')
# def hello_world():
#     return "Hello, World Welcome to the result app! ResultApp"


@product.route("/getAllProducts", methods=['GET'])
def get_all_product():
    return get_all_products()


@product.route("/createProduct", methods=['POST'])
def create_product():
    return create_new_product()


@product.route("/updateproduct/<product_id>", methods=['PUT'])
def update_product():
    return update_a_product(product)

@product.route("/deleteproduct/<product_id>", methods=['DELETE'])
def delete_product(product_id):
    return delete_a_product(product_id)