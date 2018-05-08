/* julian.coffee */
/* (c) 2018 Julian Weiss */

class CoffeeObject {
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

	generateAndRenderDivs(coffeeObjects) {		
		var generatedDivs = coffeeObjects.map(c => c.generateDiv());
		this.renderDivs(generatedDivs);
	}

	brew(coffeeObjects) {
		this.generateAndRenderDivs(coffeeObjects);
	}
}
