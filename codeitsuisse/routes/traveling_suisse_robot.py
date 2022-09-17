from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)

@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def findTravelPath():
	Map = request.data	
	return jsonify(Map)
