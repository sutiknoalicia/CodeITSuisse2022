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
			self.location = (i, mapData[i].find("X"))
			break
		self.letterLocs = {
			"c" : [],
			"o" : [],
			"d" : [],
			"e" : [],
			"i" : [],
			"t" : [],
			"s" : [],
			"u" : [],
		}

	def findLetterLocations(self):
		number = 12
		for i in range(0, len(self.map)):
			while number != 0:
				if any(letter in self.letterLocs.keys for letter in self.map[i]):
					letterLocs[letter].append(i.index(letter))
					number -= 1
				else: break

@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)
	Map = list(map(lambda x: x.rstrip("\n\r\n"), Map))

	bot = Robot(Map)

	return jsonify(Map) 
