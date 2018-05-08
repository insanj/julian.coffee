/* julian.coffee */
/* (c) 2018 Julian Weiss */

class CoffeeDiv {
	constructor(coffeeName, coffeeCount) {
		this.coffeeName = coffeeName;
		this.coffeeCount = coffeeCount;
	}

	generateDiv() {
		var divTemplate = "<h3>";
		for (var i = 0; i < this.coffeeCount; i++) {
			divTemplate += "☕️ ";
		}

		divTemplate += "<br/>";
		divTemplate += this.coffeeName;
		divTemplate += "</h3>";
		return divTemplate;
	}

	static createDivArrayFromVenmoJSON(jsonArray) {
		var venmoJSONDict = {};

		for (var i = 0; i < jsonArray.length; i++) {
			var venmoJSON = jsonArray[i];
			var venmoJSONName = venmoJSON["actor"]["username"];

			var existingCount = venmoJSONDict[venmoJSONName];
			if (existingCount) {
				venmoJSONDict[venmoJSONName] = existingCount + 1;
			} else {
				venmoJSONDict[venmoJSONName] = 1;
			}
		}

		var newlyBrewedObjects = [];
		$.each(venmoJSONDict, function(key, value) {
			var venmoObj = new CoffeeDiv(key, value);
			newlyBrewedObjects.push(venmoObj);
		});

		return newlyBrewedObjects;
	}
}

class CoffeeRenderer {
	constructor(parentDivID) {
		this.parentDivID = parentDivID;
	}

	renderDivs(divArray) {
		var parentDivIDHash = "#"+this.parentDivID;
		for (var i = 0; i  < divArray.length; i++) {
			$(parentDivIDHash).append(divArray[i]);
		}
	}
}

class CoffeeRuntime {
	constructor() {
		this.renderer = new CoffeeRenderer("patrons");
	}

	generateAndRenderDivs(sourceJSON) {
		var jsonArray = sourceJSON["data"];
		var coffeeDivs = CoffeeDiv.createDivArrayFromVenmoJSON(jsonArray);
		var generatedDivs = coffeeDivs.map(c => c.generateDiv());
		this.renderer.renderDivs(generatedDivs);
	}

	generateAndRenderDivsFromURL(coffeeURL) {
		var runtime = this;
		$.ajax({
			dataType: "json",
			url: coffeeURL,
			beforeSend: function(xhr) {
				xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
			},
			success: function (data) {
				runtime.generateAndRenderDivs(data);
			}
		});
	}

	brew(coffeeURL) {
		if (coffeeURL == null) {
			this.generateAndRenderDivsFromURL("venmo_mock.json");
		} else {
			this.generateAndRenderDivsFromURL(coffeeURL);
		}
	}
}

/* runtime */
$(document).ready(function() {
	var coffeeURL = null; // "https://venmo.com/api/v5/users/886771/feed";
	var coffeeRuntime = new CoffeeRuntime();
	coffeeRuntime.brew(coffeeURL);
});
