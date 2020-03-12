from scanner import scanWrapper
from reverseshServer import reverseshWrapper

print(" ")
print("Welcome to Networker - penetration testing tool for combat situations")
print(" ") 
print("\t[1] Reverse shell server")
print("\t[2] Port Scanner")
print("\t[3] Help")
print(" ")


if __name__ == "__main__":
    while True:
        action = input("[*] Load module >> ")
        if action == "1":
            print("[!] Reverse shell module activated...")
            reverseshWrapper()
            break
        elif action == "2":
            print("[!] Port scanner module activated...")
            scanWrapper()
            break
        elif action == "3":
            print("[!] Manual module activated...")
            print(" ")
            print("\t\t\t\t\t*** MANUAL ***")
            print(" ")
            print("REVERSE SHELL MODULE - set your public IP/port to listen for incoming connections,\n                       then start backdoor.py on target machine to get reverse shell")
            print("PORT SCANNER MODULE  - poor Nmap, set scan type [1] Single port scan or [2] List port scan \n                       to get some information about target machine")
            break
        else:
            print("[!] Unrecognized module choosed")
            continue
