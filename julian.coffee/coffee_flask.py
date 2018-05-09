#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from coffee import *
import os

app = Flask(__name__)

serverBrowserLocation = "coffee/external/chromedriver.exe"
venmoAuthFileLocation = os.path.join(os.getcwd(), "coffee")
venmoAuthFileLocation = os.path.join(venmoAuthFileLocation, "external")
venmoAuthFileLocation = os.path.join(venmoAuthFileLocation, "venmo.csv")

onLaunchBrowser = CoffeeBarista(serverBrowserLocation)
onLaunchBrowser.navigateToWebpage("http://127.0.0.1:5000")

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/coffeeTime')
def coffeeTime():
	coffeeHouse = CoffeeHouse(serverBrowserLocation, venmoAuthFileLocation)
	coffeeVenmoURL = request.args.get('url', default = '*', type = str)
	return coffeeHouse.beginCoffeeTime(coffeeVenmoURL)
