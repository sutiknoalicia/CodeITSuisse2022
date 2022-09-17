from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)

@app.route("/travelling-suisse-robot", methods=['GET', 'POST'])
@accept('text/plain')
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)

	return jsonify(Map)
