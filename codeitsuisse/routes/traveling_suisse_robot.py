from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)
	Map = list(map(lambda x: x.rstrip("\n\r\n"), Map))
	Map = list(map(lambda x: x.split(""), Map))

	return jsonify(Map)

