# see https://github.com/Olical/Spark/blob/master/makefile
# rsync
FLASK_APP=coffee_flask.py
SRC_DIR=julian.coffee
NGROK_PATH=C:/Users/insan/Documents/julian.coffee/julian.coffee/coffee/external/ngrok.exe
NGROK_CMD=$(NGROK_PATH) http 5000

windows: # ngrok
	cd $(SRC_DIR) && set FLASK_APP=$(FLASK_APP) && flask run

ngrok:
	start cmd.exe @cmd /k "$(NGROK_CMD)"

curl:	
	curl https://venmo.com/slycecoffee >> resources/venmo_mock.html
	python -m SimpleHTTPServer 8888
	open "localhost:8888"

deps:
	pip install flask
	pip install selenium
	pip install twilio

ship:
	apt-get install git-ftp
	git config git.ftp.xxxx.url ftpservice.server.com/root/dir/for/ftp
	git config git.ftp.xxxx.user myUsername
	git config git.ftp.xxxx.password myPassword
	git ftp pull
	git ftp show --scope xxxx
	git ftp log --scope xxxx

clean-windows:
	del /s /q *.pyc
	rmdir /s /q "finally/exports"

