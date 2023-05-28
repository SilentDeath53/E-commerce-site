@app.route('/apply_discount', methods=['POST'])
def apply_discount():
    discount_code = request.form.get('discount_code')

    discount = Discount.query.filter_by(code=discount_code).first()

    if discount:
        # Apply the discount to the cart or specific products
        # Update the prices of the discounted products if necessary
        # Calculate the total discounted amount

        return redirect(url_for('cart'))
    else:
        flash('Invalid discount code', 'danger')
        return redirect(url_for('cart'))
