from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
import numpy as np

logger = logging.getLogger(__name__)

def hailstone(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True)
	
	arr = np.asarray(stream, dtype='int64')
	
	for price in np.nditer(arr, op_flags=['readwrite'], flags=["refs_ok"]):
		if price == 1 or price == 2:
			price = 4
		else:
			temp = price
			while price != 1:
				if price > temp:
					temp = price
				price = hailstone(price)
			price = temp
	
	return jsonify(arr.tolist())
