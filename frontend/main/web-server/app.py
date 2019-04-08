from flask import Flask
app = Flask(__name__)

#Home Page
@app.route("/")	#Related to website locations
def homePage():	#Returns data for the main home page, should be HTML data
	return "<h1>Home Page</h1>"


#Home Page
@app.route("/about")	
def aboutPage():
	return "<h1>About Page</h1>"








#Run Flask Application
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)