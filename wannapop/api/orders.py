from . import api_bp
from .errors import not_found, bad_request
from .. import db_manager as db
from ..models import Order, ConfirmedOrder
from ..helper_json import json_request, json_response
from flask import current_app, jsonify, request

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
def hacer_oferta():
    datos_oferta = request.get_json()
    order_id = db.generar_id_unico(Order)
    nueva_order = Order(id=order_id, producto=datos_oferta["producto"], precio=datos_oferta["precio"])

    try:
        nueva_order.save()
    except:
        return bad_request('Error al hacer la oferta')  

    current_app.logger.debug(f"Order {order_id} creada exitosamente")

    return jsonify(
        {
            "data": {"id": order_id, "message": f"Order {order_id} creada exitosamente"},
            "success": True
        }), 200

@api_bp.route('/orders/<int:order_id>', methods=['PUT'])
def editar_oferta(order_id):
    order = Order.query.get(order_id)

    if order:
        datos_oferta = json_request()

        order.producto = datos_oferta.get("producto", order.producto)
        order.precio = datos_oferta.get("precio", order.precio)

        try:
            order.save()
        except:
            return bad_request('Error al editar la oferta')

        current_app.logger.debug(f"Order {order_id} editada exitosamente")
        return jsonify(
            {
                "data" : order_id,
                "success": True
            }), 200
    else:
        return not_found('Order no encontrada')

@api_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def cancelar_oferta(order_id):
    order = Order.query.get(order_id)

    if order:
        try:
            order.delete()
        except:
            return bad_request('Error al cancelar la oferta')

        current_app.logger.debug(f"Order {order_id} cancelada exitosamente")
        return jsonify(
            {
                "data" : order_id,
                "success": True
            }), 200    
    else:
        return not_found('Order no encontrada')       
    
