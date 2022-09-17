from flask import Flask, jsonify, request, Response
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

@app.route("/cryptocollapz", methods=['GET', 'POST'])
def maxPrice():
	stream = json.loads(request.data)
	result = []
	for prices in stream:
		result.append([])
		for price in prices:
			temp = [int(price)]
			if temp[-1] == 1 or temp[-1] == 2:
				while temp[-1] != 4:
					if temp[-1] % 2 == 0: temp.append(temp[-1] / 2)
					else: temp.append(temp[-1] * 3 + 1)
				result[-1].append(int(max(temp)))
			else:
				result[-1].append(4)
	return jsonify(result)
