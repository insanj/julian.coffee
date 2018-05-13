#!/usr/bin/python
from coffee_safe import *
from coffee_barista import *
import time

class CoffeeHouse:
	browserPath = None
	safePath = None

	def __init__(self, browserPath, safePath):
		self.browserPath = browserPath
		self.safePath = safePath

	def beginCoffeeTime(self, venmoURL):
		webBrowser = CoffeeBarista(self.browserPath)
		loginAuth = CoffeeSafe(self.safePath)

		waitTime = 2

		webBrowser.navigateToWebpage(loginAuth.loginSite)
		# webBrowser.setWebpageCookie(loginAuth.cookie)
		webBrowser.setValueForSelector(loginAuth.loginUsername, loginAuth.loginUsernameSelector)
		webBrowser.setValueForSelector(loginAuth.loginPassword, loginAuth.loginPasswordSelector)
		webBrowser.submitForSelector(loginAuth.loginSubmitSelector)
		# self.webBrowser.waitForSelector(loginAuth.loginSMSSelector)
		time.sleep(waitTime)

		webBrowser.submitForSelector(loginAuth.loginSMSSelector)
		time.sleep(waitTime)

		mfaNumber = loginAuth.readVerificationNumber()
		webBrowser.setValueForSelector(mfaNumber, loginAuth.loginMFAFormSelector)
		webBrowser.submitForSelector(loginAuth.loginSubmitSelector)
		time.sleep(waitTime)

		webBrowser.submitForSelector(loginAuth.loginSubmitSelector)
		webBrowser.navigateToWebpage(venmoURL)

		time.sleep(waitTime)

		# moreButton ////

		venmoWebpage = webBrowser.getWebpageHTMLBody()
		webBrowser.closeWebpage()
		return venmoWebpage

	def rememberVerificationNumber(self, verificationNumber):
		safe = CoffeeSafe(self.safePath)
		safe.writeVerificationNumber(verificationNumber)
		return True