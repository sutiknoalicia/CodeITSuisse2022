from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def hailstone(n):
	temp = n
	if n == 1 or n == 2: return 4
	while n != 1:
		if n > temp:
			temp = n
		if n % 2 == 0: n = n // 2
		else: n = n * 3 + 1
	return temp

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True)
	arr = pd.DataFrame(stream)

	arr.applymap(hailstone())

	return jsonify([arr])
