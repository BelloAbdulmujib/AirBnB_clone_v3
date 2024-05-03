#!/usr/bin/python3
"""
creating a rout that returns a JSON
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
"""view point that return json output"""
def app_status():
    return jsonify({"status": "OK"})
