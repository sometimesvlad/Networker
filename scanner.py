from termcolor import colored
import socket
from socket import timeout

def scanWrapper():
    def singlePortScan():
        color_b = colored("[!] ", "red")
        color_c = colored("[*] ", "yellow")
        closed = colored("[CLOSED]", "red")
        listen = colored("[OPEN]", "yellow")

        host = input("[$2] set HOST —> ")
        port = input("[$2] set PORT —> ")
        port=int(port)
        try:
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(1)
            scan.connect((host, port))
            scan.send(b'WhoAreYou\r\n')
            banner = scan.recv(100)
        except socket.error:
            print(color_b + str(port) + " -- " + closed)
        else:
            print(color_c + str(port) + " -- " + listen)
            print(banner.decode("utf-8"))

    def listPortScan():
        color_b = colored("[!] ", "red")
        color_c = colored("[*] ", "yellow")
        closed = colored("[CLOSED]", "red")
        listen = colored("[OPEN]", "yellow")

        host = input("[$2] RHOST --> ")
        #edit if you need custom port list
        port = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 443]
        for i in port:
            try:
                scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scan.settimeout(1)
                scan.connect((host, i))
                scan.send(b'WhoAreYou\r\n')
                banner = scan.recv(100)
            except socket.timeout:
                print(color_b + str(i) + " -- " + closed)
            else:
                print(color_c + str(i) + " -- " + listen)
                print(banner.decode("utf-8"))

    print("*"*50)
    print("\t[1]  ---  Single Port Scan")
    print("\t[2]  ---  List Port Scan")
    print("*"*50)

    action = input("[$2] Set scan type >> ")
    if action=="1":
        singlePortScan()
    elif action=="2":
        listPortScan()
    else:
        print("Ti cho durak blyat nahuya ti jmesh drugie chisla, eto ne ya govnokoder eto ti ebanat)))")

