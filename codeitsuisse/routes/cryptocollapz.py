from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = request.get_json(force=True) 
	result = []
	for prices in stream:
		result.append([])
		for price in prices:
			temp = [int(price)]
			if temp[-1] == 1: result[-1].append(4)
			elif temp[-1] == 2: result[-1].append(4)
			else:
				while temp[-1] != 1:
					if temp[-1] % 2 == 0: temp.append(temp[-1] / 2)
					else: temp.append(temp[-1] * 3 + 1)
				result[-1].append(int(max(temp)))
	Response(json.dumps({"data" : result}), mimetype='application/json')
