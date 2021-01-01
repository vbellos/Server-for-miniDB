import socket

if __name__ == "__main__":
	ip = '127.0.0.1'
	port = 3555
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip,port))
	
	string = input("Enter String:")
	sock.send(bytes(string,"utf-8"))
	buffer = sock.recv(1024)
	buffer = buffer.decode("utf-8")
	print(f"Server: {buffer}")
