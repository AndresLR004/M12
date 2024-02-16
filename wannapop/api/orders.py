from . import api_bp
from .errors import not_found, bad_request
from .. import db_manager as db
from ..models import Order, ConfirmedOrder, Product
from ..helper_json import json_request, json_response, json_error_response
from flask import current_app, jsonify, request, g
from .helper_auth import token_auth


@api_bp.route('/orders/<int:order_id>/confirmed', methods=['POST'])
def accept_order(order_id):
    order = Order.query.get(order_id)

    if order:
        if order.confirmed_order:
            return bad_request('Order already confirmed')

        confirmed_order = ConfirmedOrder(order=order)
        
        try:
            confirmed_order.save()
        except:
            return bad_request('Error confirming the order')

        current_app.logger.debug(f"Order {order_id} confirmed successfully")
        return json_response({'message': f'Order {order_id} confirmed successfully'})
    else:
        return not_found('Order not found')
    
@api_bp.route('/orders/<int:order_id>/confirmed', methods=['DELETE'])
def cancel_confirmed_order(order_id):
    confirmed_order = ConfirmedOrder.query.get(order_id)

    if confirmed_order:
        # Elimina la entrada de confirmed_orders
        try:
            confirmed_order.delete()
        except:
            return bad_request('Error canceling the confirmed order')

        current_app.logger.debug(f"ConfirmedOrder {order_id} canceled successfully")
        return json_response({'message': f'ConfirmedOrder {order_id} canceled successfully'})
    else:
        return not_found('ConfirmedOrder not found')
 
@api_bp.route('/orders', methods=['POST'])
@token_auth.login_required
def hacer_oferta():
    try:
        data = json_request(['product_id'])
    except Exception as e:
        current_app.logger.debug(e)
        return bad_request(str(e))

    product = Product.query.get(data['product_id'])

    if not product:
        return jsonify({'error': 'Not Found', 
                        'message': 'Product not found', 
                        'success': False
                        }), 404

    if product.seller_id == g.current_user.id:
        return jsonify({'error': 'Forbidden', 
                        'message': 'Cannot order your own product', 
                        'success': False
                        }), 403

    new_order_data = {'buyer_id': g.current_user.id, 'product_id': data['product_id']}
    new_order = Order.save(**new_order_data)

    current_app.logger.debug("CREATED order: {}".format(new_order.to_dict()))

    return json_response(new_order.to_dict(), 201)

@api_bp.route('/orders/<int:order_id>', methods=['PUT'])
@token_auth.login_required
def editar_oferta(order_id):

    order = Order.get(order_id)
    if order:
        if order.buyer_id != g.current_user.id:
            return json_error_response("You are not authorized to edit this order.")
        try:
            data = json_request(['product_id', 'offer'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            order.update(**data)
            current_app.logger.debug("UPDATE order: {}".format(order.to_dict()))
            return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")

@api_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@token_auth.login_required
def cancelar_oferta(order_id):
    
    order = Order.get(order_id)
    if order:
        if order.buyer_id != g.current_user.id:
            return json_error_response(401, "You are not authorized to cancel this order.")
        if order.confirmed_order:
            return json_error_response(400, "Cannot cancel a confirmed order.")
        order.delete()
        current_app.logger.debug("DELETE order: {}".format(order_id))
        return json_response(order.to_dict())
    else:
        current_app.logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")  
