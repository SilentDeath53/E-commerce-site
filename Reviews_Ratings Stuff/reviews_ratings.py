@app.route('/product/<int:product_id>/rate', methods=['POST'])
def rate_product(product_id):
    rating_value = int(request.form.get('rating'))

    rating = Rating(value=rating_value, product_id=product_id)
    db.session.add(rating)
    db.session.commit()

    return redirect(url_for('product_details', product_id=product_id))

@app.route('/product/<int:product_id>/review', methods=['POST'])
def review_product(product_id):
    review_content = request.form.get('review')

    review = Review(content=review_content, product_id=product_id)
    db.session.add(review)
    db.session.commit()

    return redirect(url_for('product_details', product_id=product_id))
