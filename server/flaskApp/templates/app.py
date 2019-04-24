from flask import Flask, render_template, url_for, flash, request
from forms import MessageForm
from wtforms.widgets import html_params, HTMLString

from flask_socketio import SocketIO

#import subprocess


app = Flask(__name__)

app.config['SECRET_KEY'] = '3985723043u208uj23022039rue'
socketio = SocketIO(app)
 
client1IP = "192.168.0.16"


#Home Page
@app.route("/", methods=['GET', 'POST'])	#Related to website locations
def homePage():	#Returns data for the main home page, should be HTML data
	form = MessageForm()

	JoysRoom = False
	UpstairsBathroom = False

	if request.method == "POST":
		 locations = request.form.getlist('location')
		 if u'Upstairs Bathroom' in locations : UpstairsBathroom = True
		 if u'Joys Room' in locations : JoysRoom = True



	if form.validate_on_submit():
		#THIS IS WHAT HAPPENS WHEN THE SUBMIT BUTTON IS PRESSED
		 message = request.form.get("LCDMessage")

		 app.logger.warning('Submit happened!')
		 app.logger.warning(message)
		 app.logger.warning("Joy\'s Room: " + str(JoysRoom)) 
		 app.logger.warning("Upstairs Bathroom: " + str(UpstairsBathroom)) 

		 ######Send message to LCD and do GPIO stuff here #########


		 #subprocess.run()


		 #####################



	return render_template('home.html', title='Blog Posts', form=form)




def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')




@socketio.on('submitHit')
def handle_submit_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)





#About Page
@app.route("/about")	
def aboutPage():
	return "<h1>About Page</h1>"










if __name__ == '__main__':
	#Run Flask Application
	socketio.run(app, debug=True, host='0.0.0.0', port=80)
