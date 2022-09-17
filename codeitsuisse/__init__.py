from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.tickerstream
import codeitsuisse.routes.cryptocollapz
import codeitsuisse.routes.calendar
import codeitsuisse.routes.travelingsuisserobot
