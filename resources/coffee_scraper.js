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
		scraper.getHTMLForCORSProxyURL(function(htmlResult) {
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
			beforeSend: function(xhr) {
				xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
			},
			success: function (data) {
				ajaxCallback(data);
			},
			error: function (data) {
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
		var parsableNodes = $(parsedHTML).find(".single-payment");

		var parser = this;
		var parsedNameCounts = {};
		$.each(parsableNodes, function(i, el) {
			var name = parser.parseVenmoNameFromHTMLNode(el);
			var existingCount = parsedNameCounts[name];
			if (existingCount) {
				parsedNameCounts[name] = existingCount + 1;
			} else {
				parsedNameCounts[name] = 1;
			}
		});

		return parsedNameCounts;
	}

	parseVenmoNameFromHTMLNode(htmlNode) {
		return $(htmlNode).find(".paymentpage-subline").find("a")[0].text;
	}
}

/* loop through HTML DOM and isolate `single-payment content-wrap`, each element has structure:
<div class="single-payment content-wrap" onclick="parent.location='/story/5ae880295a877f6e38bc2648'">
	<div class="paymentpage-payment-container group">
		<div class="paymentpage-avatars float_left">
			<img src="https://s3.amazonaws.com/venmo/no-image.gif" class="to_user float_left">
			<img src="https://venmopics.appspot.com/u/v1/m/81a21320-00dc-48da-8925-ee4482b8f3e0" class="from_user">
		</div>

		<div class="paymentpage-textbox m_fifteen_l float_left">
			<div class="paymentpage-subline">
				<a href="/aturkelson">Adam Turkelson</a> paid

				
					<a href="/slycecoffee">Nicole Harris</a>
				

			</div>
			<div class="paymentpage-text m_five_t">☕</div>
			<div class="paymentpage-datetime m_five_t">
			  <div class="date"> on May  1, 2018 at 02:56PM - Comments (0)</div>
			</div>
			<div class="align_right" style="height:25px;z-index:10;">
				<div class="fb-like fb_iframe_widget" data-href="https://venmo.com/story/5ae880295a877f6e38bc2648" data-send="false" data-layout="button_count" data-width="450" data-show-faces="false" fb-xfbml-state="rendered" fb-iframe-plugin-query="app_id=180347063770&amp;container_width=465&amp;href=https%3A%2F%2Fvenmo.com%2Fstory%2F5ae880295a877f6e38bc2648&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;send=false&amp;show_faces=false&amp;width=450"><span style="vertical-align: bottom; width: 61px; height: 20px;"><iframe name="f130a4112ae7ab4" width="450px" height="1000px" frameborder="0" allowtransparency="true" allowfullscreen="true" scrolling="no" allow="encrypted-media" title="fb:like Facebook Social Plugin" src="https://www.facebook.com/v2.1/plugins/like.php?app_id=180347063770&amp;channel=https%3A%2F%2Fstaticxx.facebook.com%2Fconnect%2Fxd_arbiter%2Fr%2F2VRzCA39w_9.js%3Fversion%3D42%23cb%3Df146988f7ea91b8%26domain%3Dvenmo.com%26origin%3Dhttps%253A%252F%252Fvenmo.com%252Ff1a86a1595bba08%26relation%3Dparent.parent&amp;container_width=465&amp;href=https%3A%2F%2Fvenmo.com%2Fstory%2F5ae880295a877f6e38bc2648&amp;layout=button_count&amp;locale=en_US&amp;sdk=joey&amp;send=false&amp;show_faces=false&amp;width=450" style="border: none; visibility: visible; width: 61px; height: 20px;" class=""></iframe></span></div>
			</div>
		</div>
	</div> <!-- end payment-container-->
</div>
*/
