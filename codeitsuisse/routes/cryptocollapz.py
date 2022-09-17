from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging
import pandas as pd

logger = logging.getLogger(__name__)

count = {1: 1}

def recur(n):
    if n not in count:  # memoize
        count[n] = 1 + recur(n//2 if n % 2 == 0 else 3*n + 1)
    return count[n]

def hailstone(n):
	temp = n
	if n == 1 or n == 2: return 4
	while n != 1:
		if n > temp:
			temp = n
		n = recur(n)
	return temp

@app.route("/cryptocollapz", methods=['GET', 'POST'])
@memoize
def maxPrice():
	stream = request.get_json(force=True)
	
	arr = pd.DataFrame(stream)
	arr = arr.applymap(lambda x: hailstone(x))

	return jsonify(arr.values.tolist())
