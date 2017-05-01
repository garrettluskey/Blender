import socket
from threading import Thread
import time

def sendinfo():
    s.connect(('127.0.0.1',2000))
    print('connected')
    while True:
        s.send(bytes('asdf', 'UTF-8'))
        time.sleep(1)
    



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def main():
    sendinfo()
main()
