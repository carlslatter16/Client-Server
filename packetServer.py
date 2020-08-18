#!/usr/bin/python3
import socket, sys

#================================ Global Variables ====================================

interfaceAddr='127.0.0.1' 
buffer=1024
usage = "Usage: python3 PacketServer.py -tcp/udp <port>"
message=b"Server Responce"

#================================ Setup TCP/UDP Interface Bind ====================================

def tcpBind():
    print(interfaceAddr,":", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((interfaceAddr, port))
    tcpListen(s)

def udpBind():
    print(interfaceAddr, ":", port)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((interfaceAddr, port))
    udpListen(s)

#================================== TCP Listener & Responder ==================================

def tcpRespond(conn, addr, s):
    try:
        data = conn.recv(buffer)

        if data:
            print("Message: ",  data)
            conn.sendall(message)
            conn.close()
            tcpListen(s)

    except socket.error:
        print("A binding error occured - possible half-open scanning?")

def tcpListen(s):
    s.listen(1)
    conn, addr = s.accept()
    print('Incoming IP:', addr)
    while True:
        tcpRespond(conn, addr, s)


#=================================== UDP Listener & Responder ===========================================

def udpRespond(s, connPair):
    s.sendto(message, connPair[1])
    udpListen(s)

def udpListen(s):
    while(True):
        connPair = s.recvfrom(buffer)
        print("Message:{}".format(connPair[0]))
        print("Incoming IP:{}".format(connPair[1]))
        udpRespond(s, connPair)

#================================== Argument Parser & Stager ============================================

if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            protocol = sys.argv[1]
            port = int(sys.argv[2])

            if protocol == "-tcp":
                tcpBind()
            elif protocol == "-udp":
                udpBind()
        else:
            raise ValueError
        
    except ValueError:
        print(usage)

#================================== To-Do ============================================
# - UDP scanning detection
# - Fragmented scan detection
# - DoS detection with ICMP listener
# - Nicer message output
# - Proper comments & docs