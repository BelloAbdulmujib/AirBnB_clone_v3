#!/usr/bin/python3
"""Create a new view for State objects that handles all default
RESTFul API actions"""

from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def dic_states():
    """Returns the dictionary of States in state.py"""
    dico = []
    for ind in storage.all(State).values():
        dico.append(ind.to_dict())
    return jsonify(dico)


@app_views.route('/states/<path:state_id>')
def get_state(state_id):
    """Gets all the elements of State from states.py"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<path:state_id>', methods=['DELETE'],
        strict_slashes=False)
def delete_state(state_id):
    """delete the state element"""
    state = storage.get(State, state_id)
    if state_id is None:
        abort(404)
    state.delete()
    state.save()
    storage.save()
    return jsonify({})
