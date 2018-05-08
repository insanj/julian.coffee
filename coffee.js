/* julian.coffee */
/* (c) 2018 Julian Weiss */

$(document).ready(function() {
	var coffeeURL = "http://cors-proxy.htmldriven.com/?url=https://venmo.com/slycecoffee";
	var coffeeScraper = new CoffeeScraper(coffeeURL);
	coffeeScraper.roast(function (coffeeObjects) {
		var coffeeParentDivId = "patrons";
		var coffeeRenderer = new CoffeeRenderer(coffeeParentDivId);
		coffeeRenderer.brew(coffeeObjects);
	});
});
