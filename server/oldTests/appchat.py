import socket, select

if __name__ == "__main__":

	CONNECTION_LIST = []
	RECV_BUFFER = 4096	#4 kb
	PORT = 8888

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(("", PORT))
	server_socket.listen(10)	#up to 10 connections

	CONNECTION_LIST.append(server_socket)	#Not sure if neccessary

	print("Char server has started on port " + str(PORT))

	while True :
		#poll here
		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST, [], [])

		for sock in read_sockets :
			if sock == server_socket :	#If the connection is from ourselves
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print("Client (%s, %s) connected" % addr)

			else :
				try:
					data = sock.recv(RECV_BUFFER)
					if data :
						sock.send("Server received data".encode())
						print("Client says:" + data.decode())
				except:
					broadcast_data(sock, "Client is offline")
					print("Client is offline (printstatement)")
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue

	server_socket.close()