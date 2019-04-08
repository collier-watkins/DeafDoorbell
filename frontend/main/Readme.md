MOST SUCCESSFUL ROUTE SO FAR. 

GPIO tutorial: https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/

Follow this video: https://www.youtube.com/watch?v=MwZwr5Tvyxo
Time: 14:41

## Plan
Use the flask framework in Python to produce an HTML page that can operate remote Pi GPIO pins using "Remote GPIO" in python.

## Dependency Commands
```
pip install flask

export FLASK_APP=app.py

export FLASK_DEBUG=1
```

## Run Commands
Navigate to web-server/
```
sudo flask run
```
or:
```
sudo python app.py
```
sudo is required to run on port 80