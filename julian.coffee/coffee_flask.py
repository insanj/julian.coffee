#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from coffee import *
import os

app = Flask(__name__)

appHost = '127.0.0.1'
appPort = '5000'

serverBrowserLocation = "coffee/external/chromedriver.exe"
venmoAuthLocation = os.path.join(os.getcwd(), "coffee")
venmoAuthLocation = os.path.join(venmoAuthLocation, "external")
venmoProfileURL = "https://venmo.com/slycecoffee"

onLaunchBrowser = CoffeeBarista(serverBrowserLocation)
onLaunchBrowser.navigateToWebpage("http://" + appHost + ":" + appPort)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/coffeeTime')
def coffeeTime():
	coffeeHouse = CoffeeHouse(serverBrowserLocation, venmoAuthLocation)
	return coffeeHouse.beginCoffeeTime(venmoProfileURL)
