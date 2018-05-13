#!/usr/bin/python
from selenium import webdriver
from coffee_cookie import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class CoffeeBarista():
	baristaBrowser = None

	def __init__(self, browserPath):
		opts = Options()
		opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
		self.baristaBrowser = webdriver.Chrome(browserPath, chrome_options=opts)

	def navigateToWebpage(self, baristaURL):
		self.baristaBrowser.get(baristaURL)

	def getElementForSelector(self, selector):
		return self.baristaBrowser.find_element_by_css_selector(selector)

	def setValueForSelector(self, value, selector):
		element = self.getElementForSelector(selector)
		element.send_keys(value)

	def submitForSelector(self, selector):
		element = self.getElementForSelector(selector)
		element.submit()

	def closeWebpage(self):
		self.baristaBrowser.quit()

	def getWebpageHTMLBody(self):
		return self.getElementForSelector("html").get_attribute("innerHTML")
 
	def setWebpageCookie(self, cookie):
		print "before setting, here ar ecookies " + str(self.baristaBrowser.get_cookies())
		if cookie is None:
			print "setWebpageCookie invalid because null cookie"
		else:
			biscotti = cookie.biscottiFormat()
			print "Yay! biscotti " + str(biscotti)
			for b in biscotti:
				print "Yay! b " + str(b)
				self.baristaBrowser.add_cookie(b)

	def waitForSelector(self, selector, timeout=5):
		element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
		WebDriverWait(self.baristaBrowser, timeout).until(element_present)
		return True