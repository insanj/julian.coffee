#!/usr/bin/python
from coffee_safe import *
from coffee_barista import *

class CoffeeHouse:
	webBrowser = None

	def auth(self):
		loginAuth = CoffeeSafe()
		loginAuthSite = loginAuth.authWebpage()
		loginAuthDict = loginAuth.authDict()
		loginAuthSubmitSel = loginAuth.submitSelector()

		self.webBrowser.navigateToWebpage(loginAuthSite)

		for key, value in loginAuthDict.iteritems():
			self.webBrowser.sendValueForKey(value, key);

		self.webBrowser.submitForSelector(loginAuthSubmitSel)

	def download(self, downloadURL):
		self.webBrowser.navigateToWebpage(downloadURL)

		className = ""

		parsedElements = []
		for e in self.webBrowser.findAllElementsForClass(className):
			parsedElements.append(e.text)
		return parsedElements

	def beginCoffeeTime(self, venmoURL):
		self.webBrowser = CoffeeBarista()
		self.auth()
		venmoWebpage = self.download(venmoURL)
		self.webBrowser.close()
		return venmoWebpage
