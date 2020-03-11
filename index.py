from scanner import scanWrapper
from reverseshServer import reverseshWrapper


print("\t[1] Reverse shell server")
print("\t[2] Port Scanner")
print("\t[3] Help")
print(" ")


if __name__ == "__main__":
    while True:
        action = input("[*] Load module >> ")
        if action == "1":
            print("[!] TCP connection module activated...")
            reverseshWrapper()
            break
        elif action == "2":
            print("[!] Port scanner module activated...")
            scanWrapper()
            break
        elif action == "3":
            print("Help")
            break
        else:
            print("[!] Error")