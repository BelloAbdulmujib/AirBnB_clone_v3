from flask import Flask, jsonify, abort
from models import storage
from models.state import State
from api.v1.views import app_views

@app_views.route('/states', methods=['GET'])
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

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """delete the state element"""
    state = storage.get(State, state_id)
    if state_id is None:
        abort(404)
    state.delete()
    state.save()
    storage.save()
    return jsonify({}, 200)
