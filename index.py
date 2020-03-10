from scanner import scanWrapper
from bindshClient import bindshWrapper

print("\t[1] Bind shell client")
print("\t[2] Handle incoming TCP connections")
print("\t[3] Port scanner")
print(" ")


if __name__ == "__main__":
    while True:
        action = input("[*] Load module >> ")
        if action == "1":
            print("[!] TCP connection module activated...")
            bindshWrapper()
            break
        elif action == "2":
            print("[2] item2")
            break
        elif action == "3":
            print("[!] Port scanner module activated...")
            scanWrapper()
            break
        else:
            print("[!] Error")