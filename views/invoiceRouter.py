from controllers.invoicecontrollers import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
invoice = Blueprint('invoice', __name__)



@invoice.route("/getAllinvoice", methods=['GET'])
def get_all_invoice():
    return get_all_invoices()


@invoice.route("/createinvoice", methods=['POST'])
def create_invoice():
    return create_an_invoice()


@invoice.route("/updateinvoice/<invoice_id>", methods=['PUT'])
def update_invoice(invoice_id):
    return update_an_invoice(invoice_id)

@invoice.route("/deleteinvoice/<invoice_id>", methods=['DELETE'])
def delete_invoice(invoice_id):
    return delete_an_invoice(invoice_id)