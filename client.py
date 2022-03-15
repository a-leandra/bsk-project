import socket
import config

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((config.HOST, config.PORT))

done = False

while not done:
    send_msg = input("Message: ")
    client.send(send_msg.encode('utf-8'))
    msg = client.recv(2*config.PACKAGE_SIZE).decode('utf-8')
    if send_msg == 'quit' or msg == 'quit':
        done = True
        if msg == 'quit':
            print("Server is quiting...")
        else:
            print("Closing connection...")
    else:
        print(msg)

client.close()