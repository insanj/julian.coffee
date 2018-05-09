
all:	
	curl https://venmo.com/slycecoffee >> resources/venmo_mock.html
	python -m SimpleHTTPServer 8888
	open "localhost:8888"

deps:
	pip install 1pass
	pip install flask
	pip install selenium