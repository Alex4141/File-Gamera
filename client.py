import socket
import os

# Basic Configuration for socket, looks at port 8080
def socketConf():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setblocking(1)
	sock.connect(('',8080))
	return sock

# Creates a directory for file transfers
def getDirectory():
	relativePath = os.path.join(os.getcwd(),'forTransfers')
	if not os.path.isdir(relativePath):
		os.mkdir('forTransfers')
	return relativePath

# Creates a file
def createFile(currentSocket):
	currentDirectory = getDirectory()
	filename = currentDirectory + '/' +  currentSocket.recv(1024)
	newFile = open(filename, 'a')
	appendData(currentSocket, newFile)

# Get 1024 bytes at a time and append it to the file
def appendData(currentSocket, transferFile):
	while True:
		chunk = currentSocket.recv(1024)
		if chunk:
			transferFile.write(chunk)
			transferFile.flush()
		else:
			transferFile.close()
			print("FTP Complete")
			break

sock = socketConf()
createFile(sock)
sock.close()
