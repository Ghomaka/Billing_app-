
from flask import Flask
from router.productRouter import product
from router.invoiceRouter import invoice
from router.orderRouter import order

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World Welcome to the result app!"

# Optional URL prefix
app.register_blueprint(product, url_prefix='/api/product')
app.register_blueprint(invoice, url_prefix='/api/invoice')
app.register_blueprint(order, url_prefix='/api/order')


if __name__ == "__main__":
    app.run(debug=True)