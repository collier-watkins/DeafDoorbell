import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

import select

import sys

import socket
import fcntl
import struct

import I2C_LCD_driver

from subprocess import check_output

host_name = ''
host_port = 80

lcdClearLine = "                "

myIP = check_output(['hostname', '--all-ip-addresses']).decode("utf-8").strip()


############ Socket to client setup ############

def setupSocket():
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		print("Socket created.")
	except socket.error as msg :
		print(msg)
		sys.exit()
	return s

socks = []

####################################################################





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
		html = self.openPage("indexTEST.html")
		temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
		self.do_HEAD()
		status = ''
		if self.path=='/':
			mylcd.lcd_display_string("*", 1, 15)
			print("root hit")

		elif '/msg/' in self.path :
			arr = self.path.split("/")
			msg = arr[-1].replace("_", " ")
			joyChecked = '/joyCheck/' in self.path
			upstairsChecked = '/upstairsCheck/' in self.path
			mylcd.lcd_display_string(lcdClearLine, 1, 0)
			mylcd.lcd_display_string(lcdClearLine, 2, 0)
			if joyChecked :
				#mylcd.lcd_display_string("joy", 1, 0)
				print("joyChecked")
				try:
					socks[0].sendall(msg.encode())
					reply = socks[0].recv(4096)
					print("socks[0] reply: " + reply.decode())
					mylcd.lcd_display_string("0:" + reply.decode(), 1, 0)
				except:
					print("msg to socks[0] failed")
			if upstairsChecked :
				#mylcd.lcd_display_string("up", 1, 4)
				print("upstairsChecked")
				try:
					socks[1].sendall(msg.encode())
					reply = socks[1].recv(4096)
					print("socks[1] reply: " + reply.decode())
					mylcd.lcd_display_string("1:" + reply.decode(), 2, 0)
				except:
					print("msg to socks[1] failed")
			#mylcd.lcd_display_string(msg, 2, 0)
			print(msg)

		elif '/occCheck/' in self.path :


		elif self.path=='/flavicon.ico':
			print("flavicon.ico")

		else :
			print("Exeption: Bad URL")
			#mylcd.lcd_display_string(lcdClearLine, 2, 0)
			#mylcd.lcd_display_string("Exp: Bad URL", 2, 0)


		self.wfile.write(html.format(temp[5:], status).encode("utf-8"))


if __name__ == '__main__':
	## HTTP Setup
	http_server = HTTPServer((host_name, host_port), MyServer)
	print("Server Starts - %s:%s" % (host_name, host_port))

	### LCD Setup
	mylcd = I2C_LCD_driver.lcd()
	mylcd.lcd_clear()

	mylcd.lcd_display_string("Server", 1, 0)

	print("'" + myIP + "'")
	mylcd.lcd_display_string(myIP, 2, 0)



	##Socket Setup
	for arg in sys.argv[1:] :
		socks.append(setupSocket())
	i = 1
	for s in socks :
		s.connect((sys.argv[i], 8888))
		i += 1


	## Run HTTP Server
	try:
		http_server.serve_forever()
	except KeyboardInterrupt:
		#Actions for keyboard interrupt
		http_server.server_close()
		for s in socks :
			s.close()