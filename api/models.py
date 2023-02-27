from . import db
from flask_login import UserMixin
from datetime import datetime

class Customer(db.Model):
    # customer purchasing the product
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(500))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    country = db.Column(db.String(100))
    zip = db.Column(db.String(100))
    orders = db.Column(db.Integer, db.ForeignKey('order.order_id'))

    def __str__(self):
        return "{} {}".format(self.firstname, self.last_name)
    
class Artiste(db.Model):
    # artist creating the songs in each product
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(150))
    artist_email = db.Column(db.String(100), unique=True)
    artist_songs = db.relationship("Product")

    def __str__(self):
        return "{}".format(self.artist_name)
    
class Order(db.Model):
    # order songs
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, default=datetime.utcnow())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    filled = db.Column(db.Boolean, default=False)
    ordered_products = db.relationship('Product')

    def __str__(self):
        return "{}".format(self.order_date)
    
class Song(db.Model):
    # songs in each product like album
    song_id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.Integer, db.ForeignKey('artiste.artist_id'))
    song_title = db.Column(db.String(100))
    song_description = db.Column(db.String(1000))
    product_song = db.Column(db.Integer, db.ForeignKey('product.product_id'))

    def __str__(self):
        return f"{self.song_title}"

class Product(db.Model):
    # album product containing songs which can be order
    product_id = db.Column(db.Integer, primary_key=True)
    product_price = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.Integer, nullable=False, default=datetime.utcnow())
    product_title = db.Column(db.String(100), nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    ordered = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    product_song = db.relationship('Song')



    def __str__(self):
        return f"${self.product_price}"


