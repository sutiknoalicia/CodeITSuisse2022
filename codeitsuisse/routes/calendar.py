from flask import Flask, jsonify, request
from codeitsuisse import app
import json
import logging

logger = logging.getLogger(__name__)

#part 1

import datetime
import string

dayLetter = ['m', 't', 'w', 't', 'f', 's', 's']

months = [[False for i in range(7)] for x in range(12)]

monthDays = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

output = ["       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,", "       ,"]

def checkAllWeek(m: list):
    for i in range(7):
        if not m[i]:
            return False
    return True

def checkWeekday(m: list):
    if not m[5] and not m[6] and m[0] and m[1] and m[2] and m[3] and m[4]:
        return True
    return False

def checkWeekend(m: list):
    if m[5] and m[6] and not m[0] and not m[1] and not m[2] and not m[3] and not m[4]:
        return True
    return False

@app.route("/calendarDays", methods=['GET', 'POST'])

def calendar():
    #part1
    stream = json.loads(request.data)
    year = stream[0]
    firstDate = datetime.datetime(year, 1, 1)
    for i in range(1, len(stream)):
        days = stream[i] - 1
        thisDate = firstDate + datetime.timedelta(days)
        day = thisDate.weekday()
        months[thisDate.month - 1][day] = True

    for i in range(12):
        thisMonth = months[i]
        if checkAllWeek(thisMonth):
            output[i] = "alldays,"
        elif checkWeekday(thisMonth):
            output[i] = "weekday,"
        elif checkWeekend(thisMonth):
            output[i] = "weekend,"
        else:
            for x in range(7):
                if thisMonth[x]:
                    new = list(output[i])
                    new[x] = dayLetter[x]
                    output[i] = "".join(new)
    
    output = "".join(output)
    
    #part2
    for i in range(len(calendar)):
        if calendar[i] == ' ':
            year = 2001 + i
            break

    if year % 4 == 0:
        monthDays[2] += 1

    calList = calendar.split(',')
    output2 = []

    for i in range(12):
        firstDate = datetime.datetime(year, i+1, 1)
        firstDay = firstDate.weekday()

        offset = 0
        for x in range(i+1):
            offset += monthDays[x]

        if calList[i] == "alldays":
            for x in range(7):
                output2.append(offset+x)

        elif calList[i] == "weekday":
            untilWeekend = 5 - firstDay
            counter = 0

            if untilWeekend > 0:
                for x in range(untilWeekend):
                    counter += 1
                    offset += x
                    output2.append(offset)
                offset += 3
            else:
                offset += (7 - firstDay)
            counter = 5 - counter
            for x in range(counter):
                output2.append(offset+x)

        elif calList[i] == "weekend":
            untilWeekend = 5 - firstDay

            if untilWeekend < 0:
                output2.append(offset)
                offset += 6
                output2.append(offset)
            elif untilWeekend > 0:
                for x in range(untilWeekend+1):
                    offset += x
                for x in range(2):
                    output2.append(offset+x)
            elif untilWeekend == 0:
                for x in range(2):
                    output2.append(offset+x)
        
        else:
            for x in range(7):
                if calList[i][x] != ' ':
                    thisDay = dayLetter.index(calList[i][x])
                    diff = thisDay - firstDay
                    if diff < 0:
                        diff += 7
                    output2.append(offset+diff)
        
    output2.sort()
    output2.insert(0, year)
    return jsonify({"part1" : output , "part2" : output2})
