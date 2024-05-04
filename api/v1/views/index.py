#!/usr/bin/python3
"""
creating a rout that returns a JSON
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'])
def status():
    """ func of status """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'])
def all_state():
    """Display the objects after retrieval """
    class_object = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(class_object)
