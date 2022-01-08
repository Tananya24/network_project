import socket
import select
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv)!=3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address,Port))
while True:
    socket_list = [sys.stdin, server]
    read_sockets,write_socket,error_socket =select
    for socks in read_sockets:
        if socks == read_sockets:
            message = socket.recv(2048)
            print(message)
        else:
            message = socket.stdin.readline()
            server.send(message)
            sys.stdout.write("<YOU>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
        
        