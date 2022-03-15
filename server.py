import socket
import config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config.HOST, config.PORT))

server.listen()

client, addr = server.accept()

done = False
send_msg = ''

while not done:
    msg = client.recv(2*config.PACKAGE_SIZE).decode('utf-8')
    if send_msg == 'quit' or msg == 'quit':
        done = True
        if msg == 'quit':
            print("Client is quiting...")
        else:
            print("Closing connection...")
    else:
        print(msg)
        send_msg = input("Message: ")
        client.send(send_msg.encode('utf-8'))

client.close()
server.close()