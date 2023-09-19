#!/usr/bin/python3
""" Index view
"""
from flask import Flask
from flask import jsonify

from api.v1.views import app_views

app = Flask(__name__)

@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
