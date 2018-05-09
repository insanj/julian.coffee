#!/usr/bin/python
import os
import csv

class CoffeeSafe():
	safePath = None

	def __init__(self, safePath):
		self.safePath = safePath

	def authWebpage(self):
		return "https://venmo.com/account/sign-in/"

	def venmoConfigFileContents(self):
		fileName = self.safePath
		print "getting file contents of " + str(fileName)
		with open(fileName, 'rb') as csvfile:
			csvreader = csv.reader(csvfile)
			csvcontents = [e for e in csvreader]
			print "contents = " + str(csvcontents)
			return csvcontents

	def authDict(self):
		config = self.venmoConfigFileContents()
		configKeys = config[0]
		configValues = config[1]
		configDict = dict(zip(configKeys, configValues))
		print "dict = " + str(configDict)
		return configDict

	def submitClass(self):
		return "auth-button"