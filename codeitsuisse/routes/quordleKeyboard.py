from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

import numpy as np

def partition5(l):
    for i in range(0, len(l), 5):
        yield l[i: i+5]

@app.route("/quordleKeyboard", methods=['GET', 'POST'])

def quordle():
    if request.method == 'POST':
        stream1 = request.get_json["answers"]
        stream2 = request.get_json["attempts"]
        allLetters = []
        letterGreyed = {chr(x): 0 for x in range(65, 91)}
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        #part1

        allLetters = {x: [y for y in x] for x in stream1}
        part1steps = []

        print("         " + "".join(alphabet))
        for x in stream2:
            doneLetters = []
            if x in stream1:
                del allLetters[x]
            allLettersList = list(allLetters.values())
            allLettersList = np.array(allLettersList)

            for y in x:
                if y not in allLettersList and y not in doneLetters:
                    alphabet2[alphabet.index(y)] = ' '
                    doneLetters.append(y)
            
            for i in range(len(alphabet2)):
                if alphabet2[i] == ' ':
                    letterGreyed[alphabet[i]] += 1

            part1steps.append(x + "    " + "".join(alphabet2))

        ans = ""
        for i in range(65, 91):
            if letterGreyed[chr(i)] != 0:
                ans = ans + str(letterGreyed[chr(i)])
        
        #part2

        stream3 = request.get_json["numbers"]
        pNums = list(partition5(stream3))
        fiveBin = [[0,0,0,0,0] for i in range(5)]
        denaries = ['', '', '', '', '']

        for i in range(5):
            for j in range(5):
                thisNum = str(pNums[i][j])
                fiveBin[i][j] = int(thisNum in ans)
        
        for i in range(5):
            den = int("".join(str(x) for x in fiveBin[i]), 2)
            denaries[i] = alphabet[den-1]
            
        lastLine = part1steps[-1]
        remainLetters = ""

        for i in range(5, len(lastLine)):
            if lastLine[i] != ' ':
                remainLetters += lastLine[i]
        
        ans2 = "".join(denaries) + remainLetters
        return jsonify({"part1" : ans, "part2" : ans2})
