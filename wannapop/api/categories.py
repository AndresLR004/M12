from . import api_bp
from ..models import Category, Product
from ..helper_json import json_response
from flask import current_app

# List
@api_bp.route('/category', methods=['GET'])
def get_category():
    categories = Category.get_all()
    data = Category.to_dict_collection(categories)
    return json_response(data)

# Items list
@api_bp.route('/categories/<int:id>/product', methods=['GET'])
def get_category_product(id):
    product = Product.get_all_filtered_by(cateogry_id=id)
    data = Product.to_dict_collection(product)
    return json_response(data)