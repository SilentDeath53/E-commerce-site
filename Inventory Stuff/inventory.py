@app.route('/')
def product_list():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@app.route('/place_order', methods=['POST'])
def place_order():
    

    order = Order(customer_name=customer_name, customer_email=customer_email, product_id=product_id)

    product = Product.query.get(product_id)
    product.inventory -= 1

    db.session.add(order)
    db.session.commit()

    # ...

@app.route('/place_order', methods=['POST'])
def place_order():
    
    product = Product.query.get(product_id)
    if product.inventory <= 0:
        return "Product is out of stock"

    product.inventory -= 1

    db.session.add(order)
    db.session.commit()

    # ...
    
