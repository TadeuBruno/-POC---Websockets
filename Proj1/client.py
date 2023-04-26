import socket
PORT = 3031
HOST = '10.1.76.29'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
while True:

    chat_message = str(input("Type the message: "))
    socket.send(f"{chat_message}".encode('utf-8'))
    print(socket.recv(1024).decode('utf-8'))