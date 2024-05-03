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


@app_views.route("/status", methods=['GET'])
def all_state():
    """ shows the objects after retrieval """
    class_object = {
        "amenities": storage.count("Amenities"),
        "cities": storage.count("Cities"),
        "places": storage.count("Places"),
        "reviews": storage.count("Review"),
        "states": storage.count("States"),
        "users": storage.count("Users")
    }
    return jsonify(class_object)
