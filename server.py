import socket
import config

# połączenie TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((config.HOST, config.PORT))

# jeśli więcej niż 5 połączeń czeka to odrzucamy nowe połączenia
server.listen(5)

# nie możemy jeszcze obsługiwać wielu połączeń na raz
while True:
    # metoda accept() zwraca adres klienta, który chce się połączyć
    # oraz socket, dzięki któremu możemy porozumiewać się z klientem
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(2*config.PACKAGE_SIZE).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} closed!")


