/* julian.coffee */
/* (c) 2018 Julian Weiss */

$(document).ready(function() {
	var coffeeURL = window.location.href + "coffeeTime";
	var coffeeScraper = new CoffeeScraper(null, coffeeURL);
	coffeeScraper.roast(function (coffeeObjects) {
		$("#loading").remove();
		var coffeeParentDivId = "patrons";
		var coffeeRenderer = new CoffeeRenderer(coffeeParentDivId);
		coffeeRenderer.brew(coffeeObjects);
	});
});
