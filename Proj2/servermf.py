from http import client
from pydoc import cli
from random import randint
import threading
import socket


PORT = 3003
HOST = '10.1.76.33'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
nicknames = []

obj_chat_rooms = {'r1': {}}

def get_subindice(client):
    for i in obj_chat_rooms.keys():
        for j in obj_chat_rooms[i]:
            if obj_chat_rooms[i][j] ==  client:
                for y in obj_chat_rooms[i]:
                    if(obj_chat_rooms[i][y] == client):
                        return y


def broadcast(message, clientParm):
    for i in obj_chat_rooms:
        if clientParm in obj_chat_rooms[i]:
            for z in obj_chat_rooms[i]:
                obj_chat_rooms[i][z].send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, get_subindice(client))
            print(f'{obj_chat_rooms}')
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'), get_subindice(client))
            nicknames.remove[nickname]
            break

def receive():
    indice = 1
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        if(len(obj_chat_rooms[max(obj_chat_rooms.keys())]) <2):
            obj_chat_rooms[max(obj_chat_rooms.keys())][f'client{indice}']= client
        else:
            obj_chat_rooms[f'r{indice}'] = {f'client{indice}': client}

        indice+=1   
        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat".encode("ascii"), get_subindice(client))
        client.send("Connected to the server".encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()



server.bind((HOST, PORT))
server.listen()
print('Server is listening...')
receive()

