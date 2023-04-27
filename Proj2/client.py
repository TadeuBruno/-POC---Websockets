import socket
import threading
import pymongo
nickname =input("Choose a nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cluster = pymongo.MongoClient("mongodb+srv://bruno:1234@cluster0.j7eftti.mongodb.net/?retryWrites=true&w=majority")
banco = cluster['Ports']
col = banco['available_ports']

def get_port_and_update():
    if(not col.find_one({"connections": {"$lte": 2}}, {"port": 1, "_id": 0}) == None):
        cliente_inserted = col.find_one_and_update({"connections": {"$lte": 2}}, {"$set": {"connections": col.find_one({"connections": {"$lte": 2}}, {"connections": 1, "_id": 0})['connections']+1}})
        return cliente_inserted['port']


client.connect(('10.1.76.30', get_port_and_update()))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode( 'ascii'))
            else:
                print(message)
        except:
            print('An error occured')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()