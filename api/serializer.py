from . import ma
from .models import Customer, Order, Song, Product, Artiste

class CustomerSchema(ma.Schema):
    class meta:
        model = Customer


class OrderSchema(ma.Schema):
    class meta:
        model = Order

class ProductSchema(ma.Schema):
    class meta:
        model = Product


class ArtisteSchema(ma.Schema):
    class meta:
        model = Artiste


class SongSchema(ma.Schema):
    class meta:
        model = Song
