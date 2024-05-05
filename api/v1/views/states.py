#!/usr/bin/python3
"""Create a new view for State objects that handles all default
RESTFul API actions"""
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Gets all the elements of State from states.py"""
    dico = []
    for index in storage.all(State).values():
        dico.append(index.to_dict())
    return jsonify(dico)


@app_views.route('/states/<path:state_id>')
def get_state(state_id):
    """Gets the state with id number"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<path:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """delete the state element"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """post a request via http and updating the object"""
    result = request.get_json()
    if type(result) != dict:
        return abort(400, {'message': 'Not a JSON'})
    if 'name' not in result:
        return abort(400, {'message': 'Missing name'})
    dic_state = State(**result)
    dic_state.save()
    return jsonify(dic_state.to_dict()), 201


@app_views.route('/states/<path:state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """Put method in restapi that save the initial setup via http"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    res = request.get_json()
    if type(res) != dict:
        return abort(400, {'message': 'Not a JSON'})
    for key, value in res.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
