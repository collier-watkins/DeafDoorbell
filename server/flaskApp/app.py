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

message = ""
JoysRoom = False
UpstairsBathroom = False



#def get_pi_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,  # SIOCGIFADDR
#        struct.pack('256s', ifname[:15])
#   )[20:24])

#mylcd = I2C_LCD_driver.lcd()

#mylcd.lcd_clear()

print("Starting...")
#print("Current Local IP: " + get_pi_ip_address('wlan0'))

#mylcd.lcd_display_string("Server", 1, 0)
#mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)



#Home Page
@app.route("/", methods=['GET', 'POST'])	#Related to website locations
def homePage():	#Returns data for the main home page, should be HTML data

	#mylcd.lcd_display_string("*", 1, 15)


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


		 

		 #####################



	return render_template('home.html', title='Blog Posts', form=form)



@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(arg1):
    print('received args: ' + arg1)

#About Page
@app.route("/about")	
def aboutPage():
	return "<h1>About Page</h1>"










if __name__ == '__main__':
	#Run Flask Application
	socketio.run(app, debug=True, host='0.0.0.0', port=80)
