from flask import Blueprint
from . import models

cart_bp = Blueprint('cart', __name__, template_folder='templates/cartbp')

from ECOMMERCE.cartbp import routes
