from flask import Blueprint, jsonify, request, abort
from api.models import Artiste
from api import db
from .serializer import ArtisteSchema
# contains all the routes about the music application

artiste = Blueprint("artiste", __name__, url_prefix="/api/v1/")


@artiste.route("/artiste/", methods=['GET', 'POST'])
def get_all_artiste():

    if request.method == "GET":
        """ get all artiste """
        data = Artiste.query.all()
        artiste_schema = ArtisteSchema()
        result = artiste_schema.dump(data)
        return jsonify(result)
    
    elif request.method == "POST":
        """ creates new artiste"""
        name = request.get_json()['name']
        email = request.get_json()['email']

        if not email or name:
            abort(404)

        new_user = Artiste(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success": "success"}), 201
    else:
        return jsonify({"error": "method not allowed"}), 405
    
@artiste.route("/artiste/<int:artist_id>", methods=['PUT', 'GET', 'DELETE'])
def get_artiste_by_id(artist_id):
    """ get a particular artist, update data and delete data """
    user = Artiste.query.filter_by(artist_id=artist_id).first()
    if request.method == 'GET':
        if not user:
            abort(404)
        else:
            return jsonify(user), 200
    
    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return jsonify({})
    
    if request.method == "PUT":
        data = request.get_json()
        email = data['email']
        name = data['name']

        user.name = name
        user.email = email
        db.session.commit()
        return jsonify({"user": user.name}), 200
    else:
        abort(404)
