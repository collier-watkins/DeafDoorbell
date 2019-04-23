import I2C_LCD_driver
import socket
import fcntl
import struct

import sys
from thread import *

from time import *

host = "www.google.com"
port = 80


def get_pi_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

mylcd = I2C_LCD_driver.lcd()



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


mylcd.lcd_display_string("IP:" + get_pi_ip_address('wlan0'), 2, 0)



####### Socket Setup ######################################

s = setupServer()

host_ip = socket.gethostbyname(host)

s.connect((host_ip, port))

print("Socket connected")

message = "GET / HTTP/1.1\r\n\r\n"

#Actually send message
try:
	s.sendall(message.encode())
except:
	print("Did not send message")
	sys.exit()

print("Message Sent")