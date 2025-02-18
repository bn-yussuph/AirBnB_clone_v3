#!/usr/bin/python3
""" states """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid

@app_view.route('/states/', methods=['GET'])
def list_states():
    '''return a list of all states'''
    list_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_states)

@app_view.route('/states/', methods=['POST']
def create_state():
    '''create a new state'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201

@app_views.route('/states/<state_id>', methods=['GET']
def get_state(state_id):
    """get a single state object"""
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []
        abort(404)
    return jsonify(state_obj[0])

@app_views.route('/states/<state_id>', methods=['DELETE']
def delete_state(state_id):
    '''deletes a state'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []
        abort(404)
    state_obj.remove(state_obj[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200

@app_views.route('/states/<state_id>', methods=['PUT']
def updates_state(state_id):
    '''Updates a state object'''
    all_states = storage.all('State').values()
    state_obj = obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state_obj[0]['name'] = request.json['name']
    for obj in all_states:
        if obj.id == state-id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_obj[0]), 200
