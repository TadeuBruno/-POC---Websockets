import socket

# host = socket.gethostname(socket.gethostname())
PORT = 3031
HOST = '10.1.76.29'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


server.listen(2)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    while True:
        message = communication_socket.recv(1024).decode('utf-8')
        print(f"Message from client is: {message}")
        chat_message = str(input("Type the message: "))
        communication_socket.send(f"{chat_message}".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")