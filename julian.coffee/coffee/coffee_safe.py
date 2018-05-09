#!/usr/bin/python
import os
import csv

class CoffeeSafe():
	def authWebpage(self):
		return "https://venmo.com/account/sign-in/"

	def venmoConfigFileContents(self):
		filePath = "venmo.csv"
		configContents = []
		with open(filePath, 'rb') as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',')
			for csvelement in csvreader:
				configContents.append(csvelement)
			return configContents

	def authDict(self):
		config = self.venmoConfigFileContents()
		return {"username" : config[0], "password" : config[1]}

	def submitClass(self):
		return "auth-button"