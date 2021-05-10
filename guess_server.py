import socket
import random

ls = socket.socket()
ls.bind(('127.0.0.1', 9999))
ls.listen()

s, addr = ls.accept()
r = random.randint(1,100)
print(r)
w = 0
for i in range(5):
    s.sendall(b'GUESS\n')
    data = b''
    while b'\n' not in data:
        data += s.recv(1024)
    if int(data.decode()) < r:
        s.sendall(b'LOW\n')
    elif int(data.decode()) > r:
        s.sendall(b'HIGH\n')
    else:
        w = 1
        break
if w:
  s.sendall(b'WIN\n')
  s.close()
else:
  s.sendall(b'GAMEOVER\n')
  print('Real value: ' + str(r))
s.close()
