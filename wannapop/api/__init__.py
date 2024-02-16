<<<<<<< HEAD
from flask import Blueprint

api_bp = Blueprint('api', __name__)

# necessari per a que es carreguin les rutes
from . import products, categories, errors, orders, statuses, users
=======
from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import products, categories, errors, orders
>>>>>>> 34fa2dd9d57cdc8b99fc46b8ad56e54c7dc0ede4
