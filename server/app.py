#install telnet packages?

import socket
import sys

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

conn, addr = s.accept()

print("Connected with " + str(addr[0]) + ":" + str(addr[1]))

data = conn.recv(1024 * 16*2)	#32kb of data
print(data.decode())
conn.sendall("Howdy")

print(data.decode())

conn.close()
s.close()
