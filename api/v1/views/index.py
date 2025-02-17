#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"users": "User", "places": "Place", "states": "State", "cities": "City", "amenities": "Amenity", "reviews": "Review"}

@app_views.route('/status', methods=['GET'])
def status():
    """routes to status page"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def count():
    """retrieve the number of each object by type"""
    count = {}
    for cls in classes:
        count[cls] = storage.count(classes[cls])
    return jsonify(count)
