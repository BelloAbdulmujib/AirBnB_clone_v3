#!/usr/bin/python3
"""
creating a rout that returns a JSON
"""
from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.city impory City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models import storage


@app_views.route('/status', strict_slashes=False)
"""view point that return json output"""
def app_status():
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def point_stats():
    """all json obects in the file are returned """
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    })
