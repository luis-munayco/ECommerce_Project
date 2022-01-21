from flask import Blueprint
from ECOMMERCE.cataloguebp import models

catalogue_bp = Blueprint('catalogue', __name__, template_folder='templates/cataloguebp')

from ECOMMERCE.cataloguebp import routes

@routes.catalogue_bp.context_processor
def inject_context():
    return {
              'categories': models.Category.query.filter_by(category_status= models.StatusType.Active).all(), 
              'brands': models.Brand.query.filter_by(brand_status=models.StatusType.Active).all(), 
              'selected_category':'all-categories',
              'selected_brand':'all-brands',
           }