#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from coffee import *
import os
from twilio import twiml

app = Flask(__name__)

appHost = '127.0.0.1'
appPort = '5000'

serverBrowserLocation = "coffee/external/chromedriver"
venmoAuthLocation = os.path.join(os.getcwd(), "coffee")
venmoAuthLocation = os.path.join(venmoAuthLocation, "external")
venmoProfileURL = "https://venmo.com/slycecoffee"

# onLaunchBrowser = CoffeeBarista(serverBrowserLocation)
# onLaunchBrowser.navigateToWebpage("http://" + appHost + ":" + appPort)

coffeeHouse = CoffeeHouse(serverBrowserLocation, venmoAuthLocation)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/coffeeTime')
def coffeeTime():
	return coffeeHouse.beginCoffeeTime(venmoProfileURL)

@app.route('/sms', methods=['POST'])
def sms():
	number = request.form['From']
	message_body = request.form['Body']
	print str(message_body)
	verificationNumber = str(message_body).split()[-1]
	coffeeHouse.rememberVerificationNumber(verificationNumber)
	return "success"