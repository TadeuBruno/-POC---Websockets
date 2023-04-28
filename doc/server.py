import threading
import socket

porta = 3010 
ip = '172.28.80.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)