import socket
import threading
import re

clientsDict = {}


def send(connected, targetIp, targetPort, s):
    global clientsDict
    
    #converts seperate port and host into address
    addr = str(targetIp) + ':' + str(targetPort)
    
    while addr in clientsDict:
        
        #creates dictionary copy for thread
        sendDict = clientDict.copy()
        #removes the destinations data
        del sendDict[targetIp]
        #converts data into bytes
        byteinfo = bytes(sendDict, "UTF-8")
        #sends data
        s.sendto(byteinfo, (targetIP, targetPort))



def recieve(s, targetIp)
    global clientsDict
    data, addr = s.recvfrom(1048)
    if addr == str(targetIp) + ':' + str(targetPort):
        client{addr:data}
        cl


def connect(s, targetAddr)
    global clientsDict
    clientsDict[targetAddr] = None

def disconnect(s, targetAddr)
    global clientsDict
    del clientsDict[targetAddr]
def main():
    while True:
        tcp = socket.socet
        udp = socket.socket(AF_INET)
    
