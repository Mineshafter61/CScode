import socket
import random

s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen()

r = random.randint(1,100)
s.sendall(b'GUESS')
for i in range(5):
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    if int(data.decode()) < r:
        s.sendall(b'LOW')
    elif int(data.decode()) > r:
        s.sendall(b'HIGH')
    else:
        s.sendall(b'WIN')
        s.close()
        break
if s:
    s.sendall(b'GAMEOVER')
    s.close()
