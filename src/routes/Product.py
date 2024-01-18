from flask import Blueprint, jsonify

# Models 
from models.ProductModel import ProductModel
main = Blueprint('product_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products = ProductModel.get_products()
        return jsonify(products)
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@main.route('/<nom_prod>')
def get_product(nom_prod):
    try:
        product = ProductModel.get_product(nom_prod)
        if product != None:
            return jsonify(product)
        else:
            return jsonify({}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500