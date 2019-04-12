MOST SUCCESSFUL ROUTE SO FAR. 

GPIO tutorial: https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

Watching this video: https://www.youtube.com/watch?v=UIJKdCIEXUQ

## Plan
Use the flask framework in Python to produce an HTML page that can operate remote Pi GPIO pins using "Remote GPIO" in python.

## Dependency Commands
```
sudo pip install flask

sudo pip install flask_wtf
```

## Run Commands
Navigate to web-server/
```
sudo python3 app.py
```
or if that doesn't work:
```
export FLASK_APP=app.py

export FLASK_DEBUG=1

sudo flask run
```
sudo is required to run on port 80.

Use web browser to navigate to http://localhost or the local IP address of the device running the program.

## Raspberry Pi Setup
Run all dependency commands above.
Open config with ```sudo raspi-config``` and enable SSH (if desired).

### Optional Bonjour Support
Allows local network URL creation. You will no longer have to type in a local IP address to the browser, just use the local URL instead.
```
sudo apt-get update

sudo apt-get upgrade

sudo apt-get install avahi-daemon
```
If you'd like to change the local IP to something different than the standard rapsberrypi.local, follow this tutorial: https://www.howtogeek.com/167195/how-to-change-your-raspberry-pi-or-other-linux-devices-hostname/

