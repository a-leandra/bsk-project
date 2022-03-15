import socket
import config

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((config.HOST, config.PORT))

socket.send("Hello! I'm sending my message to you!".encode('utf-8'))
print(socket.recv(2*config.PACKAGE_SIZE).decode('utf-8'))
