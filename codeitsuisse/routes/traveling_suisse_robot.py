from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)


@app.route("/traveling_suisse_robot.py", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)

	return jsonify(Map)

