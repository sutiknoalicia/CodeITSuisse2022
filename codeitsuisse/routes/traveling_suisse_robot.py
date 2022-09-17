from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
logger = logging.getLogger(__name__)

def EuclieanDistance(initial, target):
    x1, y1 = initial
    x2, y2 = target
    return ((y2-y1)**2+(x2-x1)**2)**0.5

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
		self.string = "codeitsuisse"

	def findLetterLocations(self):
		number = 12
		for i in range(0, len(self.map)):
			while number != 0:
				if any((letter in self.letterLocs.keys()) for letter in self.map[i]):
					letterLocs[letter].append(i.find(letter))
					number -= 1
				else: break

	def findNext(self, target):
		target = self.string[target]
		distances = []
		for i in range(0, len(letterLocs[target])):
			distances.append(EuclieanDistance(self.location, letterLocs[target][i]))
		distance, idx = min((distance, idx) for (idx, distance) in enumerate(distances))
		return letterLocs[target][idx]


@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)
	Map = list(map(lambda x: x.rstrip("\n\r\n"), Map))

	bot = Robot(Map)

	bot.findLetterLocations()

	return jsonify(Map) 
