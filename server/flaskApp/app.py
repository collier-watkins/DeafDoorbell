from flask import Flask, render_template, url_for, flash, request
from forms import MessageForm
from wtforms.widgets import html_params, HTMLString

import socket
import fcntl
import struct 
import sys

from flask_socketio import SocketIO

import I2C_LCD_driver

#import subprocess


app = Flask(__name__)

app.config['SECRET_KEY'] = '3985723043u208uj23022039rue'
socketio = SocketIO(app)
 
client1IP = "192.168.0.16"


def get_pi_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()



mylcd.lcd_display_string("Server running @", 1, 0)
mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)



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
