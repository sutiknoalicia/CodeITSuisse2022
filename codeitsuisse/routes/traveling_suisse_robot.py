def EuclieanDistance(initial, target):
    x1, y1 = initial
    x2, y2 = target
    return ((y2-y1)**2+(x2-x1)**2)**0.5

class Robot():
	def __init__(self, mapData):
		self.map = mapData
		self.location = None
		for i in range(0, len(mapData)):
			if (mapData[i].find("X")) != -1:
				self.location = (i, mapData[i].find("X"))
				break
		self.letterLocs = {
			"C" : [],
			"O" : [],
			"D" : [],
			"E" : [],
			"I" : [],
			"T" : [],
			"S" : [],
			"U" : [],
		}
		self.string = "CODEITSUISSE"

	def findLetterLocations(self):
		for idx1, i1 in enumerate(self.map):
			for idx2, i2 in enumerate(i1):
				if i2 in self.letterLocs.keys():
					self.letterLocs[i2].append((idx1, idx2))


	def findNext(self, target):
		original = target
		target = self.string[target]
		distances = []
		for i in self.letterLocs[target]:
			distances.append(EuclieanDistance(self.location, i))
		distance, idx = min((distance, idx) for (idx, distance) in enumerate(distances))
		return self.letterLocs[target][idx]

	def pathFind(self):
		path = ""
		for i in range(0, len(self.string)):
			coordinates = self.findNext(i)
			if coordinates:
				newPath = tuple(map(lambda i, j: i - j, self.location, coordinates))
				if newPath[1] > 0: path += "R"
				elif newPath[1] == 0: pass
				else: path += "L"
				path += newPath[0] * "S"
				path += "P"
		return path


@app.route("/traveling-suisse-robot", methods=['GET', 'POST'])
def main():
	Map = request.get_data().decode('utf-8').strip()
	Map = Map.splitlines(True)
	Map = list(map(lambda x: x.rstrip("\n\r\n"), Map))

	bot = Robot(Map)

	bot.findLetterLocations()

	return (bot.pathFind())
