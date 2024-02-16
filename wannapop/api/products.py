from . import api_bp
from .errors import not_found, bad_request
from .. import db_manager as db
from ..models import Product, Category, Order
from ..helper_json import json_request, json_response
from flask import current_app, jsonify, request

#List
@api_bp.route('/products', methods=['GET'])
def get_product_filtred():
    title = request.args.get('title')
    if title:
        Product.db_enable_debug()
        products_with_title = Product.query.filter_by(title=title).all()
    else:
        products_with_title = []
    data = Product.to_dict_collection(products_with_title)
    return jsonify(
            {
                'data': data, 
                'success': True
            }), 200


@api_bp.route('/products/<int:product_id>/orders', methods=['GET'])
def listar_ofertas_por_producto(product_id):
    orders = Order.query.filter_by(product_id=product_id).all()
    if orders:
        data = [order.to_dict() for order in orders]
        return jsonify(
        {
            'data': data, 
            'success': True
        }), 200    
    else:
        return not_found('No offers found for the specified product')
    
#Show
@api_bp.route('/products/<int:id>', methods=['GET'])
def get_api_product_show(id):
    result = Product.get_with(id, Category)
    if result:
        (product, category) = result
        # Serialize data
        data = product.to_dict()
        # Add relationship
        data["category"] = category.to_dict()
        del data["category_id"]
        return jsonify(
            {
                'data': data, 
                'success': True
            }), 200  
    else:
        current_app.logger.debug(f"Product {id} not found")
        return not_found("Product not found")
    
# Update
@api_bp.route('/products/<int:id>', methods=['PUT'])
def update_api_product(id):
    product = Product.get(id)
    if product:
        try:
            data = json_request(['title', 'description', 'photo', 'price', 'category_id'], False)
        except Exception as e:
            current_app.logger.debug(e)
            return bad_request(str(e))
        else:
            product.update(**data)
            current_app.logger.debug("UPDATED item: {}".format(product.to_dict()))
            return jsonify(
                {
                    'data': product.to_dict(), 
                    'success': True
                }), 200 
    else:
        current_app.logger.debug(f"Product {id} not found")
        return not_found("Product not found")






##########################################
##          ANTERIOR CODIGO             ##
##########################################

# from . import api_bp
# from .errors import not_found, bad_request
# from ..models import Product, Category
# from ..helper_json import json_request, json_response
# from flask import current_app, request

# LIST
# @api_bp.route('/products', methods=['GET'])
# def get_products_list():
#     search = request.args.get('search')
#     if search:
#         Product.db_enable_debug()
#         my_filter = Product.nom.like('%' + search + '%')
#         products_with_category = Product.db_query_with(Category).filter(my_filter)
#     else:
#         products_with_category = Product.get_all_with(Category)
#     data = Product.to_dict_collection(products_with_category)
#     return json_response(data)

# # CREATE
# @api_bp.route('/products', methods=['POST'])
# def create_product():
#     try:
#         data = json_request(['nom', 'category_id', 'unitats'])
#     except Exception as e:
#         current_app.logger.debug(e)
#         return bad_request(str(e))

# # READ
# @api_bp.route('/products/<int:product_id>', methods = ['GET'])
# def get_product(product_id):
#     result = Product.get_with(id, Category)
#     if result:
#         (product, category, discount) = result
#         data = product.to_dict()
#         data["store"] = category.to_dict()
#         del data["store_id"]
#         if (discount):
#             data["discount"] = discount.discount
#         return json_response(data)
#     else:
#         current_app.logger.debug("Product {} not found".format(product_id))
#         return not_found("Product not found")

# # UPDATE
# @api_bp.route('/products/<int:product_id>', methods = ['PUT'])
# def update_product(product_id):
#     product = Product.get(id)
#     if product:
#         try:
#             data = json_request(['nom', 'category_id', 'unitats'], False)
#         except Exception as e:
#             current_app.logger.debug(e)
#             return bad_request(str(e))
#         else:
#             product.update(**data)
#             current_app.logger.debug("UPDATED product: {}".format(product.to_dict()))
#             return json_response(product.to_dict())
#     else:
#         current_app.logger.debug("Product {} not found".format(product_id))
#         return not_found("Product not found")

# # DELETE
# @api_bp.route('/products/<int:product_id>', methods = ['DELETE'])
# def delete_product(product_id):
#     product = Product.get(product_id)
#     if product:
#         product.delete()
#         current_app.logger.debug("DELETED product: {}".format(id))
#         return json_response(product.to_dict())
#     else:
#         current_app.logger.debug("Product {} not found".format(id))
#         return not_found("Product not found")
