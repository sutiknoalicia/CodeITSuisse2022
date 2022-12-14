from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

count = {1 : 4, 2 : 4}


def hailstone(n):
	x = n
	if n not in count:
		temp = n
		if n == 1 or n == 2: return 4
		while n != 1:
			if n > temp:
				temp = n
			elif n % 2 == 0: n = n // 2
			else: n = n * 3 + 1
		count[x] = temp
		return temp
	else: return count[n]

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True)

	return jsonify([[hailstone(y) for y in x] for x in stream])
