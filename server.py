import socket
import os
from sys import argv

# Function takes the CLI argument and returns the absolute path
def getPath():
	if len(argv) > 1 and os.path.exists(argv[1]):
		return open(argv[1], 'rb')

# Basic Configuration for socket, binds at port 8080
def socketConf():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',8080))
	sock.listen(1)
	return sock

# Two states: Passing the filename and then passing file content
def stateSend(connectionSocket, serveFile):
		for line in serveFile:
			connectionSocket.send(line)
		connectionSocket.close()

'''
Get the file and create socket
Wait for connections
Send file content
'''
currFile = getPath()
sock = socketConf()

while True:
	conn, address = sock.accept()
	stateSend(conn,currFile)
	conn.close()
	break
