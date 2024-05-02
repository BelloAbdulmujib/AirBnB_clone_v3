#!/usr/bin/python3
"""
creating a rout that returns a JSON
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def my_app_status():
    return (jsonify({"status": "OK"}))


@app_views.route("/stats", strict_slashes=False)
def all_the_stats():
    """ all json obects in the file are returned """
    class_object = {
        "amenities": storage.count("Amenities"),
        "cities": storage.count("Cities"),
        "places": storage.count("Places"),
        "reviews": storage.count("Review"),
        "states": storage.count("States"),
        "users": storage.count("Users")
    }
    return (jsonify(class_object))
