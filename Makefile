# see https://github.com/Olical/Spark/blob/master/makefile
# rsync
FLASK_APP=coffee_flask.py
SRC_DIR=julian.coffee
NGROK_PATH=C:/Users/insan/Documents/julian.coffee/julian.coffee/coffee/external/ngrok.exe
NGROK_CMD=$(NGROK_PATH) http 5000
NGROK_MAC_CMD=ngrok http -subdomain coffee 5000

windows: # ngrok
	cd $(SRC_DIR) && set FLASK_APP=$(FLASK_APP) && flask run

mac:
	cd $(SRC_DIR) && export FLASK_APP=$(FLASK_APP) && python -m flask run

windows-ngrok: # configure the result of this in Twilio dashboard for callback
	start cmd.exe @cmd /k "$(NGROK_CMD)"

mac-ngrok:
	osascript -e 'tell application "Terminal" to do script "$(NGROK_MAC_CMD)"'

curl:	
	curl https://venmo.com/slycecoffee >> resources/venmo_mock.html
	python -m SimpleHTTPServer 8888
	open "localhost:8888"

mac-deps-fix:
	pip install --user --upgrade matplotlib

mac-deps: 
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python get-pip.py
	sudo pip install Flask

deps:
	@echo "Manual dependancies: (1) python (2) ngrok (for hosting remotely)"
	pip install --user flask
	pip install --user selenium
	pip install --user twilio

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

