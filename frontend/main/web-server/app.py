from flask import Flask
app = Flask(__name__)

#Home Page
@app.route("/")	#Related to website locations
def hello():	#Returns data for the main home page, should be HTML data
	return "Hello World!"