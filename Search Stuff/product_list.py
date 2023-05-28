@app.route('/')
def product_list():
    search_query = request.args.get('search_query', '')  # Get the search query from the URL parameter
    filters = request.args.getlist('filter')  # Get any additional filters from the URL parameters

    products = Product.query.filter(Product.name.ilike(f'%{search_query}%'))

    if filters:
        products = products.filter(Product.category.in_(filters))

    products = products.all()

    return render_template('product_list.html', products=products, search_query=search_query, filters=filters)
