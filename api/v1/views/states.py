from flask import Flask, jsonify, abort
from models import models
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'])
def get_states():
    dico = []
    for ind in storage.all(State).values():
        dico.append(val.to_dict())
    return (jsonify(dico)
