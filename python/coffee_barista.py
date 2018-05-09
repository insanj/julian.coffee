#!/usr/bin/python
from onepassword import Keychain
from selenium import webdriver

# coordinator; logins into venmo using 1pass and downloads profile page
class Coffeehouse():
	venmoURL = None

	def __init__(self, venmoURL):
		self.venmoURL = venmoURL

	def getCoffeeTime():

class CoffeeBarista():
	baristaURL = None
	baristaDriver = None

	def __init__(self, baristaURL):
		self.baristaURL = baristaURL
		self.baristaDriver = webdriver.Chrome()

	def navigateToWebpage():
		self.baristaDriver.get(self.baristaURL)

	def focusCurrentWebpage():
		self.baristaDriver

	def sendValueForKey(value, key):
		element = self.baristaDriver.find_element_by_class_name(key) # js-username-field
		element.send_keys(value)

	def submitForSelector(selector):
		element = self.baristaDriver.find_element_by_css_selector(selector) # button.submit
		element.submit()

# gets the profile site
class CoffeeProfileBarista(CoffeeBarista):
	def downloadHTMLFromProfileWebpage():

# gets the username, pass to login
class CoffeeOnePasswordBarista(CoffeeBarista):

	my_keychain = Keychain(path="~/Dropbox/1Password.agilekeychain")
	my_keychain.unlock("my-master-password")
	my_keychain.item("An item's name").password

# submits the login information
class CoffeeLoginBarista(CoffeeBarista):
	def inputUsernameIntoWebpage():
	def inputPasswordIntoWebpage():
	def submitLoginFormForWebpage():
