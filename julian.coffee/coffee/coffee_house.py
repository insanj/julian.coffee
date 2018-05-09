#!/usr/bin/python
from coffee_safe import *
from coffee_barista import *

class CoffeeHouse:
	webBrowser = None

	def __init__(self, browserPath):
		self.webBrowser = CoffeeBarista(browserPath)

	def auth(self):
		loginAuth = CoffeeSafe()
		loginAuthSite = loginAuth.authWebpage()
		loginAuthDict = loginAuth.authDict()
		loginAuthSubmit = loginAuth.submitClass()

		self.webBrowser.navigateToWebpage(loginAuthSite)

		for key, value in loginAuthDict.iteritems():
			self.webBrowser.sendValueForName(value, key);

		self.webBrowser.submitForClass(loginAuthSubmit)

	def beginCoffeeTime(self, venmoURL):
		self.auth()
		venmoWebpage = self.webBrowser.getWebpageHTMLBody(venmoURL)
		self.webBrowser.close()
		return venmoWebpage