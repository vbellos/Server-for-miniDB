import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 3555

server_address = (ip,port)
print(f"starting up on {ip} port: {port}")
sock.bind(server_address)

sock.listen(5)

while True:
	try:
		try:
	
			print (sys.stderr, "waiting for connection")
			client, address = sock.accept()
			print(f"Connection Established - {address[0]}:{address[1]}")
	#Receive
			string = client.recv(1024)
			string = string.decode("utf-8")
			string = "123+"+string
	#Send		
			client.send(bytes(string, "utf-8"))
	
			client.close()
		except KeyboardInterrupt:
			sock.close()
			print("KeyboardInterrupt")
			raise
	
	except(KeyboardInterrupt,SystemExit):
		print("Programm Stopped manually")
		raise

