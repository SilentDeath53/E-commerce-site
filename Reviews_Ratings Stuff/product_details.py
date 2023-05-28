@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get(product_id)
    ratings = Rating.query.filter_by(product_id=product_id).all()
    reviews = Review.query.filter_by(product_id=product_id).all()

    return render_template('product_details.html', product=product, ratings=ratings, reviews=reviews)
