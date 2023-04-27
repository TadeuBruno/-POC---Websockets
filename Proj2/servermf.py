from random import randint
import threading
import socket
import pymongo


cluster = pymongo.MongoClient("mongodb+srv://bruno:1234@cluster0.j7eftti.mongodb.net/?retryWrites=true&w=majority")
banco = cluster['Ports']
col = banco['available_ports']

def get_port():
    while True:
        port = randint(1000, 65000)
        try:
            print(col.find_one({"port": port}, {'port': 1})['port'])
            continue
        except:
            port = col.insert_one({"port": port, "connections": 1})
            id = port.inserted_id
            result = col.find_one({"_id": id})
            return result['port']

PORT = get_port()
HOST = '10.1.76.30'

# ideia de porta aleatoria, ter no banco só as que não posso usar, e verificar no banco se existir, se não existir colocar






# *_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove[nickname]
            break
    
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat".encode("ascii"))
        client.send("Connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print('Server is listening...')
receive()