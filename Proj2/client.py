import socket
import threading
import pymongo
# nickname =input("Choose a nickname: ")
nickname = 'Bruno'
# porta = int(input('Escolha a sua porta: '))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('172.28.80.1', 3003))

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