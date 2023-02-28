from flask import Blueprint, jsonify, request, abort
from api.models import Product
from api import db
from .serializer import ProductSchema
# contains all the routes about the music application

product = Blueprint("product", __name__, url_prefix="/api/v1/")

@product.route('/customer/<order_id>/product', methods=['GET', 'PUT', 'DELETE'])
def customer_products(order_id):
    """ customer can read , update and delete ordered product but cant create """
    data = Product.query.filter_by(ordered=order_id)
    product_schema = ProductSchema()
    result = product_schema.dump(data)
    
    if request.method == 'GET':
        if not data:
            abort(404)
        else:
            return jsonify(result), 200
        
    if request.method == 'DELETE':
        db.session.delete(result)
        db.session.commit()
        return jsonify({})
    else:
        abort(404)


@product.route('/product', methods=['GET'])
def get_all_products():
    product = Product.query.all()
    product_schema = ProductSchema()
    result = product_schema.dump(product)
    return jsonify(result)

@product.route('/product/<product_id>/')    
@product.route("/product/<product_id>")
def get_specific_product(product_id):
    """get a particular product """
    data = Product.query.filter_by(product_id=product_id).first()
    product_schema = ProductSchema()
    result = product_schema.dump(data)
    if data:
        return jsonify(result)
    abort(404)


@product.route("/artiste/<artist_id>/product", methods=['GET', 'POST'])
def get_all_product_of_artiste(artist_id):
    data = Product.query.filter_by(artist=artist_id)
    product_schema = ProductSchema()
    result = product_schema.dump(data)
    return jsonify(result)

    if request.method == 'POST':
        new_product = request.get_json()
        product_price = new_product['price']
        product_title = new_product['product_tile']
        product_date = new_product['release_date']
        product_stock = new_product['instock']

        new_data = Product(artist=artist_id, product_price=product_price, instock=product_stock, product_title=product_title, release_date=product_date)
        new_user = product_schema.dump(new_data).data
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_user)
    else:
        abort(404)

@product.route('/artiste/<artist_id>/product/<product_id>', methods=['GET', 'PUT', 'DELETE'])
def artist_product(artist_id, product_id):
    product = Product.query.filter_by(artist=artist_id, product_id=product_id)
    product_schema = ProductSchema()
    result = product_schema.dump(product)
    if request.method == 'GET':
        if product:
            return jsonify(result), 200
        else:
            abort(404)

    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
        return jsonify({"success": "Deleted successfully"}), 200
    
    if request.method == 'PUT':
        data = request.get_json()
        price = data['price']
        date = data['date']
        title = data['title']
        stock = data['stock']

        new_update = Product(artist=artist_id, product_price=price, instock=stock, product_title=title, release_date=date)
        db.session.commit()
        
