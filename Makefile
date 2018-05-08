
all:	
	curl https://venmo.com/slycecoffee >> venmo_mock.html
	python -m SimpleHTTPServer 8888
	open "localhost:8888"