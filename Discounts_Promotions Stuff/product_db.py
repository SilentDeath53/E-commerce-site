class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image = db.Column(db.String(200))
    discount_price = db.Column(db.Float)  

    def __repr__(self):
        return f'<Product {self.name}>'
