#!/usr/bin/python3
"""app entry point"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def tear(self):
    """close storage engine"""
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    code = exception.__str__().split()[0]
    message = {"error": "Not found"}
   # if code == 404:
   #     message = {"error": "Not found"}
    return make_response(jsonify(message), code)

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
