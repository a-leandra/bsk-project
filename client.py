import socket

import config

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello Server!".encode('utf-8'), (config.HOST, config.PORT))
print(client.recvfrom(config.PACKAGE_SIZE)[0].decode('utf-8'))