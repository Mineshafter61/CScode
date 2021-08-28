from hangman_modules import *
import socket
listen_socket = socket.socket()
listen_socket.bind(("127.0.0.1", 9999))
listen_socket.listen()

while True:
  s, addr = listen_socket.accept()
  received = b''
  s.sendall(b"Welcome to my Hangman game!")
  secret = getSecret()
  num_guess = len(secret)*2
  guessed = []
  show = reveal(secret, guessed)
  win = False
  data = s.recv(1024)
  if data.decode() = 'I am ready to play!':
    for i in range(num_guess):
      msg = 'GUESS,'+str(num_guess-1)+'\n'
      s.sendall(msg.encode())
      guessed.append(data.decode())
      show = reveal(secret, guessed)
      if show == secret:
        win = True
        s.sendall(b'WIN\n')
        print("CLIENT WIN")
        break
      elif i == num_guess - 1:
        msg = "LOSE...The word is {}\n".format(secret)
        print(msg)
        s.sendall(msg.encode())
      else:
        mssg = show+'\n'
        s.sendall(msg.encode())
