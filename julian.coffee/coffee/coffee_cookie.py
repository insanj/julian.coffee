#!/usr/bin/python
import os
import json

class CoffeeCookie:
	safePath = None
	cookieFilename = None
	cookies = None

	def __init__(self, safePath, cookieFilename):
		self.safePath = safePath
		self.cookieFilename = cookieFilename
		self.cookies = self.loadCookies()

	def loadCookies(self):
		cookiePath = os.path.join(self.safePath, self.cookieFilename)
		cookieData = self.readCookieFile(cookiePath)
		print "cookieData = " + str(cookieData)
		return cookieData

	def readCookieFile(self, cookiePath):
		with open(cookiePath) as cookieFile:
			jsonCookie = cookieFile.read()
			return json.loads(jsonCookie)

	def biscottiFormat(self, validKeys=["name", "value", "path"]):
		formattedCookies = []
		for c in self.cookies:
			preformattedCookie = {}
			for key, value in c.iteritems():
				if key in validKeys:
					preformattedCookie[key] = value
			formattedCookies.append(preformattedCookie)
		return formattedCookies
