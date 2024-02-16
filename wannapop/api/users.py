from . import api_bp
from .errors import not_found, bad_request
from .. import db_manager as db
from ..models import Order, ConfirmedOrder, User, Product
from ..helper_json import json_request, json_response
from flask import current_app, jsonify, request

   
@api_bp.route('/users', methods=['GET'])
def users_list():
    name = request.args.get('name')
    if name:
        User.db_enable_debug()
        user_whith_name = User.query.filter_by(name=name).all()
    else:
        user_whith_name = []
    data = User.to_dict_collection(user_whith_name)
    return jsonify(
            {
                'data': data, 
                'success': True
            }), 200

@api_bp.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    result = User.get_with(id, Order)
    if result:
        (user, order) = result
        data = user.to_dict()
        data['order'] = order.to_dict()
        del data ["order_id"]
        return jsonify(
            {
                "data" : data,
                "success": True
            }), 200
    else:
        return not_found("Order not found")   
    
    
@api_bp.route('/users/<int:seller_id>/products', methods=['GET'])
def list_product_user(seller_id):
    products = Product.query.filter_by(seller_id=seller_id).all()
    if products:
        data = [product.to_dict() for product in products]
        return jsonify(
            {
                "data" : data,
                "success": True
            }), 200
    else:
        return not_found('No products for the especified user')