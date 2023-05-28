@app.route('/')
def product_list():
    products = Product.query.all()
    return render_template('product_list.html', products=products)
