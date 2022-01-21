from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

def create_app(settings_module):
    
    # Create app
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the config file specified by the APP environment variable
    app.config.from_object(settings_module)
    
    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py', silent=True)

    # Register Blueprints
    from .cataloguebp import catalogue_bp
    app.register_blueprint(catalogue_bp)

    from .cartbp import cart_bp
    app.register_blueprint(cart_bp)

    from .locationbp import location_bp
    app.register_blueprint(location_bp)

    from .userbp import user_bp
    app.register_blueprint(user_bp)

    from .orderbp import order_bp
    app.register_blueprint(order_bp)

    from .checkoutbp import checkout_bp
    app.register_blueprint(checkout_bp)

    # Context processor
    from .cartbp import cart_service
    @app.context_processor
    def inject_context():
        return {
                'cart_item_count': cart_service.cart_items_count(request,session),
                'cart_total': cart_service.get_cart_total(request, session),
                'cart_items': cart_service.get_cart_items(request,session),
            }

    #Register the product catalogue models to the Admin Module
    from ECOMMERCE.cataloguebp.models import Brand, Category, Product
    admin=Admin(app)
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Category, db.session))
    admin.add_view(ModelView(Brand, db.session))

    from ECOMMERCE.userbp.models import Person, Customer
    admin.add_view(ModelView(Person, db.session))
    admin.add_view(ModelView(Customer, db.session))

    from ECOMMERCE.locationbp.models import Address
    admin.add_view(ModelView(Address, db.session))

    # Init SQLAlchemy
    db.init_app(app)
    migrate=Migrate(app,db)

    return app
