from flask import (Blueprint, request, render_template, url_for, redirect) 
from datetime import datetime
from ECOMMERCE.cartbp import cart_service
from ECOMMERCE.cartbp import cart_bp

@cart_bp.route('/cart', methods=['GET','POST'])
def cart_detail():

    if request.method == "POST":
        cart_service.remove_from_cart(request)

        return render_template(
           'cart_detail.html',
           title='Product Page',
           year=datetime.now().year,
         )
    
    else:
        
        return render_template(
           'cart_detail.html',
           title='Product Page',
           year=datetime.now().year,
         )
