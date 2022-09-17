from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)

def strToMap(strMap):
	Map = [line.split(" ") for line in strMap.split("\n")]

@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def findTravelPath():
	Map = request.data
	Map = [line.split(" ") for line in Map.split("\n")]
	
	return jsonify(Map)
