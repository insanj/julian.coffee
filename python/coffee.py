#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from coffee_barista import *

app = Flask(__name__)

@app.route('/')
def coffeeTime():
	# goal: -> take in a request with a venmo URL
	#		<- send out a response that requires (1) logging into venmo (2) accessing the URL (3) sending back the webpage (JSON? HTML if need be)
	
	
	return 