#!/usr/bin/python
import os
import csv

class CoffeeSafe:
	safePath = None
	loginSite ="https://venmo.com/account/sign-in/"
	loginUsername = None
	loginPassword = None
	loginUsernameSelector = ".auth-form-input[data-test=username]"
	loginPasswordSelector = ".auth-form-input[data-test=password]"
	loginSubmitSelector = ".auth-button"

	def __init__(self, safePath):
		self.setupFromConfigFile(safePath)

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
