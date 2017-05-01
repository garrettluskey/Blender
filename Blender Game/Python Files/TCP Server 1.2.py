import socket
import threading

def getinfo(conn):
    while True:
        info = conn.
        
        if info != 0:
            info = conn.recv(1024)
        else:
            conn.close()
            break
    conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 2000
s.bind((host,port))
s.listen(5)
def main():
    while True:
        print('waiting for new connection')
        conn, addr = s.accept()
        print(addr)
        getinfothread = threading.Thread(target=getinfo, args=[conn])
        getinfothread.start()



main()

