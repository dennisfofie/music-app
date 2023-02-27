from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# creating a server using the flask


load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "This is my secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)

    create_database(app)
    from .auth import auth
    from .routes import views

    app.register_blueprint(views)
    app.register_blueprint(auth)


    return app


def create_database(app):
    with app.app_context():
        if not path.exists("api/database.db"):
            db.create_all()
            print("Database created successfully")
    