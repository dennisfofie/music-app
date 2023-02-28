from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
# creating a server using the flask


load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "This is my secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)

from .auth import auth
from .routes import views
from .artiste_routes import artiste
from .orders_route import order
from .products_routes import product

app.register_blueprint(views)
app.register_blueprint(auth)
app.register_blueprint(order)
app.register_blueprint(product)
app.register_blueprint(artiste)