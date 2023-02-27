from flask import Blueprint, jsonify
# contains all the routes about the music application

views = Blueprint("views", __name__, url_prefix="/api/v1/")


@views.route("/", methods=['GET'])
def home():
    return jsonify({"error": "This is working"})

