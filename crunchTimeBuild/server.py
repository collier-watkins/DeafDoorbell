import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

import select

import socket
import fcntl
import struct

import I2C_LCD_driver

from subprocess import check_output

host_name = ''  # Change this to your Raspberry Pi IP address
host_port = 80

#mylcd = I2C_LCD_driver.lcd()

lcdClearLine = "                "

myIP = check_output(['hostname', '--all-ip-addresses']).decode("utf-8").strip()


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def openPage(self, filename):
      with open(filename) as f:
        return f.read()

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    ### This runs when someone gets connected
    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = self.openPage("index.html")
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            #GPIO.setmode(GPIO.BCM)
            #GPIO.setwarnings(False)
            #GPIO.setup(18, GPIO.OUT)
            mylcd.lcd_display_string("*", 1, 15)


        #elif self.path=='/on':
            #GPIO.output(18, GPIO.HIGH)
            #status='LED is On'
        #    mylcd.lcd_display_string("*", 1, 15)


        #elif self.path=='/off':
            #GPIO.output(18, GPIO.LOW)
            #status='LED is Off'
        #    mylcd.lcd_display_string("o", 1, 15)
        elif self.path.startswith('/sub/'):
          #print(self.path)
          msg = self.path[5:].replace("_", " ")
          print("'" + msg + "'")
          mylcd.lcd_display_string(lcdClearLine, 2, 0)
          mylcd.lcd_display_string(msg, 2, 0)



        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    ############ Socket to client setup ############
	CONNECTION_LIST = []
	RECV_BUFFER = 4096	#4 kb
	PORT = 8888

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("", PORT))
	server_socket.listen(10)	#up to 10 connections

	CONNECTION_LIST.append(server_socket)	#Not sure if neccessary

    ####################################################################

    mylcd.lcd_clear()

    
    mylcd.lcd_display_string("Server", 1, 0)

    print("'" + myIP + "'")
    mylcd.lcd_display_string(myIP, 2, 0)
    

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()