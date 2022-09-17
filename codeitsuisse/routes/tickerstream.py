from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

from datetime import  datetime
@app.route("/tickerStreamPart1", methods=['GET', 'POST'])
def to_cumulative():
	stream = json.loads(request.data)["stream"]
	streamSL = [] #stores the strings inside a list
	timestamp = [] #stores the different timestamps
	streamFNL = [] #stores the return value

	#finds cumulative_notional for each timestamp (input value)
	for i in range(len(stream)):
		#streamL: converts the str into list
		streamL = stream[i].split(',')
		timestamp.append(streamL[0])
		cumulative_notional = str(float(streamL[2])*float(streamL[3]))
		streamL[3] = cumulative_notional
		#streamS: converts list into str
		streamS = ",".join(streamL)
		streamSL.append(streamS)

	#list storing all different timestamps (no repeating)
	timestamp = sorted(list(set(timestamp)))

	#combines the same tumestamps into 1 string
	for i in range(len(timestamp)):
		group = [] #stores the ticker, quantity, notion for a certain timestamp
		for j in streamSL:
			if timestamp[i] == j[0:5]:
				group.append(j[6:])
		group = sorted(group,key=lambda ticker:ticker[0])
		#sorts the ticker, quantity,notion by ticker
		group = ",".join(group)
		streamFNL.append(timestamp[i]+","+group)
	
	return jsonify({"output" : streamFNL})

@app.route("/tickerStreamPart2", methods=['GET', 'POST'])
def to_cumulative_delayed():
	stream = request.args.get("stream")
	quantity_block = request.args.get("quantityBlock")
	ticker = []
	streamFNL = []
	streamL = []
	stream = sorted(stream) #ensures timestamp is arranged chronologically

	#identifies the different tickers
	for i in range(len(stream)):
		streamL = stream[i].split(',')
		ticker.append(streamL[1])
	ticker = sorted(list(set(ticker)))

	for i in ticker: #will go through the stream for each different ticker
		cumulative_quantity, cumulative_notional = 0, float(0)
		for j in range(len(stream)):
			streamL = stream[j].split(',')
			if i == streamL[1]:
				#adds notional and quantity depending on the quantity of the stream
				for k in range(int(streamL[2])): 
					cumulative_quantity += 1
					cumulative_notional += float(streamL[3])
					if int(cumulative_quantity) == quantity_block:
						streamFNL.append(streamL[0]+","+i+","+str(cumulative_quantity)+","+str(cumulative_notional))
						break
	
	streamFNL = sorted(streamFNL)
	return jsonify({"output" : result}) #returns sorted stream where timestamps are in chronological order
