import socket, select

import I2C_LCD_driver

import fcntl
import struct

import sys
from thread import *

from time import *

import RPi.GPIO as GPIO


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

	mylcd.lcd_display_string("Server", 1, 0)
	mylcd.lcd_display_string(get_pi_ip_address('wlan0'), 2, 0)



	CONNECTION_LIST = []
	RECV_BUFFER = 4096	#4 kb
	PORT = 8888

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("", PORT))
	server_socket.listen(10)	#up to 10 connections

	CONNECTION_LIST.append(server_socket)	#Not sure if neccessary

	print("Chat server has started on port " + str(PORT))

	while True :
		#poll here
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST, [], [])

		for sock in read_sockets :
			if sock == server_socket :	#If the connection is from ourselves
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print("Client (%s, %s) connected" % addr)
				mylcd.lcd_display_string("%", 1, 15)


			else :
				try:
					data = sock.recv(RECV_BUFFER)
					if data :
						sock.send(("Server got: " + data.decode() ).encode())
						print("Client says:" + data.decode())
						mylcd.lcd_display_string(data.decode(), 0, 0)
				except:
					broadcast_data(sock, "Client is offline")
					print("Client is offline (printstatement)")
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue

	server_socket.close()