#!/usr/bin/python
from coffee_safe import *
from coffee_barista import *

class CoffeeHouse:
	webBrowser = None
	safePath = None

	def __init__(self, browserPath, safePath):
		self.webBrowser = CoffeeBarista(browserPath)
		self.safePath = safePath

	def beginCoffeeTime(self, venmoURL):
		loginAuth = CoffeeSafe(self.safePath)

		self.webBrowser.navigateToWebpage(loginAuth.loginSite)
		self.webBrowser.setWebpageCookie(loginAuth.cookie)
		self.webBrowser.setValueForSelector(loginAuth.loginUsername, loginAuth.loginUsernameSelector)
		self.webBrowser.setValueForSelector(loginAuth.loginPassword, loginAuth.loginPasswordSelector)
		self.webBrowser.submitForSelector(loginAuth.loginSubmitSelector)

		#venmoWebpage = self.webBrowser.getWebpageHTMLBody(venmoURL)
		#self.webBrowser.closeWebpage()

		#return venmoWebpage
		return "Hello"