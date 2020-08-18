#!/usr/bin/python3
import socket, sys

#================================ Global Variables ====================================

buffer=1024
message=b"Client Request"
usage = "Usage: python3 PacketClient.py -tcp/udp <host> <port>"

#================================== TCP Request ==================================

def tcpRequest():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(message)
        responce = s.recv(buffer)
        print("Responce:", str(repr(responce)))
        s.close()
    except socket.error:
        print("Error connecting to:", host, ":", port)

#================================== UDP Request ==================================

def udpRequest():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message,(host,port))
        responce = s.recv(buffer)
        print("Responce:", str(repr(responce)))
        s.close()
    except socket.error:
        print("Error connecting to:", host, ":", port)


#================================== Argument Parser & Stager ============================================

if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            protocol = sys.argv[1]
            host = sys.argv[2]
            port = int(sys.argv[3])

            if protocol == "-tcp":
                tcpRequest()
            elif protocol == "-udp":
                udpRequest()
        else:
            raise ValueError
        
    except ValueError:
        print(usage)

#================================== To-Do ============================================
# - Raw sockets: spoofed sender
# - Payload support
# - Network layer protocols (ICMP etc..)