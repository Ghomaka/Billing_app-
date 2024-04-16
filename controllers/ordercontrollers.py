from flask import Flask, jsonify, request
from models.order import Order


def get_all_orders():
    try:
        return jsonify({"orders": Order().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_new_order():
    try:
        data = request.get_json()
        order = Order(order_id=data["order_id"], product_id=data["product_id"])
        order.save()
        return jsonify({'message': 'order produced'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_an_order(order_id):
    try:
        data = request.get_json()
        order = Order( order_id=data["order_id"],
                          product_id=data["product_id"])
        order.save()
        return jsonify({'message': 'invoice updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_a_product(order_id):
    try:
        Order().delete(id=order_id)
        return jsonify({'message': 'subject deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
