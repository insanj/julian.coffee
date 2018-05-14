/* julian.coffee */
/* (c) 2018 Julian Weiss */

class CoffeeScraper {
	constructor(localPath, remoteURL) {
		if (localPath == null) {
			this.scraperURL = remoteURL;
		} else {
			this.scraperURL = localPath;
		}
	}

	roast(callback) {
		var scraper = this;
		var coffeeURL = scraper.scraperURL;
		scraper.getHTMLForURL(function(htmlResult) {
			var scrapedResult = scraper.scrapeHTMLForCoffeeObjects(htmlResult);
			callback(scrapedResult);
		});
	}

	getHTMLForURL(htmlCallback) {
		var htmlURL = this.scraperURL;
		var ajaxCallback = htmlCallback;
		$.ajax({
			dataType: "html",
			url: htmlURL,
		    timeout: 100000,
			beforeSend: function(xhr) {
				xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
			},
			success: function (data) {
				console.log("Got HTML for URL! " + data);
				ajaxCallback(data);
			},
			error: function (data) {
				console.log("Failed to get HTML for URL :(");
				ajaxCallback(null);
			}
		});
	}

	getHTMLForCORSProxyURL(htmlCallback) {
		var jsonURL = this.scraperURL;
		var ajaxCallback = htmlCallback;
		$.ajax({
			dataType: "json",
			url: jsonURL,
			success: function (data) {
				ajaxCallback(data["body"]);
			},
			error: function (data) {
				ajaxCallback(null);
			}
		});
	}

	scrapeHTMLForCoffeeObjects(scrapedHTML) {
		var parsedNameCounts = this.parseHTMLIntoNameCountDict(scrapedHTML);
		var newlyBrewedObjects = [];
		$.each(parsedNameCounts, function(key, value) {
			var venmoObj = new CoffeeObject(key, value);
			newlyBrewedObjects.push(venmoObj);
		});

		return newlyBrewedObjects;
	}

	parseHTMLIntoNameCountDict(parsableHTML) {
		var parsedHTML = $.parseHTML(parsableHTML);
		var parsableNodes = $(parsedHTML).find(".relative");

		var parser = this;
		var parsedNameCounts = {};
		$.each(parsableNodes, function(i, el) {
			var name = parser.parseVenmoNameFromHTMLNode(el);
			if (name != null) {
				var existingCount = parsedNameCounts[name];
				if (existingCount) {
					parsedNameCounts[name] = existingCount + 1;
				} else {
					parsedNameCounts[name] = 1;
				}
			}
		});

		return parsedNameCounts;
	}

	parseVenmoNameFromHTMLNode(htmlNode) {
		var links = $(htmlNode).find("a");
		if (links == null || links.length <= 0) {
			return null;
		} else {
			return links[0].getAttribute("title");
		}
	}
}