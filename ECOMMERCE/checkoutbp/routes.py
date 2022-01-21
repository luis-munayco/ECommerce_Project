from flask import (Blueprint, request,session, render_template, url_for, redirect) 
from datetime import datetime
from ECOMMERCE.checkoutbp.forms import CheckoutForm
from ECOMMERCE.checkoutbp import checkout_service
from ECOMMERCE.checkoutbp import checkout_bp

@checkout_bp.route('/checkout', methods=['GET','POST'])
def checkout_view():
    if request.method == "POST":
        result  = checkout_service.process_checkout(request,session)
        if result:
           return redirect(url_for('checkout.receipt_view'))
        else:
           return redirect(url_for('checkout.receipt_view'))
    else:
       form = CheckoutForm()

       return render_template(
           'checkout.html',
           title='Checkout Page',
           year=datetime.now().year,
           form = form,
         )

@checkout_bp.route('/checkout/receipt')
def receipt_view():

    return render_template(
           'receipt.html',
           title='Receipt Page',
           year=datetime.now().year,
         )
