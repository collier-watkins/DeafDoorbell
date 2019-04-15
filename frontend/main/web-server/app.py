from flask import Flask, render_template, url_for, flash, request
from forms import MessageForm
from wtforms.widgets import html_params, HTMLString


app = Flask(__name__)

app.config['SECRET_KEY'] = '3985723043u208uj23022039rue'






#Home Page
@app.route("/", methods=['GET', 'POST'])	#Related to website locations
def homePage():	#Returns data for the main home page, should be HTML data
	form = MessageForm()
	if form.validate_on_submit():
		#THIS IS WHAT HAPPENS WHEN THE SUBMIT BUTTON IS PRESSED
		 message = request.form.get("LCDMessage")
		 device1 = request.form.get("Joy\'s Room") != None
		 device2 = "Upstairs Bathroom" in request.form
		 app.logger.warning('Submit happened!')
		 app.logger.warning(message)
		 app.logger.warning(device1)
		 app.logger.warning(device2)


	return render_template('home.html', title='Blog Posts', form=form)


#About Page
@app.route("/about")	
def aboutPage():
	return "<h1>About Page</h1>"









#Run Flask Application
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)