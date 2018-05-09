#!/usr/bin/python
from selenium import webdriver

class CoffeeBarista():
	baristaBrowser = None

	def __init__(self, baristaBrowser=webdriver.Chrome()):
		self.baristaBrowser = baristaBrowser

	def navigateToWebpage(baristaURL):
		self.baristaBrowser.get(baristaURL)

	def sendValueForKey(value, key):
		element = self.baristaBrowser.find_element_by_class_name(key) # js-username-field
		element.send_keys(value)

	def submitForSelector(selector):
		element = self.baristaBrowser.find_element_by_css_selector(selector) # button.submit
		element.submit()

	def closeWebpage():
		self.baristaBrowser.quit()

	def findAllElementsForClass(className):
		return self.baristaBrowser.find_element_by_name(className)