from controllers.ordercontrollers import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
order = Blueprint('order', __name__)



@order.route("/getAllOrder", methods=['GET'])
def get_all_order():
    return get_all_orders()


@order.route("/createOrder", methods=['POST'])
def create_order():
    return create_new_order()


@order.route("/updateorder/<order_id>", methods=['PUT'])
def update_order(order_id):
    return update_an_order(order_id)

@order.route("/deleteorder/<order_id>", methods=['DELETE'])
def delete_product(order_id):
    return delete_a_product(order_id)