from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True)
	for key1, prices in enumerate(stream):
		for key2, price in enumerate(prices):
			if not price == 1 or not price == 2:
				temp = [price]
				while temp[-1] != 2:
					if temp[-1] % 2 == 0: temp.append(temp[-1] / 2)
					else: temp.append(temp[-1] * 3 + 1 / 2)
				stream[key1][key2] = int(max(temp))
			else:
				stream[key1][key2] = 4
	return jsonify(stream)
