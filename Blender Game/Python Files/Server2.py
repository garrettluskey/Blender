import socket
import threading
import struct

host = '127.0.0.1'
port = 55455

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
print("Server Started.")
#addrList = []
#sformat = 'i'

def main():
    looping = True
    print("waiting")
    while True:
        data, addr = s.recvfrom(1024)
        print("connection from:" + str(addr)+ '  ' + 'recieved ->' + str(struct.unpack('ffffff',data)))
        
        #s.sendto(data, addr)
        #print("data recieved" + str(data))
        
    s.close()
main()
