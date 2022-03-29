import socket
import threading

import config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config.HOST, config.PORT))

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        index = clients.index(client)
        try:
            message = client.recv(config.PACKAGE_SIZE)
            print(f"{nicknames[index]} says {message}")
            broadcast(message)
        except:
            clients.remove(client)
            client.close
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(config.PACKAGE_SIZE)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening..")
receive()
