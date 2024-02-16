from . import api_bp
from .errors import not_found
from .. import db_manager as db
from ..models import Category, Order
from ..helper_json import json_response
from flask import current_app

@api_bp.route('/categories', methods=['GET'])
def get_api_categories():
    categories = Category.get_all()
    data = Category.to_dict_collection(categories)
    return json_response(data)

# Items list
@api_bp.route('/categories/<int:id>/product', methods=['GET'])
def get_category_product(id):
    product = Product.get_all_filtered_by(cateogry_id=id)
    data = Product.to_dict_collection(product)
    return json_response(data)