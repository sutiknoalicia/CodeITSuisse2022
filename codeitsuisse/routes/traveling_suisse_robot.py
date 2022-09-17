from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)

class Robot():
	def __init__(self, mapData):
		self.map = mapData
		self.location = None
		for i in range(0, len(mapData)):
			self.location = (i, i.index("X"))
			break
		self.letterLocs = {
			"c" : []
			"o" : []
			"d" : []
			"e" : []
			"i" : []
			"t" : []
			"s" : []
			"u" : []
		}

	def findLetterLocations:


@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)
	Map = list(map(rstrip("\n\r\n"), Map))

	bot = Robot(Map)

	return jsonify(Map)
