import socket

import config

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((config.HOST, config.PORT))

message, address = server.recvfrom(config.PACKAGE_SIZE)
print(message.decode('utf-8'))
server.sendto("Hello Client!".encode('utf-8'), address)