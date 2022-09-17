from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

def hailstone(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True)
	for key1, prices in enumerate(stream):
		for key2, price in enumerate(prices):
			if not price == 1 or not price == 2:
				temp = price
				while price != 2:
					if price > temp:
						temp = price
					price = hailstone(price)
				stream[key1][key2] = price
			else:
				stream[key1][key2] = 4
	return jsonify(stream)
