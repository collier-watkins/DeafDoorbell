import I2C_LCD_driver
import socket
import fcntl
import struct

import sys
from thread import *

from time import *

import RPi.GPIO as GPIO


#autorunning this script using the file /home/pi/.bashrc


host = "10.230.142.162"
port = 8888

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#Button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	#Occupancy Signal
GPIO.setup(18, GPIO.OUT)	#Attention LED



#CLIENT NEEDS

# GPIO things:
	# LCD Screen
		# VCC and Ground on board
		# SDA on GPIO 2
		# SCL on GPIO 3
	# Motion Sensor
	# LED for attention
	# Button for acknowledgement




def get_pi_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()

def setupServer():
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		print("Socket s created.")
	except socket.error as msg :
		print(msg)
		sys.exit()
	return s



###### LCD Setup #############
print("Starting...")
print("Current Local IP: " + get_pi_ip_address('wlan0'))



####### Socket Setup ######################################

s = setupServer()

#host_ip = socket.gethostbyname(host)

s.connect((host, port))

print("Socket connected")

mylcd.lcd_display_string("Tap btn to start", 1, 0)
mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)

while True :
	if GPIO.input(4) == False :
		mylcd.lcd_clear()
		break

while True: 

	rep = 1
	message = "message #" + str(rep)
	

	# GET MOTION SENSOR AND BUTTON STATUS INFO HERE
	# PUT IN A STRING
	

	sleep(0.2)

	#Below sends message string
	try:
		s.sendall(message.encode())
	except:
		print("Did not send message")
		sys.exit()

	print(message)

	#This is what the server sends back. Will contain the message the LCD screen should show
	reply = s.recv(4096)	#4096 is the size of the memory received from the socket

	print(reply.decode())

	#Button pressed
	if GPIO.input(4) == False :
		print("Button Pressed")
		mylcd.lcd_display_string("Btn Pressed", 1, 1)

	#Room occupied
	if GPIO.input(17) == True :
		print("Occupied")
		mylcd.lcd_display_string("*", 1, 15)
		#Attention LED testing
		GPIO.output(18,1)
	else :
		mylcd.lcd_display_string(" ", 1, 15)
		#Attention LED testing
		GPIO.output(18,0)

	rep += 1





s.close() #Closing socket connection, remove later
