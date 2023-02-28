from flask import Flask, current_app
from os import path
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
# creating a server using the flask


db = SQLAlchemy()


app = Flask(__name__)
app.config["SECRET_KEY"] = "This is my secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
ma = Marshmallow(app)

    
from .auth import auth
from .artiste_routes import artiste
from .orders_route import order
from .products_routes import product

app.register_blueprint(artiste)
app.register_blueprint(auth)
app.register_blueprint(order)
app.register_blueprint(product)