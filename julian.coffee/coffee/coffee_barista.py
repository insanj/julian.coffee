#!/usr/bin/python
from selenium import webdriver

class CoffeeBarista():
	baristaBrowser = None

	def __init__(self, browserPath):
		self.baristaBrowser = webdriver.Chrome(browserPath)

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

	def getWebpageHTMLBody(self, baristaURL):
		self.baristaBrowser.get(baristaURL)
		return self.getElementForSelector("html").get_attribute("innerHTML")