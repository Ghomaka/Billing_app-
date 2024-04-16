from flask import Flask, jsonify, request
from models.products import Product

def get_all_products():
    product = Product()
    try:
        return jsonify({"product": product.read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_new_product():
    try:
        data = request.get_json()
        product = Product(product_name=data["product_name"], price=data["price"],
                          quantity=data["quantity"], category=data["category"])
        product.save()
        return jsonify({'message': 'product created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_a_product():
    try:
        data = request.get_json()
        product = Product( product_name=data[" product_name"], price=data["price"],
                          quantity=data["quantity"], category=data["category"])
        product.save()
        return jsonify({'message': 'price updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_a_product(product_id):
    product = Product
    try:
        product.delete(id=product_id)
        return jsonify({'message': 'product deletes successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500