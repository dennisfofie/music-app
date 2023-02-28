from flask import Blueprint, jsonify, request, abort
from api.models import Order
from api import db
from .serializer import OrderSchema
# contains all the routes about the orders route

order = Blueprint("order", __name__, url_prefix="/api/v1/")

@order.route("/customer/<int:customer_id>/orders", methods=['GET', 'POST'])
def get_all_orders(customer_id):
    """get all orders of a particular customers"""

    if request.method == "GET":
        data = Order.query.filter_by(customer_id=customer_id)
        order_schema = OrderSchema()
        result = order_schema.dump(data)
        if not data:
            abort(404)

        else:
            return jsonify(result),200
    
    if request.method == 'POST':
        new_data = request.get_json()
        date = new_data['date']
        filled = new_data['filled']

        new_order = Order(customer_id=customer_id, order_date=date, filled=filled)
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"success": "order_created"}), 201
    
@order.route("/customer/<int:customer_id>/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def get_specific_order(customer_id, order_id):
    """ get single data, update this data and delete as well """
    user = Order.query.filter_by(customer_id=customer_id, order_id=order_id)

    order_schema = OrderSchema()
    result = order_schema.dump(user)

    if request.method == 'GET':
        return jsonify(result), 200
    else:
        abort(404)
    
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({}), 200
    else:
        abort(404)

    if request.method == 'PUT':
        date = request.get_json()['date']
        filled = request.get_json()['filled']

        new_order = Order(customer_id=customer_id, order_id=order_id, date=date, filled=filled)
        db.session.commit()
        return jsonify({"updated": "success"})

