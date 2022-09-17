from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

from datetime import  datetime

class Ticker:
	def __init__(self, *args):
		self.timestamp = datetime.strptime(args[0], '%H:%M')
		self.ticker = args[1]
		self.quantity = int(args[2])
		self.price = float(args[3])
		self.strTime = str(self.timestamp.time())[0:5]

	def evaluatePriceSingle(self):
		self.price = self.quantity * self.price

	def seperateIntoQuantity(self):
		return [Ticker(self.strTime, self.ticker, 1, self.price) for i in range(self.quantity)]

	def __repr__(self):
		return f"{self.strTime},{self.ticker},{self.quantity},{self.price}"

	def __lt__(self, other):
		if self.timestamp == other.timestamp:
			return self.ticker < other.ticker
		return self.timestamp < other.timestamp

@app.route("/tickerStreamPart1", methods=['GET', 'POST'])
def to_cumulative():
	if request.method == 'POST':
		stream = request.args.get("stream")
		Timestamps = {}
		result = []
		for tick in stream:
			temp = Ticker(*tick.split(","))
			temp.evaluatePriceSingle()
			if temp.timestamp in Timestamps.keys():
				Timestamps[temp.timestamp] += [temp]
			else:
				Timestamps[temp.timestamp] = [temp]
		for key, tickers in Timestamps.items():
			result.append(str(key.time())[0:5])
			tickers.sort()
			for ticker in tickers:
				result[-1] += f",{ticker.ticker},{ticker.quantity},{ticker.price}"
		return jsonify({"output" : result})
		raise Exception

@app.route("/tickerStreamPart2", methods=['GET', 'POST'])
def to_cumulative_delayed():
	if request.method == "POST":
		stream = request.args.get("stream", "Parameter \'stream\' was not found")
		quantity_block = request.args.get("quantityBlock", "Parameter \'quantity block\' was not found")
		Timestamps = {}
		result = []
		for tick in stream:
			temp = Ticker(*tick.split(","))
			key = temp.ticker
			if key in Timestamps.keys():
				Timestamps[key] += temp.seperateIntoQuantity()
			else:
				Timestamps[key] = temp.seperateIntoQuantity()
		for ticks in Timestamps.keys():
			Timestamps[ticks].sort()
			cumSum = 0
			counter = 0
			for i in range(0, len(Timestamps[ticks])):
				cumSum += Timestamps[ticks][i].price
				counter += 1
				if (counter) == quantity_block:
					curr = Timestamps[ticks][i]
					result.insert(0, str(Ticker(curr.strTime, curr.ticker, counter + result[-1][2], cumSum + result[-1][3])))
					break
		return jsonify({"output" : result})
		raise Exception

