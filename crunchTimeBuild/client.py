import socket, select

import I2C_LCD_driver

import fcntl
import struct

import sys
from thread import *

from time import *

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#Button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	#Occupancy Signal
GPIO.setup(18, GPIO.OUT)	#Attention LED




def get_pi_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
       s.fileno(),
       0x8915,  # SIOCGIFADDR
       struct.pack('256s', ifname[:15])
   )[20:24])

if __name__ == "__main__":

	mylcd = I2C_LCD_driver.lcd()

	mylcd.lcd_clear()

	print("Starting...")
	print("Current Local IP: " + get_pi_ip_address('wlan0'))
'''
	mylcd.lcd_display_string("Tap btn to start", 1, 0)
	mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)

	while True :
		if GPIO.input(4) == False :
			mylcd.lcd_clear()
			#mylcd.backlight(0)
			break
'''
	CONNECTION_LIST = []
	RECV_BUFFER = 4096	#4 kb
	PORT = 8888

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("", PORT))
	server_socket.listen(10)	#up to 10 connections

	CONNECTION_LIST.append(server_socket)	#Not sure if neccessary

	print("Chat server has started on port " + str(PORT))

	mylcd.lcd_display_string("Ready for server", 1, 0)
	mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)

	while True :
		#poll here
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST, [], [])

		for sock in read_sockets :
			if sock == server_socket :	#If the connection is from ourselves
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print("Server (%s, %s) connected" % addr)
				mylcd.lcd_clear()
				mylcd.lcd_display_string("Server conn.", 1, 0)
				if GPIO.input(4) == False :
					mylcd.lcd_clear()
					mylcd.backlight(0)

			else :
				try:
					data = sock.recv(RECV_BUFFER)
					if data :
						#Save data.deac
						mylcd.lcd_clear()
						response = "/occ/"
						sock.send(response.encode())
						print("Server Pi says:" + data.decode())
						mylcd.lcd_display_string(data.decode(), 1, 0)

						#Message Handling Sequence
						mylcd.backlight(1)
						lightOn = True
						while True :
							sleep(0.2)
							if lightOn :
								GPIO.output(18,1)
								lightOn = not lightOn
							else :
								GPIO.output(18,0)
								lightOn = not lightOn
							if GPIO.input(4) == False :
								mylcd.lcd_clear()
								mylcd.backlight(0)
								GPIO.output(18,0)
								break


				except:
					#broadcast_data(sock, "Server is offline")
					print("Server is offline")
					mylcd.backlight(0)
					mylcd.lcd_clear()
					mylcd.lcd_display_string("Server offline", 1, 0)
					#mylcd.lcd_display_string("Please Reboot", 2, 0)
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue

	server_socket.close()