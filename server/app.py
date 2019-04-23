#install telnet packages?

import socket
import sys

from _thread import *

host = ''
port = 8888


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
try:
	s.bind((host, port))
except socket.error:
	print("Binding failed")
	sys.exit()

print("Socket bounded")

s.listen(10)	#up to 10 people can be queued for connection at a time

print("Socket is ready to listen")

def clientThread(conn):
	conn.send("Welcome to the server. Type something and hit enter.\n".encode())
	while True :
		data = conn.recv(1024 * 16*2)
		if not data :
			break
		print("Client data received: " + data.decode())
		reply = input("Reply here: ")
		conn.sendall(reply)

	conn.close()




while True:
	conn, addr = s.accept()
	print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
	start_new_thread(clientThread, (conn,))

s.close()