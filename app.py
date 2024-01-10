from flask import Flask, request, jsonify
import json

app = Flask(__name__)

products = []

@app.route('/add', methods=['POST'])
def add_product():
    global products
    product = request.get_json()
    products.append(product)
    return jsonify({"message": "Product added successfully."}), 201

@app.route('/delete', methods=['DELETE'])
def delete_product():
    global products
    product_name = request.get_json()['name']
    products = [product for product in products if product['name'] != product_name]
    return jsonify({"message": "Product deleted successfully."}), 200

if __name__ == '__main__':
    app.run(port=5001)