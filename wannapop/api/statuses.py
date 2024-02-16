from . import api_bp
from .errors import not_found, bad_request
from .. import db_manager as db
from ..models import Status, ConfirmedOrder, Category
from ..helper_json import json_request, json_response
from flask import current_app, jsonify

@api_bp.route('/statuses', methods=['GET'])
def get_statuses_list():
    statuses = Status.get_all()
    data = Status.to_dict_collection(statuses)
    return jsonify(
        {
            "data" : data,
            "success": True
        }), 200