from flask import Flask
app = Flask(__name__)

#Home Page
@app.route("/")	#Related to website locations
def hello():	#Returns data for the main home page, should be HTML data
	return "<h1>Home Page</h1>"





#Run Flask Application
if __name__ == '__main__':
	app.run(debug=True)