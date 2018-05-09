#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from coffee import *

app = Flask(__name__)

serverBrowserLocation = "coffee/external/chromedriver.exe"
onLaunchBrowser = CoffeeBarista(serverBrowserLocation)
onLaunchBrowser.navigateToWebpage("http://127.0.0.1:5000")

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/coffeeTime')
def coffeeTime():
	coffeeHouse = CoffeeHouse(serverBrowserLocation)
	coffeeVenmoURL = request.args.get('url', default = '*', type = str)
	return coffeeHouse.beginCoffeeTime(coffeeVenmoURL)
