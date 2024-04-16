from flask import Flask, jsonify, request
from models.invoice import Invoice


def get_all_invoices():
    try:
        return jsonify({"invoices": Invoice().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_an_invoice():
    try:
        data = request.get_json()
        invoice = Invoice(id=data["invoice_id"], id2=data["product_id"],
                          datetime=data["datetime"],total=data["total"])
        invoice.save()
        return jsonify({'message': 'invoice created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_an_invoice(invoice_id):
    try:
        data = request.get_json()
        invoice = Invoice(id=data["invoice_id"], id2=data["product_id"], name=data["product_name"], datetime=data["datetime"],
                          total=data["total"])
        invoice.save()
        return jsonify({'message': 'invoice updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_an_invoice(invoice_id):
    try:
        Invoice().delete(id=invoice_id)
        return jsonify({'message': 'invoice deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
