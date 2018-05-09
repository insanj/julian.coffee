#!/usr/bin/python
from selenium import webdriver

class CoffeeBarista():
	baristaBrowser = None

	def __init__(self, browserPath):
		self.baristaBrowser = webdriver.Chrome(browserPath)

	def navigateToWebpage(self, baristaURL):
		self.baristaBrowser.get(baristaURL)

	def sendValueForKey(self, value, key):
		element = self.baristaBrowser.find_element_by_class_name(key)
		element.send_keys(value)

	def sendValueForName(self, value, name):
		element = self.baristaBrowser.find_element_by_name(name)
		element.send_keys(value)

	def submitForClass(self, className):
		element = self.baristaBrowser.find_element_by_class_name(className)
		element.submit()

	def submitForSelector(self, selector):
		element = self.baristaBrowser.find_element_by_css_selector(selector)
		element.submit()

	def closeWebpage(self):
		self.baristaBrowser.quit()

	def getWebpageHTMLBody(self, baristaURL):
		self.baristaBrowser.get(baristaURL)
		print self.baristaBrowser.find_element_by_xpath("/html/body").text