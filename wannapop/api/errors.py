<<<<<<< HEAD
from . import api_bp
from ..helper_json import json_error_response
from werkzeug.exceptions import HTTPException

def bad_request(message):
    return json_error_response(400, message)

def forbidden_access(message):
    return json_error_response(403, message)

def not_found(message):
    return json_error_response(404, message)

# Catch all HTTP exceptions
# For example: abort(401)
@api_bp.errorhandler(HTTPException)
def handle_exception(e):
=======
from . import api_bp
from ..helper_json import json_error_response
from werkzeug.exceptions import HTTPException

def bad_request(message):
    return json_error_response(400, message)

def forbidden_access(message):
    return json_error_response(403, message)

def not_found(message):
    return json_error_response(404, message)

# Catch all HTTP exceptions
# For example: abort(401)
@api_bp.errorhandler(HTTPException)
def handle_exception(e):
>>>>>>> 34fa2dd9d57cdc8b99fc46b8ad56e54c7dc0ede4
    return json_error_response(e.code)