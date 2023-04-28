from random import randint
import threading
import socket


PORT = 3003
HOST = '172.28.80.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
nicknames = []
teste = {'r1': {'c1': 'client', 'c2': 'client2', 'c9': 'nre'}, 'r2': {'c3': 'client3', 'c4': 'client4'}, 'r3': {'c5': 'client5', 'c6': 'client6'}, 'r4': {'c19': 'client', 'c92': 'client2'}}


def change(cara, msg):
    for i in teste:
        for j in teste[i]:
            print(j)
    
change('c1', '_+_+_+_+_+_+_+_+_+_')
# obj_chat_rooms = {'r1': {}}

# def broadcast(message):
#     for client in clients:
#         client.send(message)

# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             broadcast(message)
#             print(obj_chat_rooms)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close
#             nickname = nicknames[index]
#             broadcast(f'{nickname} left the chat!'.encode('ascii'))
#             nicknames.remove[nickname]
#             break

# def receive():
#     indice = 1
#     while True:
#         client, address = server.accept()
#         print(f"Connected with {str(address)}")

#         client.send("NICK".encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
#         if(len(obj_chat_rooms[max(obj_chat_rooms.keys())]) <2):
#             obj_chat_rooms[max(obj_chat_rooms.keys())][f'client{indice}']= client
#         else:
#             obj_chat_rooms[f'r{indice}'] = {f'client{indice}': client}

#         indice+=1   
#         print(f"Nickname of the client is {nickname}!")
#         broadcast(f"{nickname} joined the chat".encode("ascii"))
#         client.send("Connected to the server".encode('ascii'))
#         print(len(clients))
#         print(obj_chat_rooms)

#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()



# server.bind((HOST, PORT))
# server.listen()
# print('Server is listening...')
# receive()

