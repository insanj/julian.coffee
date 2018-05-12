#!/usr/bin/python
import os
import csv
import json
from coffee_cookie import *

class CoffeeSafe:
	safePath = None
	loginSite ="https://venmo.com/account/sign-in/"
	loginUsername = None
	loginPassword = None
	loginUsernameSelector = ".auth-form-input[data-test=username]"
	loginPasswordSelector = ".auth-form-input[data-test=password]"
	loginSubmitSelector = ".auth-button"
	
	cookie = None

	def __init__(self, safePath, venmoCredsFilename="venmo.csv", cookieFilename="coffee_cookie"):
		venmoPath = os.path.join(safePath, venmoCredsFilename)
		self.setupFromConfigFile(venmoPath)
		self.cookie = CoffeeCookie(safePath, cookieFilename)

	def setupFromConfigFile(self, safePath):
		with open(safePath, 'rb') as csvfile:
			csvreader = csv.reader(csvfile)
			csvcontents = [e for e in csvreader]
			self.setupFromConfigFileContents(csvcontents)

	def setupFromConfigFileContents(self, config):
		configKeys = config[0]
		configValues = config[1]
		configDict = dict(zip(configKeys, configValues))
		self.loginUsername = configDict["username"]
		self.loginPassword = configDict["password"]

