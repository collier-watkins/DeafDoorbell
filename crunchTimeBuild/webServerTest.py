#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer


########## Rapsberry Pi and LCD Imports #############
import socket, select

import I2C_LCD_driver

import fcntl
import struct

import sys
from _thread import *

from time import *

import RPi.GPIO as GPIO
#####################################################

def get_pi_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
       s.fileno(),
       0x8915,  # SIOCGIFADDR
       struct.pack('256s', ifname[:15])
   )[20:24])



 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  def openPage(self, filename):
  	with open(filename) as f:
  		return f.read()

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = self.openPage("index.html")
        #message = "Howdy"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', 80)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()

##### LCD Code Here
mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_clear()

print("Starting...")
print("Current Local IP: " + get_pi_ip_address('wlan0'))

mylcd.lcd_display_string("Server", 1, 0)
mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)